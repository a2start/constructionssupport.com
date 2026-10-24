# Generates the static Construction Helps website (run once to (re)build the .html files).
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

SITE = {
    "name": "Construction Helps",
    "phone1": "0203 400 8738",
    "phone1_tel": "02034008738",
    "phone2": "0333 303 1186",
    "phone2_tel": "03333031186",
    "email": "Info@constructionhelps.com",
    "address": "71-75 Shelton Street, Covent Garden, London, United Kingdom, WC2H 9JQ",
}

NAV_ITEMS = [
    ("index.html", "Home"),
]

CARDS = [
    {
        "slug": "green-card", "name": "Green Card", "short": "Labourer",
        "theme": "green", "hex": "#2e7d32",
        "hero_img": "images/Green-Labourer-(1)-(2).webp",
        "tile_img": "images/11-Green-MateAssistant.png",
        "tagline": "The starting point for anyone new to construction site work.",
        "intro": [
            "The CSCS Green Card is the entry-level card held by labourers and mates working on UK construction sites. "
            "It confirms that the holder has passed the CITB Health, Safety &amp; Environment (HS&amp;E) test and understands the basic "
            "health and safety standards expected on site.",
            "It's the most common starting point for people entering the industry without a formal trade qualification yet, and it "
            "gives you the right to be on site while you begin working towards an NVQ.",
        ],
        "who": [
            "New starters and general labourers working on site",
            "Mates and assistants supporting skilled tradespeople",
            "Anyone beginning their career in construction before enrolling on an NVQ",
        ],
        "requirements": [
            "Pass the CITB Operatives Health, Safety &amp; Environment test",
            "Provide proof of identity for your application",
            "Be working towards, or planning to enrol on, a relevant NVQ Level 1 or 2",
        ],
        "validity": "5 years", "level": "Entry level", "test": "CITB Operatives HS&E Test",
        "subtypes": None,
    },
    {
        "slug": "blue-card", "name": "Blue Card", "short": "Skilled Worker",
        "theme": "blue", "hex": "#1565c0",
        "hero_img": "images/1---Plumber-Blue.png",
        "tile_img": "images/4-Blue-Skilled-Worker.png",
        "tagline": "For qualified tradespeople who have proven their skills with an NVQ Level 2.",
        "intro": [
            "The CSCS Blue Card is held by skilled workers who have achieved an NVQ or SVQ Level 2 (or an equivalent recognised "
            "qualification) in their chosen construction occupation, such as plumbing, bricklaying or carpentry.",
            "It's a clear signal to site managers that the holder has the practical competence and up-to-date health and safety "
            "knowledge required to work independently in their trade.",
        ],
        "who": [
            "Qualified tradespeople with an NVQ/SVQ Level 2",
            "Skilled operatives moving up from a Green or Red card",
            "Plumbers, electricians, bricklayers and other trade specialists",
        ],
        "requirements": [
            "Hold an NVQ/SVQ Level 2 (or approved equivalent) in a relevant construction occupation",
            "Pass the CITB Operatives Health, Safety &amp; Environment test",
            "Provide evidence of your qualification when applying",
        ],
        "validity": "5 years", "level": "Skilled worker", "test": "CITB Operatives HS&E Test",
        "subtypes": None,
    },
    {
        "slug": "gold-card", "name": "Gold Card", "short": "Advanced Craft / Supervisor",
        "theme": "gold", "hex": "#b8860b",
        "hero_img": "images/8-Gold-Supervisor.png",
        "tile_img": "images/9-Gold-Advanced-Craft.png",
        "tagline": "For advanced craftspeople and supervisors with Level 3 qualifications.",
        "intro": [
            "The CSCS Gold Card recognises two groups: Advanced Craftspeople who hold an NVQ/SVQ Level 3 in their trade, and "
            "Supervisors who combine a Level 3 qualification with recognised supervisory training.",
            "Gold Card holders are typically the most experienced hands-on tradespeople on site, often leading small teams or "
            "taking responsibility for the quality and safety of a work area.",
        ],
        "who": [
            "Experienced tradespeople with an NVQ/SVQ Level 3",
            "Site supervisors responsible for a team or work area",
            "Workers progressing from a Blue Card into a senior craft role",
        ],
        "requirements": [
            "Hold an NVQ/SVQ Level 3 (Advanced Craft) or a supervisory qualification alongside a Level 3",
            "Pass the CITB Operatives or Supervisors HS&E test as applicable",
            "Provide evidence of your qualification and, for supervisors, your role on site",
        ],
        "validity": "5 years", "level": "Advanced / supervisory", "test": "CITB Operatives / Supervisors HS&E Test",
        "subtypes": None,
    },
    {
        "slug": "red-card", "name": "Red Card", "short": "Trainee / Provisional / Apprentice",
        "theme": "red", "hex": "#c62828",
        "hero_img": "images/2-Red-Trainee.png",
        "tile_img": "images/1-Red-Industry-Placement-Card.png",
        "tagline": "Temporary cards for people who are training or new to the industry.",
        "intro": [
            "Red Cards cover several temporary categories for people who are part-way through their construction career: "
            "trainees enrolled on an NVQ, apprentices, provisional card holders who are new to the industry, students on an "
            "industry placement, and experienced workers awaiting a formal assessment.",
            "Because there are several Red Card types, it's important to apply for the one that matches your exact circumstances "
            "— our team will help you choose the right one.",
        ],
        "who": [
            "Apprentices enrolled on a recognised apprenticeship",
            "Trainees registered on an NVQ/SVQ but not yet complete",
            "New entrants awaiting enrolment onto a qualification (Provisional)",
            "Students on a college or university industry placement",
            "Experienced workers awaiting a formal on-site assessment",
        ],
        "requirements": [
            "Pass the relevant CITB Health, Safety &amp; Environment test",
            "Provide evidence of enrolment on an NVQ, apprenticeship or placement (where applicable)",
            "Apply for the correct Red Card sub-type for your situation",
        ],
        "validity": "1–3 years depending on sub-type", "level": "Trainee / temporary", "test": "CITB HS&E Test",
        "subtypes": [
            {"name": "Trainee", "img": "images/Red-Trainee-(1).png", "desc": "For workers registered on an NVQ/SVQ who have not yet completed it."},
            {"name": "Apprentice", "img": "images/Red-Apprentice.jpg", "desc": "For those enrolled on a recognised construction apprenticeship."},
            {"name": "Provisional", "img": "images/Red-Provisional-(2).webp", "desc": "For new entrants who have passed the test but not yet enrolled on an NVQ."},
            {"name": "Industry Placement", "img": "images/Red-Industry-placement.png", "desc": "For students undertaking an industry placement as part of a course."},
            {"name": "Experienced Worker", "img": "images/Red-Technical-Experienced-(1).jpg", "desc": "For experienced workers awaiting a formal on-site assessment."},
        ],
    },
    {
        "slug": "white-card", "name": "White Card", "short": "Academically / Professionally Qualified",
        "theme": "silver", "hex": "#6b7280",
        "hero_img": "images/5-White-Academically-Qualified-Person-AQP.png",
        "tile_img": "images/6-White-Professionally-Qualified-Person-PQP.png",
        "tagline": "For degree-level professionals working towards full construction NVQs.",
        "intro": [
            "The White Card is a temporary, non-renewable card for people who hold a relevant degree, professional "
            "qualification or membership, but who have not yet completed a full construction NVQ.",
            "It covers Academically Qualified Persons (AQP), Professionally Qualified Persons (PQP), and specialist "
            "categories such as ACRIB refrigerant handlers, giving qualified professionals time-limited site access "
            "while their NVQ is finalised.",
        ],
        "who": [
            "Graduates with a construction-related degree",
            "Members of a relevant professional body (PQP)",
            "Specialist technicians such as ACRIB-registered refrigerant handlers",
        ],
        "requirements": [
            "Hold a relevant degree or professional membership",
            "Pass the CITB Managers &amp; Professionals or Operatives HS&E test as applicable",
            "Provide evidence of your qualification or membership",
        ],
        "validity": "1 year (non-renewable)", "level": "Qualified professional", "test": "CITB HS&E Test",
        "subtypes": [
            {"name": "Academically Qualified Person (AQP)", "img": "images/White-AQ.webp", "desc": "Holders of a relevant construction-related degree."},
            {"name": "Professionally Qualified Person (PQP)", "img": "images/White-PQ.webp", "desc": "Members of a recognised professional body in construction."},
            {"name": "ACRIB Refrigerant Handler", "img": "images/7-White-ACRIB-Refrigerant-Handler.png", "desc": "Specialist card for registered refrigerant handling technicians."},
        ],
    },
    {
        "slug": "black-card", "name": "Black Card", "short": "Manager",
        "theme": "black", "hex": "#1a1a1a",
        "hero_img": "images/Black-Managers.webp",
        "tile_img": "images/Black-Managers.webp",
        "tagline": "The senior card for construction managers and directors.",
        "intro": [
            "The CSCS Black Card is held by construction managers who have achieved an NVQ/SVQ Level 4, 5 or higher, "
            "or an equivalent management qualification recognised by CSCS.",
            "It confirms that the holder has the knowledge and experience to manage people, resources, quality and "
            "safety across a construction project.",
        ],
        "who": [
            "Site and project managers",
            "Construction directors and senior management staff",
            "Anyone holding an NVQ/SVQ Level 4 or above in construction management",
        ],
        "requirements": [
            "Hold an NVQ/SVQ Level 4, 5 or an equivalent management qualification",
            "Pass the CITB Managers &amp; Professionals Health, Safety &amp; Environment test",
            "Provide evidence of your qualification and management role",
        ],
        "validity": "5 years", "level": "Manager", "test": "CITB Managers & Professionals HS&E Test",
        "subtypes": None,
    },
]

OTHER_CARDS = [
    {"slug": "skill-card", "name": "Skill Card", "short": "Building Services", "hex": "#6a1b9a"},
    {"slug": "jib-card", "name": "JIB Card", "short": "Electrical / Mechanical", "hex": "#0d47a1"},
]

CARD_LOOKUP = {c["slug"]: c for c in CARDS}

MOCK_TESTS = [
    {
        "slug": "citb-operatives-mock-test", "name": "CITB Operatives Mock Test",
        "audience": "Operatives, labourers and general construction workers",
        "covers": "General health and safety knowledge required for the standard CITB Operatives test &mdash; the most common CITB test route into a Green or Blue CSCS card.",
        "topics": ["General responsibilities", "Accident reporting and first aid", "Health and welfare", "Manual handling and PPE", "Fire prevention basics"],
    },
    {
        "slug": "citb-supervisors-mock-test", "name": "CITB Supervisors Mock Test",
        "audience": "Site supervisors and team leaders",
        "covers": "Supervisory responsibilities, health and safety leadership, and site management scenarios required for the Supervisors HS&amp;E test.",
        "topics": ["Supervisory responsibilities", "Risk assessment and method statements", "Managing a team's safety", "Incident and near-miss handling", "Site inspections"],
    },
    {
        "slug": "citb-working-at-heights-mock-test", "name": "CITB Working At Heights Mock Test",
        "audience": "Anyone working at height on site",
        "covers": "Fall prevention, safe use of ladders, scaffolding and harnesses, and the working at height regulations that apply on UK construction sites.",
        "topics": ["Working at Height Regulations 2005", "Ladder and stepladder safety", "Scaffolding basics", "Harnesses and fall arrest systems", "Edge protection"],
    },
    {
        "slug": "citb-fire-extinguishers-mock-test", "name": "CITB Fire Extinguishers Mock Test",
        "audience": "Fire marshals and general site workers",
        "covers": "Fire extinguisher types, correct usage and basic fire safety awareness expected on a construction site.",
        "topics": ["Classes of fire", "Extinguisher colour coding", "Correct extinguisher for each fire type", "Evacuation procedures", "Fire risk awareness"],
    },
    {
        "slug": "citb-safety-signs-test", "name": "CITB Safety Signs Test",
        "audience": "All construction workers",
        "covers": "Recognising and understanding the mandatory, warning, prohibition and safe condition signs used across UK construction sites.",
        "topics": ["Prohibition signs", "Warning signs", "Mandatory signs", "Safe condition signs", "Fire safety signs"],
    },
]

# ---------------------------------------------------------------- helpers --

def nav_dropdown():
    items = "".join(
        '<li><a href="{slug}.html"><span class="swatch" style="background:{hex}"></span>{name}</a></li>'.format(
            slug=c["slug"], hex=c["hex"], name=c["name"]
        )
        for c in CARDS
    )
    return items

def head(title, description):
    return """<meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | {site}</title>
  <meta name="description" content="{desc}">
  <link rel="icon" href="construction_logo.svg" type="image/svg+xml">
  <link rel="stylesheet" href="assets/css/style.css">
""".format(title=title, site=SITE["name"], desc=description)

def header_html():
    return """<header class="site-header">
    <div class="container nav">
      <a href="index.html" class="brand">
        <img src="construction_logo.svg" alt="{site} logo">
      </a>
      <ul class="nav-links">
        <li><a href="index.html">Home</a></li>
        <li class="has-dropdown">
          <a href="cards.html">CSCS Cards</a>
          <ul class="dropdown">
            {dropdown}
            <li><a href="cards.html"><span class="swatch" style="background:#0d78f2"></span>All Cards Overview</a></li>
          </ul>
        </li>
        <li class="has-dropdown">
          <a href="skill-card.html">Other Cards</a>
          <ul class="dropdown">
            <li><a href="skill-card.html"><span class="swatch" style="background:#6a1b9a"></span>Skill Card</a></li>
            <li><a href="jib-card.html"><span class="swatch" style="background:#0d47a1"></span>JIB Card</a></li>
            <li><a href="ecs-card.html"><span class="swatch" style="background:#c62828"></span>ECS Card</a></li>
            <li><a href="cpcs-card.html"><span class="swatch" style="background:#1565c0"></span>CPCS Card</a></li>
          </ul>
        </li>
        <li class="has-dropdown">
          <a href="citb-test.html">CITB Test</a>
          <ul class="dropdown">
            <li><a href="citb-test.html">Book CITB Test</a></li>
            <li><a href="which-citb-test.html">Which Test Do I Need?</a></li>
            <li><a href="test-centres.html">Test Centres</a></li>
            <li><a href="group-test-booking.html">Group Test Booking</a></li>
            <li><a href="citb-revision.html">Revision Material</a></li>
            <li><a href="citb-mock-tests.html">CITB Mock Tests</a></li>
          </ul>
        </li>
        <li><a href="e-learning.html">E-Learning</a></li>
        <li><a href="faqs.html">FAQs</a></li>
        <li><a href="about.html">About</a></li>
        <li><a href="contact.html">Contact</a></li>
      </ul>
      <div class="nav-cta">
        <a href="tel:{phone1_tel}" class="btn btn-outline btn-sm">Call {phone1}</a>
        <a href="contact.html" class="btn btn-primary btn-sm">Get Started</a>
        <button class="nav-toggle" aria-label="Toggle menu"><span></span><span></span><span></span></button>
      </div>
    </div>
  </header>""".format(site=SITE["name"], dropdown=nav_dropdown(), phone1_tel=SITE["phone1_tel"], phone1=SITE["phone1"])

def topbar_html():
    return """<div class="topbar">
    <div class="container">
      <div class="topbar__contacts">
        <a href="tel:{phone1_tel}" class="topbar__primary">📞 {phone1}</a>
        <a href="tel:{phone2_tel}" class="topbar__secondary">📞 {phone2}</a>
        <a href="mailto:{email}" class="topbar__secondary">✉ {email}</a>
        <span class="topbar__secondary">📍 Covent Garden, London</span>
      </div>
      <div class="topbar__social">
        <a href="#" aria-label="Facebook">FB</a>
        <a href="#" aria-label="Twitter">X</a>
        <a href="#" aria-label="LinkedIn">IN</a>
      </div>
    </div>
  </div>""".format(**SITE)

def trust_strip():
    logos = [
        ("images/CPD-Logo.jpg", "CPD Certified"),
        ("images/IIRSM-Horizontal-Logo-Mar-26---Sept-27.jpg", "IIRSM Approved"),
        ("images/NEBOSH-Certified-Gold807-Logo-Landscape-Large-(1).png", "NEBOSH Affiliate"),
        ("images/EUSR_EL_Logo_RGB-(1).jpg", "EUSR Registered"),
        ("images/ISEP-full-name-black-RGB-(1).png", "ISEP Member"),
    ]
    items = "".join('<img src="{src}" alt="{alt}" loading="lazy">'.format(src=s, alt=a) for s, a in logos)
    return """<div class="trust-strip">
    <div class="container">
      <span class="trust-strip__label">Trusted &amp; Recognised By</span>
      <div class="trust-strip__logos">{items}</div>
    </div>
  </div>""".format(items=items)

def footer_html():
    return """<footer class="site-footer">
    <div class="container footer-top">
      <div class="footer-brand">
        <img src="construction_logo.svg" alt="{site} logo">
        <p>Construction Helps is your independent booking partner for CITB tests, CSCS, Skill and JIB cards, and
        online construction e-learning across the United Kingdom.</p>
        <div class="footer-social">
          <a href="#" aria-label="Facebook">FB</a>
          <a href="#" aria-label="Twitter">X</a>
          <a href="#" aria-label="LinkedIn">IN</a>
          <a href="#" aria-label="Instagram">IG</a>
        </div>
      </div>
      <div>
        <h4>CSCS Cards</h4>
        <ul class="flinks">
          {card_links}
        </ul>
      </div>
      <div>
        <h4>Quick Links</h4>
        <ul class="flinks">
          <li><a href="citb-test.html">CITB Test Booking</a></li>
          <li><a href="which-citb-test.html">Which Test Do I Need?</a></li>
          <li><a href="test-centres.html">Find A Test Centre</a></li>
          <li><a href="citb-mock-tests.html">CITB Mock Tests</a></li>
          <li><a href="skill-card.html">Skill Card</a></li>
          <li><a href="jib-card.html">JIB Card</a></li>
          <li><a href="ecs-card.html">ECS Card</a></li>
          <li><a href="cpcs-card.html">CPCS Card</a></li>
          <li><a href="e-learning.html">E-Learning Courses</a></li>
          <li><a href="about.html">About Us</a></li>
          <li><a href="contact.html">Contact Us</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact</h4>
        <ul class="footer-contact">
          <li><span class="ico">📍</span><span>{address}</span></li>
          <li><span class="ico">📞</span><a href="tel:{phone1_tel}">{phone1}</a></li>
          <li><span class="ico">📞</span><a href="tel:{phone2_tel}">{phone2}</a></li>
          <li><span class="ico">✉</span><a href="mailto:{email}">{email}</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <div class="container footer-bottom__row">
        <span>&copy; <span class="js-year">2026</span> {site}. All rights reserved.</span>
        <nav class="footer-legal">
          <a href="terms.html">Terms &amp; Conditions</a>
          <a href="privacy.html">Privacy Policy</a>
          <a href="refund-policy.html">Refund Policy</a>
          <a href="disclaimer.html">Disclaimer</a>
          <a href="faqs.html">FAQs</a>
        </nav>
      </div>
      <div class="container">
        <span class="footer-disclaimer">Construction Helps is an independent booking agent and is not affiliated with CSCS, CITB, JIB, ECS or CPCS.</span>
      </div>
    </div>
  </footer>
  <button class="back-to-top" aria-label="Back to top">↑</button>
  <script src="assets/js/main.js"></script>""".format(
        site=SITE["name"],
        address=SITE["address"],
        phone1=SITE["phone1"], phone1_tel=SITE["phone1_tel"],
        phone2=SITE["phone2"], phone2_tel=SITE["phone2_tel"],
        email=SITE["email"],
        card_links="".join('<li><a href="{slug}.html">{name}</a></li>'.format(slug=c["slug"], name=c["name"]) for c in CARDS),
    )

def page(title, description, body, extra_head=""):
    return """<!DOCTYPE html>
<html lang="en-GB">
<head>
  <!-- Google Tag Manager -->
  <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
  new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
  j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
  'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
  })(window,document,'script','dataLayer','GTM-MNDJT59Q');</script>
  <!-- End Google Tag Manager -->
  {head}{extra_head}
</head>
<body>
  <!-- Google Tag Manager (noscript) -->
  <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-MNDJT59Q"
  height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
  <!-- End Google Tag Manager (noscript) -->
  {topbar}
  {header}
  {body}
  {footer}
</body>
</html>
""".format(
        head=head(title, description),
        extra_head=extra_head,
        topbar=topbar_html(),
        header=header_html(),
        body=body,
        footer=footer_html(),
    )

def other_cards_strip(exclude_slug=None, title="Explore The Other Cards"):
    tiles = ""
    for c in CARDS:
        if c["slug"] == exclude_slug:
            continue
        tiles += """<a href="{slug}.html" class="other-card">
          <span class="ring" style="border-color:{hex}; color:{hex}">{initial}</span>
          <span>{name}</span>
        </a>""".format(slug=c["slug"], hex=c["hex"], initial=c["name"][0], name=c["name"])
    return """<div class="section section--alt">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">CSCS Card Family</span>
        <h2>{title}</h2>
        <p>Not sure which card matches your role? Compare all six CSCS card colours at a glance.</p>
      </div>
      <div class="other-cards">{tiles}</div>
      <div class="text-center" style="margin-top:28px;">
        <a href="cards.html" class="btn btn-outline">View Full Card Comparison</a>
      </div>
    </div>
  </div>""".format(title=title, tiles=tiles)

def cta_band(heading="Ready To Get Your Card Sorted?", text="Just call us on 0203 400 8738 and our team will take care of the rest."):
    return """<div class="container">
    <div class="cta-band">
      <div>
        <h2>{heading}</h2>
        <p>{text}</p>
      </div>
      <div class="cta-band__actions">
        <a href="citb-test.html" class="btn btn-light">Book CITB Test</a>
        <a href="tel:{phone1_tel}" class="btn btn-white-outline">Call {phone1}</a>
      </div>
    </div>
  </div>""".format(heading=heading, text=text, phone1_tel=SITE["phone1_tel"], phone1=SITE["phone1"])

def breadcrumb(current, theme="", eyebrow="", h1="", lead=""):
    return """<div class="page-hero theme-{theme}">
    <div class="container">
      <div class="breadcrumb"><a href="index.html">Home</a> / {current}</div>
      <span class="eyebrow" style="background:rgba(255,255,255,.12); color:#fff;">{eyebrow}</span>
      <h1>{h1}</h1>
      <p>{lead}</p>
    </div>
  </div>""".format(theme=theme, current=current, eyebrow=eyebrow, h1=h1, lead=lead)

# ---------------------------------------------------------------- pages ----

def build_home():
    services = [
        ("🧪", "CITB Test Booking", "Book your CITB Health, Safety &amp; Environment test at over 150 approved test centres nationwide.", "citb-test.html"),
        ("🪪", "CSCS Card Applications", "Apply for Green, Blue, Gold, Red, White or Black CSCS cards with our guided application service.", "cards.html"),
        ("🔧", "Skill Card", "Building services engineering card applications for the mechanical and electrical trades.", "skill-card.html"),
        ("⚡", "JIB Card", "Joint Industry Board card support for electrical and mechanical engineering professionals.", "jib-card.html"),
        ("💻", "Online E-Learning", "Complete Health, Safety &amp; Awareness and specialist courses online, from home.", "e-learning.html"),
        ("📍", "150+ Test Centres", "Find your nearest CITB test centre in any major UK city and book a convenient slot.", "test-centres.html"),
    ]
    service_cards = "".join("""<div class="service-card">
        <div class="service-card__icon">{icon}</div>
        <h3>{title}</h3>
        <p>{desc}</p>
        <a href="{link}" class="link-arrow">Learn more &rarr;</a>
      </div>""".format(icon=i, title=t, desc=d, link=l) for i, t, d, l in services)

    tiles = ""
    for c in CARDS:
        tiles += """<a href="{slug}.html" class="card-tile">
        <div class="card-tile__media"><img src="{img}" alt="{name}" loading="lazy"></div>
        <div class="card-tile__body">
          <div class="card-tile__strip" style="background:{hex}"></div>
          <h3>{name}</h3>
          <p>{tagline}</p>
        </div>
      </a>""".format(slug=c["slug"], img=c["tile_img"], name=c["name"], hex=c["hex"], tagline=c["tagline"])

    steps = [
        ("Choose Your Card", "Tell us your trade, qualifications and experience — we'll confirm which CSCS, Skill or JIB card fits."),
        ("Book &amp; Pass Your Test", "We book your CITB Health, Safety &amp; Environment test at a nearby approved centre."),
        ("Call Us &amp; Relax", "Just call us on 0203 400 8738 and our team will take care of the rest — application, updates and delivery."),
    ]
    steps_html = "".join("""<div class="step"><h3>{t}</h3><p>{d}</p></div>""".format(t=t, d=d) for t, d in steps)

    testimonials = [
        ("Ryan D.", "General Labourer", "Booked my CITB test and had my Green Card within a couple of weeks. Simple process from start to finish."),
        ("Amara K.", "Plumbing Apprentice", "The team explained exactly which Red Card I needed as an apprentice. Really helpful and quick to respond."),
        ("Tomasz W.", "Site Supervisor", "Renewed my Gold Card with no hassle at all. Would recommend to anyone in the trade."),
    ]
    testimonials_html = "".join("""<div class="testimonial">
        <div class="testimonial__stars">★★★★★</div>
        <p>&ldquo;{q}&rdquo;</p>
        <div class="testimonial__who">
          <div class="testimonial__avatar">{init}</div>
          <div><strong>{name}</strong><span>{role}</span></div>
        </div>
      </div>""".format(q=q, name=n, role=r, init=n[0]) for n, r, q in testimonials)

    body = """
  <section class="hero">
    <div class="container">
      <div>
        <span class="hero__badge">⚡ Next-day CITB test slots available</span>
        <h1>Book Your <span>CITB Test</span><br>&amp; Get Your CSCS Card</h1>
        <p class="lead">Construction Helps makes it simple to book your CITB Health, Safety &amp; Environment test and
        apply for the right CSCS, Skill or JIB card &mdash; with friendly, expert support the whole way.</p>
        <div class="hero__actions">
          <a href="citb-test.html" class="btn btn-primary">Book Your CITB Test</a>
          <a href="cards.html" class="btn btn-outline" style="border-color:rgba(255,255,255,.35); color:#fff;">Explore CSCS Cards</a>
        </div>
        <div class="hero__stats">
          <div><strong>150+</strong><span>Approved Test Centres</span></div>
          <div><strong>6</strong><span>CSCS Card Types</span></div>
          <div><strong>24/7</strong><span>Online Booking</span></div>
        </div>
      </div>
      <div class="hero__media">
        <img src="images/Green-Labourer-(1)-(2).webp" alt="Construction worker on site">
        <div class="hero__float">
          <div class="dot">✔</div>
          <div><strong>Test Passed</strong><span>Green Card issued in 2 weeks</span></div>
        </div>
      </div>
    </div>
  </section>

  """ + trust_strip() + """

  <section class="section section--alt">
    <div class="container">
      <div class="section-head">
        <h2>How Can We Help?</h2>
      </div>
      <div class="help-buttons">
        <a href="citb-test.html">Which CITB Test<br>Do I Need?</a>
        <a href="test-centres.html">Test Centre<br>Locations</a>
        <a href="cards.html">CSCS Card<br>Application</a>
        <a href="faqs.html">Frequently Asked<br>Questions</a>
      </div>
      <p>Our simple booking system lets you book your CITB test &mdash; known by some as the CITB HS&amp;E test or
      touch-screen test &mdash; online, safely and securely. We offer free rescheduling, free retake options and
      cancellation date tracking, so you can get back on site as soon as possible. Our friendly team and easy-to-use
      website give you all the guidance you need to complete the right test and get the right CSCS card, or renew
      your CSCS card, as quickly as possible.</p>
      <p>When applying for CSCS cards we give you all the information you need to find out which card is right for
      you. Our friendly team will guide you through the process via email. You won&rsquo;t need to wait on the
      phone, just a simple online service. We also offer training to help you get your new CSCS card as quickly as
      possible such as the online <a href="green-card-online-course.html">Health, Safety and Awareness course</a>
      which allows you to get a CSCS Green Card. You can find more information
      <a href="green-card-online-course.html">about the course.</a> The price of a CSCS card is &pound;65 which
      includes the &pound;36 CSCS Card fee, application fee and VAT. The price of a CITB test is &pound;45 which
      includes the &pound;23.50 CITB exam fee, booking fee and VAT.</p>
    </div>
  </section>

  <section class="section" id="services">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">What We Do</span>
        <h2>Everything You Need, In One Place</h2>
        <p>From your first CITB test to a full CSCS, Skill or JIB card and ongoing e-learning, we support you at every stage.</p>
      </div>
      <div class="grid grid-3">{service_cards}</div>
    </div>
  </section>

  <section class="section section--alt" id="cards">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">CSCS Cards</span>
        <h2>Find The Right Card For Your Trade</h2>
        <p>Each CSCS card colour represents a different qualification level. Explore each card to see requirements, validity and how to apply.</p>
      </div>
      <div class="card-tiles">{tiles}</div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">How It Works</span>
        <h2>Three Simple Steps</h2>
        <p>We keep the process clear and stress-free, from choosing a card to receiving it in the post.</p>
      </div>
      <div class="steps">{steps_html}</div>
    </div>
  </section>

  <section class="section section--dark">
    <div class="container">
      <div class="info-block">
        <div class="info-block__media">
          <img src="images/engineers-helmets-standing-by-factory-resize.jpg" alt="Construction engineers on site">
        </div>
        <div class="info-block__text">
          <span class="eyebrow">Why Construction Helps</span>
          <h2>A Booking Partner You Can Rely On</h2>
          <p style="color:#c7cede;">We're an independent booking agent working across the UK construction industry, helping
          thousands of workers book CITB tests and apply for CSCS, Skill and JIB cards every year.</p>
          <ul class="check-list">
            <li><span class="tick">✓</span> Free rescheduling and cancellation date tracking</li>
            <li><span class="tick">✓</span> Guidance on exactly which card and test you need</li>
            <li><span class="tick">✓</span> Secure online payment and instant email confirmation</li>
            <li><span class="tick">✓</span> Friendly UK-based support team, no waiting on hold</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Testimonials</span>
        <h2>What Workers Say About Us</h2>
      </div>
      <div class="grid grid-3">{testimonials_html}</div>
    </div>
  </section>

  <section class="section--tight">""" + cta_band() + """</section>
"""
    body = body.format(service_cards=service_cards, tiles=tiles, steps_html=steps_html, testimonials_html=testimonials_html)
    return page(
        "Home",
        "Book your CITB test and apply for CSCS, Skill and JIB cards with Construction Helps — trusted UK booking support for construction workers.",
        body,
    )

def build_cards_hub():
    tiles = ""
    for c in CARDS:
        tiles += """<a href="{slug}.html" class="card-tile">
        <div class="card-tile__media"><img src="{img}" alt="{name}" loading="lazy"></div>
        <div class="card-tile__body">
          <div class="card-tile__strip" style="background:{hex}"></div>
          <h3>{name} &mdash; {short}</h3>
          <p>{tagline}</p>
        </div>
      </a>""".format(slug=c["slug"], img=c["tile_img"], name=c["name"], short=c["short"], hex=c["hex"], tagline=c["tagline"])

    rows = "".join("""<tr>
        <td><span class="ring" style="display:inline-flex;width:28px;height:28px;border-radius:50%;background:{hex};margin-right:10px;vertical-align:middle;"></span>{name}</td>
        <td>{short}</td>
        <td>{level}</td>
        <td>{validity}</td>
        <td><a href="{slug}.html" class="btn btn-sm btn-outline">Details</a></td>
      </tr>""".format(hex=c["hex"], name=c["name"], short=c["short"], level=c["level"], validity=c["validity"], slug=c["slug"]) for c in CARDS)

    body = breadcrumb(
        "CSCS Cards", theme="", eyebrow="Card Comparison",
        h1="CSCS Cards Explained",
        lead="Compare all six CSCS card colours to find the right one for your qualifications and experience.",
    ) + """
  <section class="section">
    <div class="container">
      <div class="card-tiles">{tiles}</div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">At A Glance</span>
        <h2>Compare Card Levels &amp; Validity</h2>
      </div>
      <div style="overflow-x:auto;">
        <table style="width:100%; border-collapse:collapse; background:#fff; border-radius:14px; overflow:hidden; box-shadow:var(--shadow);">
          <thead>
            <tr style="background:var(--dark); color:#fff; text-align:left;">
              <th style="padding:16px 20px;">Card</th>
              <th style="padding:16px 20px;">Also Known As</th>
              <th style="padding:16px 20px;">Level</th>
              <th style="padding:16px 20px;">Validity</th>
              <th style="padding:16px 20px;"></th>
            </tr>
          </thead>
          <tbody>{rows}</tbody>
        </table>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="grid grid-2" style="align-items:center;">
        <div>
          <span class="eyebrow">Not Sure Where To Start?</span>
          <h2>We'll Help You Pick The Right Card</h2>
          <p style="color:var(--gray-500);">Every trade and experience level maps to a different CSCS card. Give our team a
          call and we'll confirm the right card and test for your circumstances &mdash; free of charge.</p>
          <a href="contact.html" class="btn btn-primary">Speak To Our Team</a>
        </div>
        <div class="grid grid-2">
          <div class="fact"><strong>Skill Card</strong><span>Building services engineering</span></div>
          <div class="fact"><strong>JIB Card</strong><span>Electrical &amp; mechanical trades</span></div>
        </div>
      </div>
    </div>
  </section>

  <section class="section--tight">""" + cta_band() + """</section>
"""
    body = body.format(tiles=tiles, rows=rows)

    return page(
        "CSCS Cards",
        "Compare all CSCS card colours — Green, Blue, Gold, Red, White and Black — and find out which one matches your trade and qualifications.",
        body,
    )

def build_card_page(c):
    theme = c["theme"]
    subtypes_html = ""
    if c["subtypes"]:
        cards = "".join("""<div class="subtype-card">
          <img src="{img}" alt="{name}" loading="lazy">
          <div class="subtype-card__body"><h4>{name}</h4><p>{desc}</p></div>
        </div>""".format(img=s["img"], name=s["name"], desc=s["desc"]) for s in c["subtypes"])
        subtypes_html = """<section class="section section--alt">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Card Types</span>
        <h2>{name} Sub-Types</h2>
        <p>The {name} covers a few different situations &mdash; here's how to tell them apart.</p>
      </div>
      <div class="subtype-grid">{cards}</div>
    </div>
  </section>""".format(name=c["name"], cards=cards)

    who_html = "".join('<li><span class="tick">✓</span>{item}</li>'.format(item=w) for w in c["who"])
    req_html = "".join('<li><span class="tick">✓</span>{item}</li>'.format(item=r) for r in c["requirements"])
    intro_html = "".join("<p>{p}</p>".format(p=p) for p in c["intro"])

    body = breadcrumb(
        c["name"], theme=theme, eyebrow="CSCS " + c["short"],
        h1="CSCS " + c["name"],
        lead=c["tagline"],
    ) + """
  <section class="section">
    <div class="container">
      <div class="info-block">
        <div class="info-block__media card-media">
          <img src="{hero_img}" alt="{name}">
        </div>
        <div class="info-block__text">
          <span class="eyebrow">About This Card</span>
          <h2>What Is The {name}?</h2>
          {intro_html}
          <div class="fact-row" style="grid-template-columns:repeat(3,1fr);">
            <div class="fact"><strong>{level}</strong><span>Level</span></div>
            <div class="fact"><strong>{validity}</strong><span>Validity</span></div>
            <div class="fact"><strong>{test}</strong><span>Test Required</span></div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container">
      <div class="info-block reverse">
        <div class="info-block__media card-media">
          <img src="{tile_img}" alt="{name} example">
        </div>
        <div class="info-block__text">
          <span class="eyebrow">Who It's For</span>
          <h2>Is This The Right Card For You?</h2>
          <ul class="check-list">{who_html}</ul>
        </div>
      </div>
    </div>
  </section>

  {subtypes_html}

  <section class="section">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Requirements</span>
        <h2>What You'll Need To Apply</h2>
      </div>
      <div class="grid grid-2" style="align-items:flex-start;">
        <div class="info-block__text">
          <ul class="check-list">{req_html}</ul>
        </div>
        <div class="steps" style="grid-template-columns:1fr; gap:18px;">
          <div class="step"><h3>Book Your CITB Test</h3><p>We'll book your Health, Safety &amp; Environment test at your nearest approved centre.</p></div>
          <div class="step"><h3>Pass Your Test</h3><p>Sit the multiple-choice touch-screen test &mdash; 45 out of 50 correct is a pass.</p></div>
          <div class="step"><h3>Call Us &amp; Relax</h3><p>Just call us on 0203 400 8738 and we'll take care of the rest of your {name} application.</p></div>
        </div>
      </div>
    </div>
  </section>

  """ + other_cards_strip(exclude_slug=c["slug"]) + """

  <section class="section--tight">""" + cta_band(
        heading="Ready To Apply For Your {name}?".format(name=c["name"]),
        text="Just call us on 0203 400 8738 and we'll take care of the rest of your {name} application.".format(name=c["name"]),
    ) + """</section>
"""
    body = body.format(
        hero_img=c["hero_img"], tile_img=c["tile_img"], name=c["name"], intro_html=intro_html,
        level=c["level"], validity=c["validity"], test=c["test"], who_html=who_html,
        subtypes_html=subtypes_html, req_html=req_html,
    )

    return page(
        "CSCS " + c["name"],
        "Everything you need to know about the CSCS {name} ({short}): requirements, validity and how to apply with Construction Helps.".format(name=c["name"], short=c["short"]),
        body,
    )

def build_skill_card():
    body = breadcrumb(
        "Skill Card", theme="", eyebrow="Building Services",
        h1="Skill Card Applications",
        lead="The card scheme for the building services engineering sector, covering mechanical, electrical and heating trades.",
    ) + """
  <section class="section">
    <div class="container">
      <div class="info-block">
        <div class="info-block__media card-media">
          <img src="images/rounded_skillcard_resized.jpeg" alt="Skill Card">
        </div>
        <div class="info-block__text">
          <span class="eyebrow">About The Skill Card</span>
          <h2>What Is A Skill Card?</h2>
          <p>The Skill Card is issued to operatives working in building services engineering &mdash; including heating,
          ventilation, air conditioning, refrigeration and plumbing &mdash; and is recognised alongside CSCS on many
          UK construction sites.</p>
          <p>Like CSCS, Skill Cards are colour-coded by qualification level, and holders must pass a CITB-recognised
          Health, Safety &amp; Environment test before applying.</p>
          <div class="fact-row" style="grid-template-columns:repeat(3,1fr);">
            <div class="fact"><strong>Building Services</strong><span>Sector</span></div>
            <div class="fact"><strong>5 years</strong><span>Typical Validity</span></div>
            <div class="fact"><strong>CITB HS&amp;E</strong><span>Test Required</span></div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Who Needs One</span>
        <h2>Is A Skill Card Right For You?</h2>
      </div>
      <div class="grid grid-3">
        <div class="service-card"><div class="service-card__icon">🔧</div><h3>Heating Engineers</h3><p>Gas, oil and renewable heating installers and service engineers.</p></div>
        <div class="service-card"><div class="service-card__icon">❄️</div><h3>Refrigeration &amp; AC</h3><p>Air conditioning and refrigeration engineers, including ACRIB-registered technicians.</p></div>
        <div class="service-card"><div class="service-card__icon">🚰</div><h3>Plumbers</h3><p>Plumbing and heating operatives working across domestic and commercial sites.</p></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Applying</span>
        <h2>How To Get Your Skill Card</h2>
      </div>
      <div class="steps">
        <div class="step"><h3>Confirm Eligibility</h3><p>We check your trade qualification against the correct Skill Card category.</p></div>
        <div class="step"><h3>Book Your Test</h3><p>We arrange your CITB Health, Safety &amp; Environment test at a nearby centre.</p></div>
        <div class="step"><h3>Call Us &amp; Relax</h3><p>Just call us on 0203 400 8738 and we'll take care of the rest — paperwork, tracking and delivery.</p></div>
      </div>
    </div>
  </section>

  <section class="section--tight">""" + cta_band(
        heading="Ready To Apply For Your Skill Card?",
        text="Just call us on 0203 400 8738 and our team will take care of the rest.",
    ) + """</section>
"""
    return page(
        "Skill Card",
        "Apply for a Skill Card for the building services engineering sector — heating, refrigeration, air conditioning and plumbing — with Construction Helps.",
        body,
    )

def build_jib_card():
    body = breadcrumb(
        "JIB Card", theme="", eyebrow="Electrical &amp; Mechanical",
        h1="JIB Card Applications",
        lead="Joint Industry Board cards for electrotechnical and mechanical engineering professionals across the UK.",
    ) + """
  <section class="section">
    <div class="container">
      <div class="info-block">
        <div class="info-block__media">
          <img src="images/engineers-helmets-standing-by-factory-resize.jpg" alt="JIB card engineer">
        </div>
        <div class="info-block__text">
          <span class="eyebrow">About The JIB Card</span>
          <h2>What Is A JIB Card?</h2>
          <p>The JIB (Joint Industry Board) card &mdash; often issued through the Electrotechnical Certification Scheme (ECS)
          or JIB-PMES for mechanical engineering services &mdash; proves that the holder has the right qualifications,
          training and identity checks to work as an electrical or mechanical engineer on site.</p>
          <p>Like CSCS cards, JIB cards are colour-coded to reflect the holder's grade, from apprentice through to
          approved electrician or engineering manager.</p>
          <div class="fact-row" style="grid-template-columns:repeat(3,1fr);">
            <div class="fact"><strong>Electrical / Mechanical</strong><span>Sector</span></div>
            <div class="fact"><strong>3 years</strong><span>Typical Validity</span></div>
            <div class="fact"><strong>AM2 / NVQ</strong><span>Common Requirement</span></div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Card Grades</span>
        <h2>Common JIB Card Categories</h2>
      </div>
      <div class="grid grid-4">
        <div class="service-card"><div class="service-card__icon">🎓</div><h3>Apprentice</h3><p>For those enrolled on a recognised electrical or mechanical apprenticeship.</p></div>
        <div class="service-card"><div class="service-card__icon">⚙️</div><h3>Electrician / Engineer</h3><p>For fully qualified electricians and mechanical engineering technicians.</p></div>
        <div class="service-card"><div class="service-card__icon">🛠️</div><h3>Approved Electrician</h3><p>For experienced electricians who meet the JIB's approved grading criteria.</p></div>
        <div class="service-card"><div class="service-card__icon">👷</div><h3>Technician / Manager</h3><p>For senior engineering technicians and engineering managers.</p></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Applying</span>
        <h2>How To Get Your JIB Card</h2>
      </div>
      <div class="steps">
        <div class="step"><h3>Confirm Your Grade</h3><p>We match your qualifications and experience to the correct JIB card category.</p></div>
        <div class="step"><h3>Book Any Required Test</h3><p>We arrange any health &amp; safety or trade assessment your grade requires.</p></div>
        <div class="step"><h3>Call Us &amp; Relax</h3><p>Just call us on 0203 400 8738 and we'll take care of the rest of your JIB card application.</p></div>
      </div>
    </div>
  </section>

  <section class="section--tight">""" + cta_band(
        heading="Ready To Apply For Your JIB Card?",
        text="Just call us on 0203 400 8738 and our team will take care of the rest.",
    ) + """</section>
"""
    return page(
        "JIB Card",
        "Apply for a JIB (Joint Industry Board) card for electrical and mechanical engineering professionals with Construction Helps.",
        body,
    )

def build_ecs_card():
    why = [
        ("Proof Of Competency", "Recognised certification in the electrotechnical industry."),
        ("Ensures Safety", "Demonstrates knowledge of health and safety regulations."),
        ("Verification Of Qualifications", "Confirms industry-recognised skills and training."),
        ("Access To Job Sites", "Many employers and sites require ECS certification before granting access."),
    ]
    why_html = "".join("""<div class="service-card"><div class="service-card__icon">✓</div><h3>{t}</h3><p>{d}</p></div>""".format(t=t, d=d) for t, d in why)

    subtypes = [
        ("Apprentices &amp; Trainees", "images/ecs-trainee-stage.jpg", "For those undergoing training or apprenticeships in the electrotechnical industry."),
        ("Electrical Management", "images/building_controls.webp", "For professionals working with automated building and electrical management systems."),
        ("Fire, Emergency &amp; Security Systems (FESS)", "images/FESS-Labourer.jpg", "Covers roles related to fire alarms, security systems and emergency installations."),
    ]
    subtypes_html = "".join("""<div class="subtype-card">
          <img src="{img}" alt="{name}" loading="lazy">
          <div class="subtype-card__body"><h4>{name}</h4><p>{desc}</p></div>
        </div>""".format(img=img, name=name, desc=desc) for name, img, desc in subtypes)

    body = breadcrumb(
        "ECS Card", theme="red", eyebrow="Electrotechnical Certification Scheme",
        h1="ECS Card Applications",
        lead="The official certification system for electrotechnical workers in the UK, verifying qualifications, experience and on-site competency.",
    ) + """
  <section class="section">
    <div class="container">
      <div class="info-block">
        <div class="info-block__media card-media">
          <img src="images/ecs-trainee-stage.jpg" alt="ECS Card electrotechnical worker">
        </div>
        <div class="info-block__text">
          <span class="eyebrow">About The ECS Card</span>
          <h2>What Is An ECS Card?</h2>
          <p>The Electrotechnical Certification Scheme (ECS) is the official certification system for electrotechnical
          workers in the UK. It verifies qualifications, experience and competency in various electrical-related roles.</p>
          <p>Holding an ECS card proves your skills, identity and adherence to industry standards, and is widely
          recognised and requested across UK construction and building services sites.</p>
          <div class="fact-row" style="grid-template-columns:repeat(3,1fr);">
            <div class="fact"><strong>Electrotechnical</strong><span>Sector</span></div>
            <div class="fact"><strong>3 years</strong><span>Typical Validity</span></div>
            <div class="fact"><strong>ECS H&amp;S Test</strong><span>Assessment Required</span></div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Why It Matters</span>
        <h2>Why You Need An ECS Card</h2>
      </div>
      <div class="grid grid-4">{why_html}</div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Card Categories</span>
        <h2>Choose The Right ECS Card</h2>
        <p>Decide which ECS card category matches your occupation and level of training.</p>
      </div>
      <div class="subtype-grid">{subtypes_html}</div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Applying</span>
        <h2>How To Apply For An ECS Card</h2>
      </div>
      <div class="steps">
        <div class="step"><h3>Create A MyECS Account</h3><p>Register and submit an online application through the official ECS system.</p></div>
        <div class="step"><h3>Meet Qualification Requirements</h3><p>We check the specific requirements for your ECS card category.</p></div>
        <div class="step"><h3>Pass The Health &amp; Safety Assessment</h3><p>Complete the ECS Health, Safety &amp; Environmental test.</p></div>
      </div>
      <div class="text-center" style="margin-top:28px;">
        <a href="tel:02034008738" class="btn btn-primary">Call Us &amp; Relax</a>
        <p style="margin-top:14px; color:var(--gray-500); font-size:14.5px;">Prefer we handle it for you? Just call us on 0203 400 8738 and we'll take care of the rest.</p>
      </div>
    </div>
  </section>

  <section class="section--tight">""" + cta_band(
        heading="Ready To Apply For Your ECS Card?",
        text="Just call us on 0203 400 8738 and our team will take care of the rest.",
    ) + """</section>
"""
    body = body.format(why_html=why_html, subtypes_html=subtypes_html)
    return page(
        "ECS Card",
        "Apply for an ECS (Electrotechnical Certification Scheme) card covering Apprentices & Trainees, Electrical Management and FESS categories with Construction Helps.",
        body,
    )

def build_cpcs_card():
    types = [
        {
            "name": "CPCS Red Trained Operator Card",
            "img": "images/trained-operator-card.webp",
            "desc": "Issued on successful completion of the CPCS Theory and Practical Technical Tests, which must be "
                    "taken at a CPCS-accredited test centre.",
            "steps": [
                "Pass the relevant CITB Health, Safety &amp; Environment test",
                "Achieve the CPCS theory test (within two years of the CITB test)",
                "Achieve the CPCS practical test (within six months of the CPCS theory test)",
            ],
        },
        {
            "name": "CPCS Blue Competent Operator Card",
            "img": "images/competent-operator-card.webp",
            "desc": "Confirms you have demonstrated health, safety and environment awareness through the CITB test, "
                    "underpinning knowledge through a CPCS theory test, operating ability through a CPCS practical "
                    "test, and operating competence evidenced by a vocational qualification (VQ). Valid for five "
                    "years and renewable — holders can work unsupervised and may supervise Red Trained Operators.",
            "steps": [
                "Provide proof of achievement of the VQ/NVQ for the category",
                "Pass the relevant CITB Health, Safety &amp; Environment test",
                "Achieve the CPCS theory test (within two years of the CITB test)",
                "Achieve the CPCS practical test (within six months of the CPCS theory test)",
            ],
        },
        {
            "name": "CPCS Tester Card",
            "img": "images/tester-card.webp",
            "desc": "For experienced operators who are trained and assessed to independently and impartially deliver "
                    "learning or judge a learner's skills and knowledge, evidenced through a Record of Category "
                    "Experience (RoE).",
            "steps": [
                "Hold a valid, in-date first aid certificate",
                "Pass the Managers &amp; Professionals (MAP) CITB test",
                "Achieve the CPCS Advanced Theory Test",
                "Achieve the CPCS Advanced Practical Test",
                "Hold a recognised Health &amp; Safety qualification (e.g. NEBOSH Construction Certificate, SMSTS or IOSH Managing Safely)",
            ],
        },
    ]

    blocks = ""
    for i, t in enumerate(types):
        reverse = " reverse" if i % 2 == 1 else ""
        steps_html = "".join('<li><span class="tick">✓</span>{s}</li>'.format(s=s) for s in t["steps"])
        blocks += """<div class="info-block{reverse}" style="margin-bottom:56px;">
        <div class="info-block__media card-media">
          <img src="{img}" alt="{name}">
        </div>
        <div class="info-block__text">
          <h2>{name}</h2>
          <p>{desc}</p>
          <ul class="check-list">{steps_html}</ul>
        </div>
      </div>""".format(reverse=reverse, img=t["img"], name=t["name"], desc=t["desc"], steps_html=steps_html)

    body = breadcrumb(
        "CPCS Card", theme="blue", eyebrow="Construction Plant Competence Scheme",
        h1="CPCS Card Applications",
        lead="The industry-recognised card scheme for plant operators, confirming the skills and experience to safely operate construction plant machinery.",
    ) + """
  <section class="section">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">About CPCS</span>
        <h2>What Is A CPCS Card?</h2>
        <p>The Construction Plant Competence Scheme (CPCS) verifies that plant operators have the skills, knowledge
        and experience to safely operate specific categories of construction plant. There are three main card types,
        each reflecting a different stage of training and experience.</p>
      </div>
      {blocks}
    </div>
  </section>

  <section class="section section--alt">
    <div class="container">
      <div class="info-block">
        <div class="info-block__text">
          <span class="eyebrow">Renewals</span>
          <h2>How To Book Your CPCS Renewal Test</h2>
          <p>To renew your CPCS Blue Competent Operator card, you must take and pass the CPCS Renewal Test. This
          confirms your knowledge of each plant category, or group of categories, held on your card is up to date.</p>
          <p>Each test takes around 15 minutes, and you'll need to take a renewal test for every group of categories
          on your card. Booking your CPCS renewal through us is easy &mdash; just call our team and we'll take care of the rest.</p>
          <a href="tel:{phone1_tel}" class="btn btn-primary">Call {phone1} To Renew</a>
        </div>
        <div class="info-block__media">
          <img src="images/engineers-helmets-standing-by-factory-resize.jpg" alt="CPCS plant operator on site">
        </div>
      </div>
    </div>
  </section>

  <section class="section--tight">""" + cta_band(
        heading="Ready To Apply For Your CPCS Card?",
        text="Just call us on 0203 400 8738 and our team will take care of the rest.",
    ) + """</section>
"""
    body = body.format(blocks=blocks, phone1_tel=SITE["phone1_tel"], phone1=SITE["phone1"])
    return page(
        "CPCS Card",
        "Apply for a CPCS (Construction Plant Competence Scheme) card — Red Trained Operator, Blue Competent Operator or Tester — with Construction Helps.",
        body,
    )

def build_citb_test():
    locations = ["London", "Birmingham", "Manchester", "Liverpool", "Leeds", "Glasgow", "Bristol", "Sheffield",
                 "Edinburgh", "Cardiff", "Newcastle upon Tyne", "Nottingham", "Southampton", "Belfast", "Coventry"]
    loc_html = "".join('<span class="fact" style="padding:10px 16px;">{l}</span>'.format(l=l) for l in locations)

    body = breadcrumb(
        "CITB Test", theme="", eyebrow="Health, Safety &amp; Environment Test",
        h1="Book Your CITB Test",
        lead="Book your CITB Health, Safety &amp; Environment test (the touch-screen test) online, safely and securely, at over 150 approved centres nationwide.",
    ) + """
  <section class="section--tight">
    <div class="container">""" + citb_subnav("citb-test.html") + """</div>
  </section>
  <section class="section">
    <div class="container">
      <div class="info-block">
        <div class="info-block__media">
          <img src="images/front-view-constructor-with-schematic-resize-2.jpeg" alt="CITB test candidate">
        </div>
        <div class="info-block__text">
          <span class="eyebrow">About The Test</span>
          <h2>What Is The CITB Test?</h2>
          <p>The CITB Health, Safety &amp; Environment (HS&amp;E) test, sometimes called the touch-screen test, is a
          multiple-choice exam that every applicant must pass before they can apply for a CSCS, Skill or JIB card.</p>
          <p>The test takes around 45 minutes and covers 50 questions on general health and safety topics, plus a
          behavioural case study section. You need 45 out of 50 correct to pass.</p>
          <div class="fact-row">
            <div class="fact"><strong>45 min</strong><span>Duration</span></div>
            <div class="fact"><strong>50</strong><span>Questions</span></div>
            <div class="fact"><strong>45/50</strong><span>Pass Mark</span></div>
            <div class="fact"><strong>150+</strong><span>Test Centres</span></div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Booking</span>
        <h2>Book In 3 Simple Steps</h2>
      </div>
      <div class="steps">
        <div class="step"><h3>Fill In Your Details</h3><p>Tell us your preferred test centre and choose an available date and time.</p></div>
        <div class="step"><h3>Make Payment Securely</h3><p>Pay online safely by card &mdash; your booking is confirmed instantly.</p></div>
        <div class="step"><h3>Receive Confirmation</h3><p>Get an email confirming your test date, time and location, ready to attend.</p></div>
      </div>
      <div class="text-center" style="margin-top:36px;">
        <a href="tel:02034008738" class="btn btn-primary">Call Us &amp; Relax</a>
        <p style="margin-top:14px; color:var(--gray-500); font-size:14.5px;">Prefer not to fill in a form? Just call us on 0203 400 8738 and we'll take care of the rest.</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Test Centres</span>
        <h2>Available In All Major UK Cities</h2>
        <p>There are over 150 CITB approved test centres nationwide &mdash; here are just a few of the locations we cover.</p>
      </div>
      <div style="display:flex; flex-wrap:wrap; gap:12px; justify-content:center;">{loc_html}</div>
      <div class="text-center" style="margin-top:28px;">
        <a href="test-centres.html" class="btn btn-primary">Find Your Nearest Test Centre &rarr;</a>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">FAQs</span>
        <h2>CITB Test Questions</h2>
      </div>
      <div style="max-width:760px; margin:0 auto;">
        <div class="faq-item open">
          <button class="faq-q"><span>Do I need to pass the CITB test before applying for a CSCS card?</span><span class="plus">+</span></button>
          <div class="faq-a"><p>Yes. You must pass the relevant CITB Health, Safety &amp; Environment test before your CSCS, Skill or JIB card application can be approved.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-q"><span>Can I reschedule my CITB test?</span><span class="plus">+</span></button>
          <div class="faq-a"><p>Yes, we offer free rescheduling subject to availability at your chosen test centre, along with cancellation date tracking.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-q"><span>What happens if I don't pass?</span><span class="plus">+</span></button>
          <div class="faq-a"><p>We offer free retake options to help you get the result you need as quickly as possible.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-q"><span>How much does the CITB test cost?</span><span class="plus">+</span></button>
          <div class="faq-a"><p>Pricing includes the exam fee, booking fee and VAT. Just call us on 0203 400 8738 and our team will take care of the rest — latest pricing and availability at your chosen centre.</p></div>
        </div>
      </div>
    </div>
  </section>

  <section class="section--tight">""" + cta_band() + """</section>
"""
    body = body.format(loc_html=loc_html)
    return page(
        "Book Your CITB Test",
        "Book your CITB Health, Safety & Environment test online at over 150 approved UK test centres with Construction Helps.",
        body,
    )

def build_test_centres():
    body = breadcrumb(
        "Find A Test Centre", theme="", eyebrow="150+ UK Locations",
        h1="Find A CITB Test Centre Near You",
        lead="Over 150 approved locations across the UK. Enter your postcode below and we'll find your nearest CITB test centre in seconds.",
    ) + """
  <div class="container">
    <div class="centre-search">
      <form id="centre-search-form">
        <div class="centre-search__row">
          <div class="centre-search__field">
            <label for="centre-postcode">Your Postcode</label>
            <input type="text" id="centre-postcode" name="postcode" placeholder="e.g. SW1A 1AA" autocomplete="postal-code" required>
          </div>
          <div class="centre-search__actions">
            <button type="submit" id="centre-search-btn" class="btn btn-primary">Find My Nearest Centre</button>
            <button type="button" id="centre-geo-btn" class="btn btn-outline">Use My Location</button>
          </div>
        </div>
        <p class="centre-search__hint">We use your postcode only to calculate distance to our nearest approved centres &mdash; it isn't stored.</p>
      </form>
    </div>
  </div>

  <section class="section" id="centre-results-wrap">
    <div class="container">
      <div id="centre-results-summary"></div>
      <div id="centre-results"></div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Browse All Locations</span>
        <h2>150+ Approved Test Centres By Region</h2>
        <p>Can't find your town, or prefer to book by phone? Just call us on 0203 400 8738 and our team will take care of the rest.</p>
      </div>
      <div id="centre-regions"></div>
    </div>
  </section>

  <section class="section--tight">""" + cta_band(
        heading="Ready To Book Your CITB Test?",
        text="Just call us on 0203 400 8738 and our team will take care of the rest.",
    ) + """</section>

  <script src="assets/js/test-centres.js"></script>
"""
    return page(
        "Find A Test Centre",
        "Find your nearest CITB test centre by postcode. Search over 150 approved locations across the UK with Construction Helps.",
        body,
    )

def citb_subnav(current):
    items = [
        ("citb-test.html", "Book CITB Test"),
        ("which-citb-test.html", "Which Test Do I Need?"),
        ("test-centres.html", "Test Centres"),
        ("group-test-booking.html", "Group Test Booking"),
        ("citb-revision.html", "Revision Material"),
        ("citb-mock-tests.html", "Mock Tests"),
    ]
    links = "".join(
        '<a href="{slug}"{active}>{label}</a>'.format(
            slug=slug, label=label, active=' class="active"' if slug == current else ""
        ) for slug, label in items
    )
    return '<nav class="legal-nav">{links}</nav>'.format(links=links)

def build_which_test():
    types = [
        ("Operatives Test", "For general operatives, labourers and tradespeople working towards a Green, Red, Blue or Gold CSCS card.", "citb-operatives-mock-test.html"),
        ("Supervisors Test", "For site supervisors and team leaders working towards a Gold Card supervisory role.", "citb-supervisors-mock-test.html"),
        ("Managers &amp; Professionals Test", "For managers, directors and professionally qualified staff working towards a Black or White Card.", "citb-mock-tests.html"),
    ]
    cards_html = "".join("""<div class="service-card">
        <div class="service-card__icon">📝</div>
        <h3>{name}</h3>
        <p>{desc}</p>
        <a href="{link}" class="link-arrow">Practice this test &rarr;</a>
      </div>""".format(name=n, desc=d, link=l) for n, d, l in types)

    body = breadcrumb(
        "Which Test Do I Need?", theme="", eyebrow="CITB Tests Explained",
        h1="Which CITB Test Do I Need?",
        lead="CITB runs a few different Health, Safety &amp; Environment tests, depending on your role. Here's how to pick the right one.",
    ) + """
  <section class="section--tight">
    <div class="container">""" + citb_subnav("which-citb-test.html") + """</div>
  </section>
  <section class="section">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Three Test Types</span>
        <h2>Match Your Test To Your Role</h2>
        <p>Not sure which one applies to you? Just call us on 0203 400 8738 and our team will take care of the rest.</p>
      </div>
      <div class="grid grid-3">{cards_html}</div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Still Unsure?</span>
        <h2>We'll Confirm It For You, Free</h2>
        <p>Tell us your trade, your experience and which CSCS, Skill or JIB card you're working towards, and we'll
        confirm exactly which CITB test to book &mdash; no guesswork required.</p>
      </div>
      <div class="text-center">
        <a href="citb-test.html" class="btn btn-primary">Book Your CITB Test</a>
      </div>
    </div>
  </section>

  <section class="section--tight">""" + cta_band() + """</section>
"""
    body = body.format(cards_html=cards_html)
    return page(
        "Which CITB Test Do I Need?",
        "Not sure which CITB Health, Safety & Environment test to book? Compare the Operatives, Supervisors and Managers & Professionals tests.",
        body,
    )

def build_group_booking():
    body = breadcrumb(
        "Group Test Booking", theme="", eyebrow="For Employers &amp; Teams",
        h1="Group CITB Test Booking",
        lead="Booking CITB tests for a team or workforce? We'll coordinate multiple bookings at the same test centre, on the same day.",
    ) + """
  <section class="section--tight">
    <div class="container">""" + citb_subnav("group-test-booking.html") + """</div>
  </section>
  <section class="section">
    <div class="container">
      <div class="info-block">
        <div class="info-block__text">
          <span class="eyebrow">Why Book As A Group</span>
          <h2>One Call, The Whole Team Sorted</h2>
          <p>If you're a contractor, agency or employer needing to book CITB tests for several workers at once, our
          group booking service saves you time. We coordinate test dates, times and centres so your whole team can
          test together wherever possible.</p>
          <ul class="check-list">
            <li><span class="tick">✓</span>One point of contact for your whole team's bookings</li>
            <li><span class="tick">✓</span>Coordinated dates and test centres, where availability allows</li>
            <li><span class="tick">✓</span>A single invoice for group bookings</li>
            <li><span class="tick">✓</span>Free rescheduling if a team member's plans change</li>
          </ul>
        </div>
        <div class="info-block__media">
          <img src="images/engineers-helmets-standing-by-factory-resize.jpg" alt="Construction team on site">
        </div>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">How It Works</span>
        <h2>Booking For Your Team</h2>
      </div>
      <div class="steps">
        <div class="step"><h3>Send Us Your List</h3><p>Give us the names and preferred test type for each team member.</p></div>
        <div class="step"><h3>We Coordinate Dates</h3><p>We find a test centre and dates that work for the group.</p></div>
        <div class="step"><h3>Call Us &amp; Relax</h3><p>Just call us on 0203 400 8738 and we'll take care of the rest.</p></div>
      </div>
    </div>
  </section>

  <section class="section--tight">""" + cta_band(
        heading="Ready To Book For Your Team?",
        text="Just call us on 0203 400 8738 and our team will take care of the rest.",
    ) + """</section>
"""
    return page(
        "Group CITB Test Booking",
        "Book CITB Health, Safety & Environment tests for a team or workforce with Construction Helps' group booking service.",
        body,
    )

def build_revision():
    topics = [
        ("General Responsibilities", "Your legal duties, reporting hazards and who is responsible for safety on site."),
        ("Accidents &amp; First Aid", "Reporting accidents, near misses and where to find first aid on site."),
        ("Health &amp; Welfare", "Site welfare facilities, noise, manual handling and occupational health."),
        ("PPE", "Selecting, wearing and maintaining personal protective equipment correctly."),
        ("Fire Prevention", "Fire risks, extinguisher types and evacuation procedures."),
        ("Working At Height", "Ladders, scaffolding, harnesses and fall prevention basics."),
    ]
    topics_html = "".join("""<div class="service-card"><div class="service-card__icon">📘</div><h3>{t}</h3><p>{d}</p></div>""".format(t=t, d=d) for t, d in topics)

    body = breadcrumb(
        "Revision Material", theme="", eyebrow="Get Test-Ready",
        h1="CITB Test Revision Material",
        lead="Brush up on the key topics before your CITB Health, Safety &amp; Environment test, so you pass first time.",
    ) + """
  <section class="section--tight">
    <div class="container">""" + citb_subnav("citb-revision.html") + """</div>
  </section>
  <section class="section">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Key Topics</span>
        <h2>What The CITB Test Covers</h2>
        <p>The CITB test draws its questions from a fixed set of topics. Here are the areas most candidates need to revise.</p>
      </div>
      <div class="grid grid-3">{topics_html}</div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Practice</span>
        <h2>Try Our Mock Tests</h2>
        <p>Once you've revised the topics, work through our mock tests to check you're ready.</p>
      </div>
      <div class="text-center">
        <a href="citb-mock-tests.html" class="btn btn-primary">View CITB Mock Tests</a>
      </div>
    </div>
  </section>

  <section class="section--tight">""" + cta_band() + """</section>
"""
    body = body.format(topics_html=topics_html)
    return page(
        "CITB Test Revision Material",
        "Revise the key topics covered in the CITB Health, Safety & Environment test before you book with Construction Helps.",
        body,
    )

def build_mock_tests_hub():
    cards_html = "".join("""<div class="service-card">
        <div class="service-card__icon">✅</div>
        <h3>{name}</h3>
        <p>{audience}</p>
        <a href="{slug}.html" class="link-arrow">Learn more &rarr;</a>
      </div>""".format(name=m["name"], audience=m["audience"], slug=m["slug"]) for m in MOCK_TESTS)

    body = breadcrumb(
        "CITB Mock Tests", theme="", eyebrow="Practice Before You Book",
        h1="CITB Mock Tests",
        lead="Get familiar with the format and topics before your real CITB Health, Safety &amp; Environment test.",
    ) + """
  <section class="section--tight">
    <div class="container">""" + citb_subnav("citb-mock-tests.html") + """</div>
  </section>
  <section class="section">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Choose A Mock Test</span>
        <h2>Practice The Test That Matches Your Role</h2>
      </div>
      <div class="grid grid-3">{cards_html}</div>
    </div>
  </section>

  <section class="section--tight">""" + cta_band(
        heading="Ready For The Real Thing?",
        text="Just call us on 0203 400 8738 and our team will take care of the rest.",
    ) + """</section>
"""
    body = body.format(cards_html=cards_html)
    return page(
        "CITB Mock Tests",
        "Practice CITB mock tests covering Operatives, Supervisors, Working at Heights, Fire Extinguishers and Safety Signs.",
        body,
    )

def build_mock_test_page(m):
    others = [o for o in MOCK_TESTS if o["slug"] != m["slug"]]
    topics_html = "".join('<li><span class="tick">✓</span>{t}</li>'.format(t=t) for t in m["topics"])
    others_html = "".join("""<a href="{slug}.html" class="other-card">
      <span class="ring" style="border-color:#0d78f2; color:#0d78f2;">✓</span>
      <span>{name}</span>
    </a>""".format(slug=o["slug"], name=o["name"]) for o in others)

    body = breadcrumb(
        m["name"], theme="", eyebrow="CITB Mock Test",
        h1=m["name"],
        lead=m["covers"],
    ) + """
  <section class="section--tight">
    <div class="container">""" + citb_subnav("citb-mock-tests.html") + """</div>
  </section>
  <section class="section">
    <div class="container">
      <div class="info-block">
        <div class="info-block__text">
          <span class="eyebrow">Who It's For</span>
          <h2>Is This Mock Test For You?</h2>
          <p>{audience}.</p>
          <span class="eyebrow" style="margin-top:24px;">What It Covers</span>
          <ul class="check-list">{topics_html}</ul>
        </div>
        <div class="info-block__media">
          <img src="images/front-view-constructor-with-schematic-resize-2.jpeg" alt="{name} preparation">
        </div>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Other Mock Tests</span>
        <h2>Practice Another Topic</h2>
      </div>
      <div class="other-cards">{others_html}</div>
    </div>
  </section>

  <section class="section--tight">""" + cta_band(
        heading="Ready To Book Your Real CITB Test?",
        text="Just call us on 0203 400 8738 and our team will take care of the rest.",
    ) + """</section>
"""
    body = body.format(audience=m["audience"], topics_html=topics_html, name=m["name"], others_html=others_html)
    return page(
        m["name"],
        "Practice the {name} to prepare for your official CITB Health, Safety & Environment test.".format(name=m["name"]),
        body,
    )

def build_green_card_course():
    topics = [
        "General responsibilities on a construction site",
        "Health, safety and welfare basics",
        "Personal protective equipment (PPE)",
        "Manual handling awareness",
        "Fire prevention and emergency procedures",
        "Common site hazards and how to avoid them",
    ]
    topics_html = "".join('<li><span class="tick">✓</span>{t}</li>'.format(t=t) for t in topics)

    body = breadcrumb(
        "Green Card Course", theme="green", eyebrow="Online Training",
        h1="Health, Safety &amp; Awareness Course",
        lead="Complete the course that leads to your CSCS Green Card &mdash; online, at your own pace.",
    ) + """
  <section class="section">
    <div class="container">
      <div class="info-block">
        <div class="info-block__media">
          <img src="images/AdobeStock_1516393189-(1).jpeg" alt="Health, Safety and Awareness course">
        </div>
        <div class="info-block__text">
          <span class="eyebrow">About The Course</span>
          <h2>What Is The Health, Safety &amp; Awareness Course?</h2>
          <p>The Health, Safety &amp; Awareness course is the recognised online training route to a CSCS Green
          Card. It's designed for anyone new to construction who doesn't yet hold an NVQ, covering the core health
          and safety knowledge you need before working on site.</p>
          <p>The course is completed entirely online, so you can work through it at your own pace and don't need to
          take a day off work. You'll receive a certificate as soon as you finish, which you can then use to apply
          for your CSCS Green Card.</p>
          <div class="fact-row" style="grid-template-columns:repeat(3,1fr);">
            <div class="fact"><strong>Online</strong><span>Format</span></div>
            <div class="fact"><strong>Self-Paced</strong><span>Study Time</span></div>
            <div class="fact"><strong>Instant</strong><span>Certificate</span></div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container">
      <div class="info-block reverse">
        <div class="info-block__media">
          <img src="images/11-Green-MateAssistant.png" alt="CSCS Green Card">
        </div>
        <div class="info-block__text">
          <span class="eyebrow">What You'll Learn</span>
          <h2>Course Topics</h2>
          <ul class="check-list">{topics_html}</ul>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">How It Works</span>
        <h2>Get Your Green Card In 3 Steps</h2>
      </div>
      <div class="steps">
        <div class="step"><h3>Enrol Online</h3><p>Sign up for the Health, Safety &amp; Awareness course in a couple of minutes.</p></div>
        <div class="step"><h3>Complete The Course</h3><p>Work through the course online, at your own pace, from any device.</p></div>
        <div class="step"><h3>Apply For Your Green Card</h3><p>Use your certificate to apply &mdash; or just call us on 0203 400 8738 and we'll take care of the rest.</p></div>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Pricing</span>
        <h2>What It Costs</h2>
      </div>
      <div class="grid grid-3">
        <div class="fact" style="padding:26px;"><strong style="font-size:20px;">&pound;65</strong><span>CSCS card &mdash; includes the &pound;36 CSCS card fee, application fee and VAT</span></div>
        <div class="fact" style="padding:26px;"><strong style="font-size:20px;">&pound;45</strong><span>CITB test &mdash; includes the &pound;23.50 CITB exam fee, booking fee and VAT</span></div>
        <div class="fact" style="padding:26px;"><strong style="font-size:20px;">Call Us</strong><span>For the latest Health, Safety &amp; Awareness course price</span></div>
      </div>
    </div>
  </section>

  <section class="section--tight">""" + cta_band(
        heading="Ready To Start Your Green Card Course?",
        text="Just call us on 0203 400 8738 and our team will take care of the rest.",
    ) + """</section>
"""
    body = body.format(topics_html=topics_html)
    return page(
        "Health, Safety &amp; Awareness Course",
        "Complete the online Health, Safety & Awareness course and apply for your CSCS Green Card with Construction Helps.",
        body,
    )

def build_elearning():
    courses = [
        ("Health, Safety &amp; Awareness", "images/AdobeStock_1516393189-(1).jpeg", "CSCS Green Card"),
        ("Asbestos Awareness", "images/Asbestos-Image-(1).jpeg", "Awareness"),
        ("Manual Handling", "images/Manual-Handling-Image-(1).jpeg", "Awareness"),
        ("PPE Awareness", "images/PPE-Awareness-(1).jpeg", "Awareness"),
        ("Working At Height", "images/Work-at-Height-Image-(1).jpeg", "Awareness"),
        ("Fire Marshall", "images/Fire-Marshall-Image-min.jpeg", "Certificate"),
        ("Risk Assessment Awareness", "images/Risk-Assessment-Awareness.jpeg", "Awareness"),
        ("Confined Space Awareness", "images/Confined-Space-Image-(1).jpeg", "Awareness"),
        ("Electrical Safety", "images/Electrical-Safety-Image-(1).jpeg", "Awareness"),
        ("Noise Awareness", "images/Noise-Awareness-image-(1).jpeg", "Awareness"),
        ("DSE Awareness", "images/DSE-Awareness-(1).jpeg", "Awareness"),
        ("COSHH Awareness", "images/COSSH-Image-(1).jpeg", "Awareness"),
        ("Banksman / Signaller", "images/Banksman-Image-min.jpeg", "Certificate"),
        ("Ladder Safety", "images/Ladder-Safety-min-(1).jpeg", "Awareness"),
        ("Hot Works Awareness", "images/Hot-Works-Image-(1).jpeg", "Awareness"),
        ("Temporary Works Awareness", "images/Temporary-Works-(1).jpeg", "Awareness"),
        ("PUWER Awareness", "images/PUWER-Image-min-(1).jpeg", "Awareness"),
        ("RIDDOR Awareness", "images/RIDDOR-min-(1)-(1).jpeg", "Awareness"),
        ("Mental Health First Aid Awareness", "images/Mental-Health-First-Aid-Awareness.jpeg", "Awareness"),
        ("CDM Regulations Awareness", "images/CDM-Regs-min.jpeg", "Awareness"),
        ("Abrasive Wheels Awareness", "images/Abrasive-wheels-image-(1).jpeg", "Awareness"),
        ("Workplace Safety Awareness", "images/Workplace-Safety-Image-(1).jpeg", "Awareness"),
    ]
    def _course_card(name, img, tag):
        tag_name = "a" if "Health, Safety" in name else "div"
        href = ' href="green-card-online-course.html"' if tag_name == "a" else ""
        return """<{tag_name}{href} class="course-card">
        <div class="course-card__img"><span class="course-card__tag">{tag}</span><img src="{img}" alt="{name}" loading="lazy"></div>
        <div class="course-card__body"><h4>{name}</h4><p>Online, self-paced course with instant certificate on completion.</p></div>
      </{tag_name}>""".format(tag_name=tag_name, href=href, img=img, name=name, tag=tag)

    course_html = "".join(_course_card(name, img, tag) for name, img, tag in courses)

    body = breadcrumb(
        "E-Learning", theme="", eyebrow="Online Training",
        h1="E-Learning Courses",
        lead="Complete your Health, Safety &amp; Awareness course and specialist safety training online, from home, at your own pace.",
    ) + """
  <section class="section">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Course Library</span>
        <h2>Popular Online Courses</h2>
        <p>All courses are online, self-paced and available on any device &mdash; complete your Health, Safety &amp;
        Awareness course for a CSCS Green Card, or brush up on a specific topic.</p>
      </div>
      <div class="grid grid-4">{course_html}</div>
    </div>
  </section>

  """ + trust_strip() + """

  <section class="section--tight">""" + cta_band(
        heading="Ready To Start Learning?",
        text="Not sure which course to pick? Just call us on 0203 400 8738 and our team will take care of the rest.",
    ) + """</section>
"""
    body = body.format(course_html=course_html)
    return page(
        "E-Learning Courses",
        "Complete online construction safety courses including Health, Safety & Awareness, Asbestos, Manual Handling, PPE and more with Construction Helps.",
        body,
    )

def build_about():
    body = breadcrumb(
        "About Us", theme="", eyebrow="About Construction Helps",
        h1="Supporting The UK Construction Workforce",
        lead="We're an independent booking agent helping construction workers pass their CITB test and get the right card, faster.",
    ) + """
  <section class="section">
    <div class="container">
      <div class="info-block">
        <div class="info-block__media">
          <img src="images/front-view-constructor-with-schematic-resize-2.jpeg" alt="Construction Helps team on site">
        </div>
        <div class="info-block__text">
          <span class="eyebrow">Our Story</span>
          <h2>Why We Started Construction Helps</h2>
          <p>Booking a CITB test and figuring out which CSCS, Skill or JIB card you need can be confusing, especially if
          you're new to the industry. Construction Helps was built to make that process simple &mdash; one clear
          booking journey, honest guidance, and a real support team behind it.</p>
          <p>We work with construction workers, tradespeople, apprentices and managers across the UK, helping them book
          tests at over 150 approved centres and apply for the right card the first time.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Our Values</span>
        <h2>What Guides Our Work</h2>
      </div>
      <div class="grid grid-3">
        <div class="service-card"><div class="service-card__icon">🤝</div><h3>Clear Guidance</h3><p>We explain exactly which test and card you need, in plain English, before you book anything.</p></div>
        <div class="service-card"><div class="service-card__icon">⚡</div><h3>Fast Turnaround</h3><p>Next-day CITB test slots and prompt card applications, so you can get back to work quickly.</p></div>
        <div class="service-card"><div class="service-card__icon">🔒</div><h3>Secure &amp; Trusted</h3><p>Safe, secure online payments and instant confirmation for every booking you make with us.</p></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="grid grid-4">
        <div class="fact"><strong>150+</strong><span>Test Centres</span></div>
        <div class="fact"><strong>6</strong><span>CSCS Card Types</span></div>
        <div class="fact"><strong>22+</strong><span>E-Learning Courses</span></div>
        <div class="fact"><strong>UK-Wide</strong><span>Coverage</span></div>
      </div>
    </div>
  </section>

  """ + trust_strip() + """

  <section class="section--tight">""" + cta_band() + """</section>
"""
    return page(
        "About Us",
        "Learn about Construction Helps, an independent UK booking agent for CITB tests, CSCS cards, Skill cards, JIB cards and construction e-learning.",
        body,
    )

def build_contact():
    body = breadcrumb(
        "Contact Us", theme="", eyebrow="Get In Touch",
        h1="Contact Construction Helps",
        lead="Have a question about a card, test booking or course? Our team is here to help.",
    ) + """
  <section class="section">
    <div class="container">
      <div class="contact-grid">
        <div>
          <div class="contact-card">
            <div class="ico">📍</div>
            <div><h4>Our Address</h4><p>{address}</p></div>
          </div>
          <div class="contact-card">
            <div class="ico">📞</div>
            <div><h4>Phone</h4>
              <p><a href="tel:{phone1_tel}">{phone1}</a><br><a href="tel:{phone2_tel}">{phone2}</a></p>
            </div>
          </div>
          <div class="contact-card">
            <div class="ico">✉</div>
            <div><h4>Email</h4><p><a href="mailto:{email}">{email}</a></p></div>
          </div>
          <div class="contact-card">
            <div class="ico">🕘</div>
            <div><h4>Opening Hours</h4><p>Monday &ndash; Friday: 8:00am &ndash; 6:00pm<br>Saturday: 9:00am &ndash; 1:00pm</p></div>
          </div>
          <div class="map-embed">
            <iframe src="https://www.google.com/maps?q=71-75+Shelton+Street+Covent+Garden+London+WC2H+9JQ&output=embed" loading="lazy" title="Construction Helps location"></iframe>
          </div>
        </div>
        <div>
          <form id="contact-form">
            <div class="form-row">
              <div class="field"><label for="name">Full Name</label><input id="name" name="name" type="text" required placeholder="John Smith"></div>
              <div class="field"><label for="email">Email Address</label><input id="email" name="email" type="email" required placeholder="john@example.com"></div>
            </div>
            <div class="form-row">
              <div class="field"><label for="phone">Phone Number</label><input id="phone" name="phone" type="tel" placeholder="07123 456789"></div>
              <div class="field"><label for="topic">I'm Enquiring About</label>
                <select id="topic" name="topic">
                  <option>CITB Test Booking</option>
                  <option>CSCS Green Card</option>
                  <option>CSCS Blue Card</option>
                  <option>CSCS Gold Card</option>
                  <option>CSCS Red Card</option>
                  <option>CSCS White Card</option>
                  <option>CSCS Black Card</option>
                  <option>Skill Card</option>
                  <option>JIB Card</option>
                  <option>E-Learning Courses</option>
                  <option>Other</option>
                </select>
              </div>
            </div>
            <div class="field"><label for="message">Message</label><textarea id="message" name="message" rows="5" placeholder="Tell us a little about what you need help with..."></textarea></div>
            <button type="submit" class="btn btn-primary btn-block">Send Message</button>
          </form>
        </div>
      </div>
    </div>
  </section>

  <section class="section--tight">""" + cta_band(
        heading="Prefer To Talk?",
        text="Just call us on 0203 400 8738 and our team will take care of the rest.",
    ) + """</section>
"""
    body = body.format(**SITE)
    return page(
        "Contact Us",
        "Get in touch with Construction Helps for CITB test bookings, CSCS card applications and e-learning enquiries.",
        body,
    )

def legal_nav(current):
    pages = [
        ("terms.html", "Terms &amp; Conditions"),
        ("privacy.html", "Privacy Policy"),
        ("refund-policy.html", "Refund Policy"),
        ("disclaimer.html", "Disclaimer"),
        ("faqs.html", "FAQs"),
    ]
    items = "".join(
        '<a href="{slug}"{active}>{label}</a>'.format(
            slug=slug, label=label, active=' class="active"' if slug == current else ""
        ) for slug, label in pages
    )
    return '<nav class="legal-nav">{items}</nav>'.format(items=items)

def legal_page_body(nav_slug, breadcrumb_label, eyebrow, h1, lead, content_html):
    return breadcrumb(breadcrumb_label, theme="", eyebrow=eyebrow, h1=h1, lead=lead) + """
  <section class="section">
    <div class="container">
      """ + legal_nav(nav_slug) + """
      <div class="legal-content">
        """ + content_html + """
      </div>
    </div>
  </section>
"""

def build_terms():
    content = """
        <p class="legal-updated">Last updated: 19 July 2026</p>

        <h2>1. About Construction Helps</h2>
        <p>Construction Helps ("we", "us", "our") is an independent booking agent based at 71-75 Shelton Street,
        Covent Garden, London, United Kingdom, WC2H 9JQ. We help construction workers book CITB Health, Safety &amp;
        Environment tests, apply for CSCS, Skill, JIB, ECS and CPCS cards, and access online e-learning courses.</p>
        <p>Construction Helps is not CITB, CSCS, JIB, ECS or CPCS, and is not affiliated with, endorsed by, or
        acting on behalf of any of these organisations. We act as a booking and application support service on
        your behalf.</p>

        <h2>2. Acceptance Of These Terms</h2>
        <p>By using this website, booking a test, or submitting a card application through Construction Helps, you
        agree to be bound by these Terms and Conditions. If you do not agree, please do not use our services.</p>

        <h2>3. Our Services</h2>
        <ul>
          <li>Booking CITB Health, Safety &amp; Environment tests at approved test centres</li>
          <li>Assisting with CSCS, Skill, JIB, ECS and CPCS card applications</li>
          <li>Providing access to online e-learning and awareness courses</li>
          <li>Providing guidance on which test or card is appropriate for your circumstances</li>
        </ul>

        <h2>4. Fees And Payment</h2>
        <p>Our fees include the relevant exam, application or course fee, a booking fee, and VAT where applicable.
        Prices are confirmed before you complete a booking. Payment is taken securely online or by phone at the
        time of booking.</p>

        <h2>5. Rescheduling And Cancellations</h2>
        <p>We offer free rescheduling of CITB test bookings, subject to availability at your chosen test centre.
        See our <a href="refund-policy.html">Refund Policy</a> for full details on cancellations and refunds.</p>

        <h2>6. Test Results And Card Approval</h2>
        <p>Construction Helps books your test and submits your application, but we do not set pass marks, mark
        tests, or approve card applications &mdash; these decisions are made solely by CITB, CSCS, JIB, ECS, CPCS
        or the relevant scheme body. We cannot guarantee that you will pass a test or that a card application will
        be approved.</p>

        <h2>7. Accuracy Of Information</h2>
        <p>We take reasonable care to keep the information on this website accurate and up to date. Card
        eligibility criteria, validity periods and fees are set by third-party scheme bodies and may change without
        notice. Always confirm current requirements with us or the relevant official body before relying on
        information from this site.</p>

        <h2>8. Website Use And Intellectual Property</h2>
        <p>All content on this website, including text, graphics, logos and images, is owned by or licensed to
        Construction Helps and may not be reproduced without our permission, except for personal, non-commercial
        use.</p>

        <h2>9. Limitation Of Liability</h2>
        <p>To the fullest extent permitted by law, Construction Helps is not liable for any indirect or
        consequential loss arising from your use of this website or our services, including loss of earnings
        resulting from a delayed, rescheduled or unsuccessful test or application.</p>

        <h2>10. Governing Law</h2>
        <p>These Terms and Conditions are governed by the laws of England and Wales, and any disputes will be
        subject to the exclusive jurisdiction of the courts of England and Wales.</p>

        <h2>11. Changes To These Terms</h2>
        <p>We may update these Terms and Conditions from time to time. The latest version will always be available
        on this page.</p>

        <h2>12. Contact Us</h2>
        <p>If you have any questions about these Terms and Conditions, please contact us at
        <a href="mailto:Info@constructionhelps.com">Info@constructionhelps.com</a> or call 0203 400 8738.</p>
    """
    body = legal_page_body(
        "terms.html", "Terms &amp; Conditions", "Legal",
        "Terms &amp; Conditions",
        "The terms that apply when you use this website or book a test or card application with us.",
        content,
    )
    return page(
        "Terms &amp; Conditions",
        "Terms and Conditions for using the Construction Helps website and booking CITB tests or card applications.",
        body,
    )

def build_privacy():
    content = """
        <p class="legal-updated">Last updated: 19 July 2026</p>

        <h2>1. Introduction</h2>
        <p>This Privacy Policy explains how Construction Helps collects, uses and protects your personal
        information when you use this website or our booking services, in accordance with the UK General Data
        Protection Regulation (UK GDPR) and the Data Protection Act 2018.</p>

        <h2>2. Information We Collect</h2>
        <ul>
          <li>Contact details you provide, such as your name, email address and phone number</li>
          <li>Booking details, including your preferred test centre, date and card type</li>
          <li>Postcode information, when you use our test centre finder to calculate distances</li>
          <li>Payment information, processed securely by our payment provider &mdash; we do not store full card details</li>
          <li>Technical data such as browser type and pages visited, to help us improve the website</li>
        </ul>

        <h2>3. How We Use Your Information</h2>
        <ul>
          <li>To book your CITB test and process your card application</li>
          <li>To communicate with you about your booking or application status</li>
          <li>To respond to enquiries submitted through our contact form</li>
          <li>To improve our website and services</li>
        </ul>

        <h2>4. Test Centre Finder And Postcode Lookups</h2>
        <p>When you search for your nearest test centre, your postcode is sent to the postcodes.io open data
        service to calculate an approximate location. We do not store the postcodes you search with, and this
        data is used only to calculate distance to our test centre network.</p>

        <h2>5. Sharing Your Information</h2>
        <p>We share the minimum information necessary with CITB, CSCS, JIB, ECS, CPCS, test centres or scheme
        bodies where required to complete your booking or card application. We do not sell your personal
        information to third parties.</p>

        <h2>6. Data Retention</h2>
        <p>We retain your personal information only for as long as necessary to provide our services and to meet
        legal, accounting or reporting requirements.</p>

        <h2>7. Your Rights</h2>
        <p>Under UK GDPR, you have the right to access, correct, delete or restrict use of your personal
        information, and to object to certain processing. To exercise any of these rights, contact us using the
        details below. You also have the right to complain to the Information Commissioner's Office (ICO) at
        ico.org.uk.</p>

        <h2>8. Data Security</h2>
        <p>We use appropriate technical and organisational measures to protect your personal information against
        unauthorised access, loss or misuse.</p>

        <h2>9. Children's Privacy</h2>
        <p>Our services are intended for individuals aged 16 and over. We do not knowingly collect personal
        information from children.</p>

        <h2>10. Changes To This Policy</h2>
        <p>We may update this Privacy Policy from time to time. Any changes will be posted on this page with an
        updated revision date.</p>

        <h2>11. Contact Us</h2>
        <p>For any questions about this Privacy Policy or your personal information, contact us at
        <a href="mailto:Info@constructionhelps.com">Info@constructionhelps.com</a>, by phone on 0203 400 8738, or
        by post at 71-75 Shelton Street, Covent Garden, London, United Kingdom, WC2H 9JQ.</p>
    """
    body = legal_page_body(
        "privacy.html", "Privacy Policy", "Legal",
        "Privacy Policy",
        "How we collect, use and protect your personal information.",
        content,
    )
    return page(
        "Privacy Policy",
        "Privacy Policy explaining how Construction Helps collects, uses and protects your personal information.",
        body,
    )

def build_disclaimer():
    content = """
        <p class="legal-updated">Last updated: 19 July 2026</p>

        <h2>1. General Information</h2>
        <p>The information on this website is provided for general guidance only and does not constitute
        professional, legal or financial advice. While we make every effort to keep information accurate and
        current, we make no warranties about the completeness, reliability or accuracy of this information.</p>

        <h2>2. Independent Booking Agent</h2>
        <p>Construction Helps is an independent booking agent. We are not CITB, CSCS, the Joint Industry Board
        (JIB), the Electrotechnical Certification Scheme (ECS), the Construction Plant Competence Scheme (CPCS),
        or any other awarding or certification body, and we are not affiliated with, endorsed by, or acting as an
        official representative of any of these organisations. All card names, logos and scheme names referenced
        on this site remain the property of their respective owners.</p>

        <h2>3. No Guarantee Of Outcome</h2>
        <p>Booking a test or submitting a card application through Construction Helps does not guarantee that you
        will pass a test, or that your card application will be approved. Final decisions rest solely with CITB,
        CSCS, JIB, ECS, CPCS or the relevant scheme body, in accordance with their own eligibility criteria and
        assessment standards.</p>

        <h2>4. Card Requirements May Change</h2>
        <p>Qualification requirements, test formats, card validity periods and fees are determined by third-party
        scheme bodies and are subject to change without notice. Always confirm the latest requirements with us or
        the relevant official body before making decisions based on information found on this website.</p>

        <h2>5. Test Centre Finder</h2>
        <p>Our test centre finder provides approximate distances based on postcode data, for guidance only. Exact
        venue addresses, available dates and appointment availability are confirmed when you book.</p>

        <h2>6. External Links</h2>
        <p>This website may contain links to third-party websites. We are not responsible for the content,
        accuracy or practices of any external website linked from this site.</p>

        <h2>7. Limitation Of Liability</h2>
        <p>To the fullest extent permitted by law, Construction Helps accepts no liability for any loss or damage
        arising from reliance on information contained on this website.</p>

        <h2>8. Contact Us</h2>
        <p>If you have questions about this Disclaimer, contact us at
        <a href="mailto:Info@constructionhelps.com">Info@constructionhelps.com</a> or call 0203 400 8738.</p>
    """
    body = legal_page_body(
        "disclaimer.html", "Disclaimer", "Legal",
        "Disclaimer",
        "Important information about the limits of the guidance provided on this website.",
        content,
    )
    return page(
        "Disclaimer",
        "Disclaimer covering the independent booking agent status and limitations of information on the Construction Helps website.",
        body,
    )

def build_refund_policy():
    content = """
        <p class="legal-updated">Last updated: 19 July 2026</p>

        <h2>1. Booking Fees</h2>
        <p>When you book a CITB test or submit a card application through Construction Helps, the fee you pay
        covers the relevant exam, application or course fee, our booking fee, and VAT where applicable.</p>

        <h2>2. Free Rescheduling</h2>
        <p>We offer free rescheduling of your CITB test booking, subject to availability at your chosen test
        centre. Just call us on 0203 400 8738 and our team will take care of the rest.</p>

        <h2>3. Cancelling Your Booking</h2>
        <ul>
          <li>Cancellations made more than 48 hours before your scheduled test may be eligible for a full or
          partial refund, less any non-recoverable third-party fees</li>
          <li>Cancellations made within 48 hours of your scheduled test may not be eligible for a refund, as test
          centre slots are reserved on your behalf</li>
          <li>To cancel a booking, contact us as soon as possible on 0203 400 8738 or Info@constructionhelps.com</li>
        </ul>

        <h2>4. Non-Refundable Circumstances</h2>
        <ul>
          <li>Missed appointments without prior notice</li>
          <li>Failed tests &mdash; a retake or new booking fee will apply for a further attempt</li>
          <li>Card applications submitted to CITB, CSCS, JIB, ECS or CPCS on your behalf, where processing has
          already begun</li>
          <li>Completed or partially completed e-learning courses</li>
        </ul>

        <h2>5. How To Request A Refund</h2>
        <p>To request a refund, contact our team by phone or email with your booking reference. We will confirm
        your eligibility and, where approved, process your refund to the original payment method.</p>

        <h2>6. Processing Time</h2>
        <p>Approved refunds are typically processed within 5&ndash;10 working days, though your bank or card
        provider may take longer to show the funds in your account.</p>

        <h2>7. Contact Us</h2>
        <p>For any questions about cancellations or refunds, call us on 0203 400 8738 or email
        <a href="mailto:Info@constructionhelps.com">Info@constructionhelps.com</a>.</p>
    """
    body = legal_page_body(
        "refund-policy.html", "Refund Policy", "Legal",
        "Refund Policy",
        "How cancellations, rescheduling and refunds work when you book with us.",
        content,
    )
    return page(
        "Refund Policy",
        "Refund Policy covering cancellations, rescheduling and refund eligibility for Construction Helps bookings.",
        body,
    )

def build_faqs():
    groups = [
        ("General", [
            ("What is Construction Helps?", "Construction Helps is an independent booking agent that helps construction workers book CITB tests, apply for CSCS, Skill, JIB, ECS and CPCS cards, and access online e-learning courses."),
            ("Are you CITB, CSCS, JIB, ECS or CPCS?", "No. We are an independent booking agent and are not affiliated with, endorsed by, or acting on behalf of any of these organisations. See our <a href=\"disclaimer.html\">Disclaimer</a> for more detail."),
            ("Which card do I need?", "It depends on your trade, qualifications and experience. Visit our <a href=\"cards.html\">CSCS Cards</a> page or just call us on 0203 400 8738 and our team will take care of the rest."),
        ]),
        ("Bookings &amp; Payments", [
            ("How do I book a CITB test?", "Use our <a href=\"citb-test.html\">CITB Test</a> page to book online, or call us on 0203 400 8738 and we'll book it for you over the phone."),
            ("Is payment on this site secure?", "Yes. Payments are processed securely online, and we do not store your full card details."),
            ("Can I reschedule or cancel my booking?", "Yes, we offer free rescheduling subject to availability. See our <a href=\"refund-policy.html\">Refund Policy</a> for cancellation terms."),
            ("What if I fail my test?", "You can book a retake through us. A new booking fee will apply for the further attempt."),
        ]),
        ("Cards &amp; Applications", [
            ("How long does it take to receive my card?", "Processing times vary by scheme body, but we keep you updated by email throughout your application."),
            ("Can you guarantee my application will be approved?", "No. Final approval rests with CITB, CSCS, JIB, ECS or CPCS, in line with their own eligibility criteria — see our <a href=\"disclaimer.html\">Disclaimer</a>."),
            ("Do you offer e-learning courses?", "Yes, browse our full course library on the <a href=\"e-learning.html\">E-Learning</a> page."),
        ]),
        ("Test Centres", [
            ("How do I find my nearest test centre?", "Use our <a href=\"test-centres.html\">test centre finder</a> to search by postcode, or browse all 150+ locations by region."),
            ("Is the test centre finder accurate?", "It gives an approximate distance based on your postcode. Exact venue address and availability are confirmed when you book."),
        ]),
    ]

    groups_html = ""
    for group_title, items in groups:
        items_html = "".join("""<div class="faq-item">
          <button class="faq-q"><span>{q}</span><span class="plus">+</span></button>
          <div class="faq-a"><p>{a}</p></div>
        </div>""".format(q=q, a=a) for q, a in items)
        groups_html += """<div style="margin-bottom:40px;">
          <h3 style="font-size:18px; margin-bottom:6px;">{title}</h3>
          {items_html}
        </div>""".format(title=group_title, items_html=items_html)

    content = """
        <p class="legal-updated">Answers to the questions we're asked most often. Still stuck? Just call us on
        0203 400 8738 and our team will take care of the rest.</p>
        {groups_html}
    """.format(groups_html=groups_html)

    body = legal_page_body(
        "faqs.html", "FAQs", "Support",
        "Frequently Asked Questions",
        "Answers to common questions about bookings, cards, payments and our test centre network.",
        content,
    )
    return page(
        "FAQs",
        "Frequently asked questions about booking CITB tests, CSCS/Skill/JIB/ECS/CPCS cards, payments and test centres with Construction Helps.",
        body,
    )

# ---------------------------------------------------------------- build ----

def main():
    pages = {
        "index.html": build_home(),
        "cards.html": build_cards_hub(),
        "skill-card.html": build_skill_card(),
        "jib-card.html": build_jib_card(),
        "ecs-card.html": build_ecs_card(),
        "cpcs-card.html": build_cpcs_card(),
        "citb-test.html": build_citb_test(),
        "test-centres.html": build_test_centres(),
        "which-citb-test.html": build_which_test(),
        "group-test-booking.html": build_group_booking(),
        "citb-revision.html": build_revision(),
        "citb-mock-tests.html": build_mock_tests_hub(),
        "green-card-online-course.html": build_green_card_course(),
        "e-learning.html": build_elearning(),
        "about.html": build_about(),
        "contact.html": build_contact(),
        "terms.html": build_terms(),
        "privacy.html": build_privacy(),
        "disclaimer.html": build_disclaimer(),
        "refund-policy.html": build_refund_policy(),
        "faqs.html": build_faqs(),
    }
    for c in CARDS:
        pages[c["slug"] + ".html"] = build_card_page(c)
    for m in MOCK_TESTS:
        pages[m["slug"] + ".html"] = build_mock_test_page(m)

    for filename, html in pages.items():
        with open(os.path.join(ROOT, filename), "w", encoding="utf-8") as f:
            f.write(html)
        print("wrote", filename)

if __name__ == "__main__":
    main()
