import os
import re
import urllib.request
import urllib.parse

BASE = "https://constructioncertification.co.uk"
OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")

PAGES = [
    "/", "/cscs-card-form", "/which-cscs-card-do-i-need", "/cscs-green-card",
    "/cscs-blue-card", "/black-card-test", "/red-card-test", "/gold-card-test",
    "/white-card-test", "/cscs-card-form-new", "/cscs-card-form-renew",
    "/cscs-card-form-replace", "/cscs-card-checker",
    "/skill-card/apply-for-a-skill-card", "/skill-card/which-skill-card-do-i-need",
    "/skill-card/what-is-a-skill-card", "/jib-card/jib-card-new-application",
    "/jib-card/which-jib-pmes-card-do-i-need", "/jib-card/what-is-a-jib-card",
    "/form", "/citb-test", "/which-test", "/locations", "/group", "/revision",
    "/citb-operatives-test-mock", "/citb-supervisors-test-mock",
    "/citb-working-at-heights-mock-test", "/citb-fire-extinguishers-mock-test",
    "/citb-signs-test", "/green-card-online-course",
    "/e-learning/eusr-national-water-hygiene-blue-virtual-card", "/list-nvq",
    "/e-learning", "/contact", "/faqs", "/cscs-green-card-online-course",
    "/sitemap", "/replace-a-cscs-card", "/terms", "/blog",
]

IMG_EXT_RE = r'(?:png|jpe?g|webp|gif|svg|ico)'
IMG_SRC_RE = re.compile(r'(?:src|srcset)=["\']([^"\']+)["\']', re.IGNORECASE)
CSS_URL_RE = re.compile(r'url\(\s*["\']?([^"\')]+)["\']?\s*\)', re.IGNORECASE)

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

def fetch(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=20) as resp:
        return resp.read().decode("utf-8", errors="ignore")

def extract_image_urls(html, page_url):
    found = set()
    for m in IMG_SRC_RE.finditer(html):
        raw = m.group(1)
        for part in raw.split(","):
            u = part.strip().split(" ")[0]
            if u:
                found.add(u)
    for m in CSS_URL_RE.finditer(html):
        found.add(m.group(1).strip())

    resolved = set()
    for u in found:
        if u.startswith("data:"):
            continue
        abs_url = urllib.parse.urljoin(page_url, u)
        parsed = urllib.parse.urlparse(abs_url)
        if parsed.netloc and "constructioncertification.co.uk" not in parsed.netloc:
            continue
        path = parsed.path.lower()
        if not re.search(IMG_EXT_RE + r'$', path):
            continue
        resolved.add(abs_url)
    return resolved

def dedupe_key(url):
    parsed = urllib.parse.urlparse(url)
    return parsed.netloc.replace("www.", "") + parsed.path

def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    all_images = {}  # dedupe_key -> full url
    crawled = 0
    failed_pages = []

    for path in PAGES:
        page_url = urllib.parse.urljoin(BASE, path)
        try:
            html = fetch(page_url)
        except Exception as e:
            failed_pages.append((page_url, str(e)))
            continue
        crawled += 1
        for img_url in extract_image_urls(html, page_url):
            key = dedupe_key(img_url)
            all_images.setdefault(key, img_url)

    print(f"Crawled {crawled}/{len(PAGES)} pages ({len(failed_pages)} failed)")
    print(f"Found {len(all_images)} unique images")

    used_names = set()
    downloaded = 0
    failed_downloads = []

    for key, url in sorted(all_images.items()):
        parsed = urllib.parse.urlparse(url)
        base_name = os.path.basename(parsed.path) or "image"
        base_name = urllib.parse.unquote(base_name)
        name, ext = os.path.splitext(base_name)
        candidate = base_name
        i = 1
        while candidate.lower() in used_names:
            candidate = f"{name}_{i}{ext}"
            i += 1
        used_names.add(candidate.lower())

        dest = os.path.join(OUT_DIR, candidate)
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=20) as resp:
                data = resp.read()
            with open(dest, "wb") as f:
                f.write(data)
            downloaded += 1
        except Exception as e:
            failed_downloads.append((url, str(e)))

    print(f"Downloaded {downloaded}/{len(all_images)} images to {OUT_DIR}")
    if failed_pages:
        print("Failed pages:")
        for u, e in failed_pages:
            print(f"  {u}: {e}")
    if failed_downloads:
        print("Failed downloads:")
        for u, e in failed_downloads:
            print(f"  {u}: {e}")

if __name__ == "__main__":
    main()
