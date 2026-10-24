# Construction Helps

A static marketing website for **Construction Helps** — an independent UK booking agent for CITB tests, CSCS cards (Green, Blue, Gold, Red, White, Black), Skill Cards, JIB Cards and construction e-learning courses.

Pure HTML / CSS / vanilla JS — no build step, no dependencies. Ready to deploy straight to GitHub Pages.

## Pages

| Page | File |
| --- | --- |
| Home | `index.html` |
| CSCS Cards overview | `cards.html` |
| Individual card pages | `green-card.html`, `blue-card.html`, `gold-card.html`, `red-card.html`, `white-card.html`, `black-card.html` |
| Skill Card | `skill-card.html` |
| JIB Card | `jib-card.html` |
| CITB Test booking | `citb-test.html` |
| E-Learning courses | `e-learning.html` |
| About | `about.html` |
| Contact | `contact.html` |

## Structure

```
index.html, cards.html, ...html   – the site pages (flat, no build step needed)
assets/css/style.css              – shared stylesheet
assets/js/main.js                 – nav toggle, FAQ accordion, back-to-top, contact form
images/                           – photos, card mock-ups and accreditation logos
construction_logo.svg             – site logo, used in the header/footer and as favicon
build_site.py                     – optional generator that produces all the .html files
```

## Editing content

All pages are generated from `build_site.py` (a single Python script, stdlib only) so copy, contact details and card data stay consistent across every page. To change something:

1. Edit the relevant text/data in `build_site.py` (e.g. the `SITE` dict for contact details, or the `CARDS` list for card content).
2. Regenerate the HTML files:
   ```
   python build_site.py
   ```

You can also edit the generated `.html` files directly if you prefer — they're plain static HTML and won't be overwritten unless you rerun the script.

## Running locally

Any static file server works, e.g.:

```
python -m http.server 8080
```

Then open `http://localhost:8080`.

## Deploying to GitHub Pages

1. Push this folder to a new GitHub repository.
2. In the repo settings, go to **Pages** and set the source to the `main` branch, root folder.
3. Your site will be published at `https://<username>.github.io/<repo-name>/`.

No build step is required — GitHub Pages serves the HTML/CSS/JS files as-is.
