# -*- coding: utf-8 -*-
"""Generate Donexia guides hub + 4 SEO guide pages."""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))

HEAD_META = """  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <meta name="robots" content="index, follow, max-image-preview:large" />
  <meta name="author" content="Datfuslab Technologies Private Limited" />
  <meta name="theme-color" content="#f26b21" />
  <link rel="canonical" href="{canonical}" />
  <link rel="alternate" hreflang="en-IN" href="{canonical}" />
  <link rel="alternate" hreflang="x-default" href="{canonical}" />
  <meta property="og:type" content="article" />
  <meta property="og:locale" content="en_IN" />
  <meta property="og:site_name" content="Donexia" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:url" content="{canonical}" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{title}" />
  <meta name="twitter:description" content="{desc}" />
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" />
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css" />
  <link rel="stylesheet" href="../assets/css/style.css" />
  <style>
    .guide-article h2 {{ font-size: 1.55rem; font-weight: 700; margin: 2.2rem 0 0.9rem; color: #17233c; }}
    .guide-article h3 {{ font-size: 1.2rem; font-weight: 700; margin: 1.6rem 0 0.6rem; color: #24334f; }}
    .guide-article p, .guide-article li {{ color: #3a4454; line-height: 1.75; }}
    .guide-article ul, .guide-article ol {{ padding-left: 1.3rem; margin-bottom: 1rem; }}
    .guide-article li {{ margin-bottom: 0.45rem; }}
    .guide-hero {{ background: linear-gradient(135deg, #fff4ed 0%, #ffffff 70%); padding: 56px 0 40px; }}
    .guide-meta {{ color: #6b7686; font-size: 0.92rem; }}
    .guide-callout {{ background: #fff4ed; border-left: 4px solid #f26b21; border-radius: 8px; padding: 16px 20px; margin: 1.4rem 0; }}
    .guide-callout p {{ margin: 0; }}
    .guide-table {{ width: 100%; border-collapse: collapse; margin: 1.2rem 0; font-size: 0.95rem; }}
    .guide-table th, .guide-table td {{ border: 1px solid #e5e8ee; padding: 10px 12px; text-align: left; }}
    .guide-table th {{ background: #fff4ed; color: #17233c; }}
    .guide-cta {{ background: linear-gradient(90deg, #ff6a00, #ff4b00); border-radius: 14px; color: #fff; padding: 28px; margin: 2.5rem 0 1rem; }}
    .guide-cta h3 {{ color: #fff; margin-bottom: 6px; }}
    .guide-cta p {{ color: #ffe9dc; margin-bottom: 14px; }}
    .guide-cta a.btn-light {{ font-weight: 700; }}
    .guide-faq .accordion-item {{ margin-bottom: 12px; border: 1px solid #e8eaf0; border-radius: 12px; overflow: hidden; }}
    .guide-faq .accordion-button {{ font-weight: 700; box-shadow: none; }}
    .guide-faq .accordion-button:not(.collapsed) {{ color: #d8530d; background: #fff4ed; }}
    .breadcrumb-wrap {{ --bs-breadcrumb-divider: '/'; }}
  </style>
"""

GUIDE_SCHEMA = """
  <script type="application/ld+json">
{schema}
  </script>
"""

GTAG = """  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-VET913FZZT"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){ dataLayer.push(arguments); }
    gtag('js', new Date());
    gtag('config', 'G-VET913FZZT');
  </script>
"""

HEADER = """<!-- ================= HEADER ================= -->
    <header class="site-header">
        <div class="container custom-container">
            <nav class="navbar navbar-expand-lg donexia-navbar">
                <div class="container-fluid px-2">
                    <a class="navbar-brand d-flex align-items-center gap-2" href="../index.html">
                        <div class="brand-logo"><i class="bi bi-heart-pulse"></i></div>
                        <div class="brand-text"><h2>Donexia</h2><p>NGO CRM for Greater Impact</p></div>
                    </a>
                    <button class="navbar-toggler border-0 shadow-none" type="button" data-bs-toggle="collapse" data-bs-target="#mainNavbar" aria-controls="mainNavbar" aria-expanded="false" aria-label="Open navigation menu">
                        <i class="bi bi-list fs-2"></i>
                    </button>
                    <div class="collapse navbar-collapse" id="mainNavbar">
                        <ul class="navbar-nav mx-auto align-items-lg-center">
                            <li class="nav-item"><a class="nav-link" href="../index.html">Home</a></li>
                            <li class="nav-item"><a class="nav-link" href="../about.html">About Us</a></li>
                            <li class="nav-item"><a class="nav-link" href="../pricing.html">Pricing</a></li>
                            <li class="nav-item"><a class="nav-link active" href="./">Guides</a></li>
                            <li class="nav-item"><a class="nav-link" href="../contact.html">Contact Us</a></li>
                        </ul>
                        <div class="nav-btn-wrap">
                            <a href="../signup.html" class="request-demo-btn">Start Free <i class="bi bi-arrow-right ms-2"></i></a>
                        </div>
                    </div>
                </div>
            </nav>
        </div>
    </header>
"""

FOOTER = """  <!-- ===== FOOTER ===== -->
  <footer class="donexia-footer">
    <div class="container custom-container">
      <div class="footer-inner">
        <div class="row g-4">
          <div class="col-lg-3 col-md-6">
            <div class="footer-brand-block">
              <div class="footer-brand">
                <div class="footer-brand-icon"><i class="bi bi-heart-pulse"></i></div>
                <div class="footer-brand-text"><h3>Donexia</h3><p>NGO CRM for Greater Impact</p></div>
              </div>
              <p class="footer-about">Donexia is an all-in-one NGO CRM that helps you manage donations, volunteers, campaigns and communications efficiently.</p>
            </div>
          </div>
          <div class="col-lg-2 col-md-6">
            <div class="footer-links-block">
              <h4>Quick Links</h4>
              <ul>
                <li><a href="../index.html">Home</a></li>
                <li><a href="../about.html">About Us</a></li>
                <li><a href="../pricing.html">Pricing</a></li>
                <li><a href="../campaign.html">Campaign Management</a></li>
                <li><a href="../contact.html">Contact Us</a></li>
              </ul>
            </div>
          </div>
          <div class="col-lg-3 col-md-6">
            <div class="footer-links-block">
              <h4>Features</h4>
              <ul>
                <li><a href="../index.html#donation-management">Donation Management</a></li>
                <li><a href="../index.html#volunteer-management">Volunteer Management</a></li>
                <li><a href="../campaign.html">Campaign Management</a></li>
                <li><a href="../index.html#automatic-receipts">Digital Receipts</a></li>
                <li><a href="../80g-donation-receipt-software.html">80G Receipt Software</a></li>
                <li><a href="../form-10bd-software.html">Form 10BD Records</a></li>
              </ul>
            </div>
          </div>
          <div class="col-lg-2 col-md-6">
            <div class="footer-links-block">
              <h4>Get Started</h4>
              <ul>
                <li><a href="../signup.html">Start Free — No Card</a></li>
                <li><a href="../pricing.html#free-plan">Free Plan Details</a></li>
                <li><a href="./">NGO Guides & Resources</a></li>
                <li><a href="../contact.html">Book a Demo</a></li>
              </ul>
            </div>
          </div>
          <div class="col-lg-2 col-md-6">
            <div class="footer-links-block footer-contact-block">
              <h4>Contact Us</h4>
              <ul class="footer-contact-list">
                <li><i class="bi bi-telephone"></i> <a href="tel:+917004063385">+91 7004063385</a></li>
                <li><i class="bi bi-envelope"></i> <a href="mailto:info@datfuslab.in">info@datfuslab.in</a></li>
                <li><i class="bi bi-globe"></i> <a href="https://donexia.in/">donexia.in</a></li>
                <li><i class="bi bi-geo-alt"></i> B12, Sector-16B Noida, Uttar Pradesh, India</li>
              </ul>
            </div>
          </div>
        </div>
        <div class="footer-bottom">
          <p>© 2026 Datfuslab Technologies Pvt. Ltd. All Rights Reserved.</p>
          <div class="footer-bottom-links">
            <a href="../privacy-policy.html">Privacy Policy</a>
            <span>|</span>
            <a href="../terms-and-conditions.html">Terms & Conditions</a>
          </div>
        </div>
      </div>
    </div>
  </footer>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
  <script src="../assets/js/mobile-navigation.js"></script>
</body>
</html>
"""

def faq_block(uid, qa):
    items = []
    for i, (q, a) in enumerate(qa):
        show = " show" if i == 0 else ""
        collapsed = "" if i == 0 else " collapsed"
        expanded = "true" if i == 0 else "false"
        items.append(f'''      <div class="accordion-item">
        <h2 class="accordion-header">
          <button class="accordion-button{collapsed}" type="button" data-bs-toggle="collapse" data-bs-target="#{uid}-{i}" aria-expanded="{expanded}" aria-controls="{uid}-{i}">{q}</button>
        </h2>
        <div id="{uid}-{i}" class="accordion-collapse collapse{show}" data-bs-parent="#{uid}Accordion">
          <div class="accordion-body">{a}</div>
        </div>
      </div>''')
    body = "\n".join(items)
    return f'''<section class="guide-faq py-4" aria-labelledby="{uid}-heading">
    <h2 id="{uid}-heading">Frequently Asked Questions</h2>
    <div class="accordion" id="{uid}Accordion">
{body}
    </div>
  </section>'''

def breadcrumb_html(page_name):
    return f'''<nav aria-label="breadcrumb" class="breadcrumb-wrap">
      <ol class="breadcrumb mb-0">
        <li class="breadcrumb-item"><a href="../index.html">Home</a></li>
        <li class="breadcrumb-item"><a href="./">Guides</a></li>
        <li class="breadcrumb-item active" aria-current="page">{page_name}</li>
      </ol>
    </nav>'''

def build_graph(slug, page_name, title, desc, qa, date="2026-09-08"):
    url = f"https://donexia.in/guides/{slug}" if slug else "https://donexia.in/guides/"
    graph = [
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://donexia.in/"},
            {"@type": "ListItem", "position": 2, "name": "Guides", "item": "https://donexia.in/guides/"},
            {"@type": "ListItem", "position": 3, "name": page_name, "item": url},
        ]},
    ]
    if slug:
        graph.insert(0, {
            "@type": "Article",
            "headline": title,
            "description": desc,
            "datePublished": date,
            "dateModified": date,
            "author": {"@type": "Organization", "name": "Donexia", "url": "https://donexia.in/"},
            "publisher": {"@type": "Organization", "name": "Donexia", "url": "https://donexia.in/"},
            "mainEntityOfPage": {"@type": "WebPage", "@id": url},
            "inLanguage": "en-IN",
        })
    if qa:
        graph.append({"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in qa
        ]})
    return {"@context": "https://schema.org", "@graph": graph}

def render_page(filename, title, desc, slug, page_name, hero_sub, body_html, qa, date="2026-09-08"):
    canonical = f"https://donexia.in/guides/{slug}" if slug else "https://donexia.in/guides/"
    schema = json.dumps(build_graph(slug, page_name, title, desc, qa, date), indent=2, ensure_ascii=False)
    faq_html = faq_block("guideFaq", qa) if qa else ""
    html = f"""<!DOCTYPE html>
<html lang="en-IN">
<head>
{HEAD_META.format(title=title, desc=desc, canonical=canonical)}
{GUIDE_SCHEMA.format(schema=schema)}
{GTAG}</head>
<body>
{HEADER}
<main id="main-content">
  <section class="guide-hero">
    <div class="container custom-container">
      {breadcrumb_html(page_name)}
      <h1 class="mt-3" style="font-weight:800; color:#17233c;">{page_name}</h1>
      <p class="guide-meta">{hero_sub}</p>
    </div>
  </section>
  <article class="guide-article container custom-container pb-5" style="max-width: 900px;">
{body_html}
{faq_html}
    <div class="guide-cta text-center">
      <h3>Put this into practice with Donexia</h3>
      <p>Manage donations, donors, receipts and reports from one platform — start free, no credit card.</p>
      <a href="../signup.html" class="btn btn-light">Start Free <i class="bi bi-arrow-right ms-2"></i></a>
      <a href="../contact.html" class="btn btn-outline-light ms-2">Book a Demo</a>
    </div>
  </article>
</main>
{FOOTER}"""
    with open(os.path.join(BASE, filename), "w", encoding="utf-8") as fh:
        fh.write(html)
    print("wrote", filename)

# ============================================================ GUIDE 1: Form 10BD
g1_body = """    <p><strong>Form 10BD</strong> is the statement of donations that Indian charitable institutions approved under Section 80G must file with the Income Tax Department every year. If your NGO issues 80G receipts, this guide explains what Form 10BD is, who must file it, the deadlines, and how to keep your donation records ready all year instead of assembling them in a panic in May.</p>

    <h2>What is Form 10BD?</h2>
    <p>Form 10BD is the electronic statement in which a trust, society or Section 8 company approved under Section 80G reports the donations it received during a financial year. It is filed on the Income Tax e-filing portal and must be accompanied by issuing <strong>Form 10BE</strong> certificates to donors, which donors use to claim their 80G deductions.</p>
    <p>In short: your donors' tax deductions depend on your 10BD filing being accurate and on time. Missing or incorrect filings create problems for the people who supported you.</p>

    <h2>Who must file Form 10BD?</h2>
    <ul>
      <li>Any institution approved under Section 80G (including 12AB-registered trusts, societies and Section 8 companies) that received donations during the financial year and issued or will issue 80G receipts.</li>
      <li>Institutions whose total donations received in a financial year do not exceed ₹5,000 in aggregate are exempt from filing.</li>
      <li>If you did not receive any donations in the year, there is generally nothing to file — but confirm with your Chartered Accountant.</li>
    </ul>

    <h2>Form 10BD due date and penalties</h2>
    <table class="guide-table">
      <tr><th>Item</th><th>Detail</th></tr>
      <tr><td>Filing deadline</td><td>31 May following the end of the financial year (for FY 2025-26, the due date is 31 May 2026)</td></tr>
      <tr><td>Mode of filing</td><td>Electronic, on the Income Tax e-filing portal</td></tr>
      <tr><td>Donor certificates</td><td>Form 10BE must be issued to every donor listed in 10BD</td></tr>
      <tr><td>Late filing fee</td><td>₹200 per day of delay under Section 234G, unless a valid reason is accepted</td></tr>
    </table>
    <div class="guide-callout"><p><strong>Note:</strong> Due dates are sometimes extended by the government. Always verify the current deadline on the Income Tax portal or with your CA before relying on any calendar.</p></div>

    <h2>What information does Form 10BD need?</h2>
    <p>For every donation, you typically need:</p>
    <ol>
      <li>Donor's full name and address</li>
      <li>Donor's PAN (essential — donations of ₹2,000 or more in cash require PAN, and PAN-AIS mismatches cause donor complaints)</li>
      <li>Donation amount and date</li>
      <li>Mode of donation (bank, UPI, cash, cheque, in-kind)</li>
      <li>Purpose or fund the donation is earmarked for, where applicable</li>
      <li>Your institution's 80G approval details, including the approval number/URN and validity period</li>
    </ol>

    <h2>The records problem — and how software fixes it</h2>
    <p>Most NGOs do not struggle with the filing itself. They struggle because donation records live in four places: a receipt book, a spreadsheet, the payment gateway dashboard and someone's WhatsApp. When May arrives, someone spends days reconciling them, hunting for PAN numbers and re-checking amounts.</p>
    <p>A donation management platform like Donexia removes this by design:</p>
    <ul>
      <li>Every donation is recorded once, at the time it is received, with donor details, amount, mode and date.</li>
      <li>Receipts are generated with sequential numbering and sent automatically — no duplicate or missing numbers.</li>
      <li>Donor records stay searchable, so PAN details captured in June are still there in May.</li>
      <li>Reports group donations by donor, mode and period, giving your CA a clean starting point for the 10BD statement.</li>
    </ul>
    <p>See how <a href="../form-10bd-software.html">Donexia keeps Form 10BD records organized</a> all year, or read the <a href="./80g-donation-receipt-guide.html">80G receipt guide</a> to understand what donors expect on their receipts.</p>

    <h2>A simple year-round routine</h2>
    <ol>
      <li><strong>At the time of donation:</strong> record the donation and capture the donor's PAN wherever deduction will be claimed.</li>
      <li><strong>Immediately:</strong> issue the numbered receipt and send it by WhatsApp, SMS or email.</li>
      <li><strong>Monthly:</strong> reconcile gateway and bank payouts against recorded donations.</li>
      <li><strong>In April:</strong> export your donation register and share it with your CA well before the 31 May deadline.</li>
    </ol>
    <div class="guide-callout"><p>This guide is general information, not tax advice. Filing requirements change — always confirm current rules with a qualified Chartered Accountant.</p></div>
"""
g1_qa = [
    ("What is the last date to file Form 10BD?",
     "Form 10BD is generally due by 31 May following the end of the financial year — so for FY 2025-26, the due date is 31 May 2026. The government sometimes extends deadlines, so verify on the Income Tax portal or with your CA."),
    ("What happens if Form 10BD is filed late?",
     "A late filing fee of ₹200 per day of delay applies under Section 234G, unless the tax authority accepts a valid reason for the delay. Donors may also face issues claiming deductions if their 10BE certificate is delayed."),
    ("Is PAN mandatory for donors in Form 10BD?",
     "PAN details are essential for donations where the donor intends to claim an 80G deduction, and cash donations of ₹2,000 or more require the donor's PAN. Capturing PAN at the time of donation avoids painful follow-ups later."),
    ("Does Donexia file Form 10BD for my NGO?",
     "Donexia keeps your donation and donor records organized and exportable so your CA can prepare the filing quickly. The statement itself must be filed by your institution through the Income Tax portal."),
]
render_page("form-10bd-filing-guide.html",
    "Form 10BD Filing Guide for Indian NGOs (FY 2025-26) | Donexia",
    "What is Form 10BD, who must file it, the 31 May deadline, penalties, and how to keep donation records organized all year for Indian NGOs.",
    "form-10bd-filing-guide.html", "Form 10BD Filing Guide for Indian NGOs",
    "Updated September 2026 · By the Donexia team · 6 min read", g1_body, g1_qa)

# ============================================================ GUIDE 2: 80G receipts
g2_body = """    <p>An <strong>80G donation receipt</strong> is more than a thank-you note — it is the document that lets your donors claim tax deductions, and it carries legal weight for your NGO. This guide covers what a proper 80G receipt should contain, the rules around issuing it, a practical template, and how to send receipts instantly.</p>

    <h2>What is an 80G receipt?</h2>
    <p>When a donor gives to an institution approved under Section 80G of the Income Tax Act, the institution issues a receipt that confirms the donation. The donor uses this receipt while filing their income tax return to claim the deduction. Since the introduction of Form 10BE, the donor's certificate is generated as part of the annual statement — but the immediate, numbered receipt your NGO issues remains the primary acknowledgement donors receive and expect.</p>

    <h2>What should an 80G donation receipt contain?</h2>
    <table class="guide-table">
      <tr><th>Field</th><th>Why it matters</th></tr>
      <tr><td>Receipt number and date</td><td>Sequential, never-reused numbering is the first thing auditors check</td></tr>
      <tr><td>Donor's full name and address</td><td>Must match the donor's tax records</td></tr>
      <tr><td>Donor's PAN</td><td>Required for cash donations of ₹2,000 or more; essential for deduction claims and AIS matching</td></tr>
      <tr><td>Donation amount (words and figures)</td><td>Prevents disputes and alteration</td></tr>
      <tr><td>Mode of payment</td><td>Cash, cheque, UPI, bank transfer or in-kind</td></tr>
      <tr><td>Purpose / fund</td><td>Earmarked donations must be identified</td></tr>
      <tr><td>NGO's name, address and 80G approval details</td><td>Approval number/URN and validity period confirm your 80G status</td></tr>
      <tr><td>Authorised signature</td><td>Physical or digital, as per your policy</td></tr>
    </table>

    <h2>The rules that trip NGOs up</h2>
    <ul>
      <li><strong>80G status must be valid.</strong> Receipts issued under an expired or in-renewal 80G approval create problems for donors. Track your approval validity and renew before expiry.</li>
      <li><strong>Cash above ₹2,000 is not deductible.</strong> Donations in cash above ₹2,000 do not qualify for the 80G deduction, so encourage bank, UPI or cheque payments — and make them easy with payment links.</li>
      <li><strong>Deduction percentage varies.</strong> Some funds allow 100% deduction, others 50%, and certain donations face a cap relative to the donor's income. State the applicable category carefully or let your CA advise on wording.</li>
      <li><strong>Numbering discipline.</strong> Never reuse receipt numbers. If a receipt is cancelled, keep the number with a cancellation note — auditors check exactly this.</li>
    </ul>

    <h2>A practical 80G receipt template</h2>
    <div class="guide-callout">
      <p><strong>Receipt No.:</strong> ____ &nbsp;·&nbsp; <strong>Date:</strong> ____<br><br>
      Received with thanks from <strong>[Donor Name]</strong>, PAN <strong>[PAN]</strong>, the sum of <strong>₹[Amount]</strong> (Rupees [in words] only) by <strong>[mode]</strong> towards <strong>[purpose/fund]</strong>.<br><br>
      <strong>[NGO Name]</strong> is registered under Section 80G of the Income Tax Act, 1961, Approval No. <strong>[URN]</strong>, valid up to <strong>[date]</strong>. Donations may qualify for deduction under Section 80G — donors should confirm eligibility with their tax advisor.<br><br>
      For <strong>[NGO Name]</strong><br>Authorized Signatory</p>
    </div>

    <h2>Send receipts instantly, not in March</h2>
    <p>The most common donor complaint is not the receipt format — it is the wait. Receipts typed by hand in March for a donation made in June erode trust and trigger endless follow-ups. With Donexia, a receipt is generated the moment the donation is recorded and sent to the donor automatically by <a href="../whatsapp-donation-receipts.html">WhatsApp</a>, SMS or email. Online donations through integrated gateways trigger receipts with no manual step at all.</p>
    <p>See <a href="../80g-donation-receipt-software.html">Donexia's 80G donation receipt software</a> for how numbering, templates and automatic delivery work together, and the <a href="./form-10bd-filing-guide.html">Form 10BD guide</a> for the year-end statement these receipts feed into.</p>
    <div class="guide-callout"><p>This guide is general information, not tax advice. Receipt wording and deduction rules change — confirm current requirements with a qualified Chartered Accountant.</p></div>
"""
g2_qa = [
    ("What details are mandatory on an 80G donation receipt?",
     "At minimum: a sequential receipt number and date, donor name and address, donation amount in words and figures, payment mode, and your NGO's 80G approval details. The donor's PAN is essential for donations of ₹2,000 or more in cash and strongly recommended for all donations where a deduction will be claimed."),
    ("Is there a limit on cash donations for 80G?",
     "Yes. Cash donations above ₹2,000 do not qualify for the Section 80G deduction. Encourage donors to give via UPI, bank transfer or cheque — payment links make this easy."),
    ("Can 80G receipts be sent digitally?",
     "Yes. Digital receipts sent by WhatsApp, SMS or email are widely used and accepted, provided they carry the same details as a physical receipt and come from sequential, well-controlled numbering."),
    ("What is the difference between an 80G receipt and Form 10BE?",
     "The receipt is the immediate acknowledgement your NGO issues when a donation is received. Form 10BE is the annual certificate issued as part of the Form 10BD statement filed with the Income Tax Department, which donors use as the formal proof for claiming deductions."),
]
render_page("80g-donation-receipt-guide.html",
    "80G Donation Receipts: Format, Rules & Template for NGOs | Donexia",
    "What an 80G donation receipt must contain, the rules on cash limits and numbering, a ready-to-use template, and how to send receipts instantly.",
    "80g-donation-receipt-guide.html", "80G Donation Receipts: Format, Rules & Template",
    "Updated September 2026 · By the Donexia team · 6 min read", g2_body, g2_qa)

# ============================================================ GUIDE 3: Compliance calendar
g3_body = """    <p>Indian NGOs run on deadlines: audit reports, income tax returns, Form 10BD, FCRA returns and TDS statements all land in the same few months. Missing one can mean penalties and, worse, donors losing deductions. This calendar lists the recurring compliance deadlines most Indian trusts, societies and Section 8 companies face, so you can plan the year instead of surviving it.</p>
    <div class="guide-callout"><p><strong>Important:</strong> Deadlines below are the commonly applicable statutory dates. The government frequently extends dates, and your NGO's exact obligations depend on its registrations and income. Always confirm with your Chartered Accountant.</p></div>

    <h2>September 2026 – March 2027 at a glance</h2>
    <table class="guide-table">
      <tr><th>Deadline</th><th>What is due</th><th>Who it applies to</th></tr>
      <tr><td>30 Sep 2026</td><td>Audit report for NGOs whose accounts must be audited (commonly those crossing income thresholds or with foreign funding)</td><td>NGOs requiring audit before ITR filing</td></tr>
      <tr><td>15 Sep / 15 Dec / 15 Mar 2027</td><td>Advance tax instalments</td><td>NGOs with estimated tax liability</td></tr>
      <tr><td>31 Oct 2026</td><td>Income tax return (ITR-7) for most NGOs</td><td>Trusts, societies, Section 8 companies</td></tr>
      <tr><td>31 Dec 2026</td><td>FCRA annual return (FC-4) for FY 2025-26</td><td>NGOs with FCRA registration or prior permission</td></tr>
      <tr><td>31 Jan 2027</td><td>TDS statement for Q3 (Oct–Dec)</td><td>NGOs deducting TDS</td></tr>
      <tr><td>31 Mar 2027</td><td>Fourth advance tax instalment; year-end TDS deposits</td><td>All applicable NGOs</td></tr>
      <tr><td>31 May 2027</td><td>Form 10BD statement + Form 10BE certificates for FY 2026-27</td><td>Institutions approved under 80G that received donations</td></tr>
    </table>

    <h2>The deadlines that hurt NGOs most</h2>
    <h3>1. Form 10BD — 31 May</h3>
    <p>Late filing costs ₹200 per day under Section 234G, and delayed 10BE certificates directly block your donors' deductions. The only reliable way to hit May comfortably is keeping donation records clean all year. See our <a href="./form-10bd-filing-guide.html">Form 10BD filing guide</a>.</p>
    <h3>2. FCRA FC-4 — 31 December</h3>
    <p>NGOs receiving foreign contributions must file the annual FC-4 return by 31 December for the preceding financial year. Expired FCRA registrations and missed renewals are among the most common and most damaging compliance failures.</p>
    <h3>3. ITR-7 — 31 October</h3>
    <p>Most NGOs file ITR-7. Filing requires audited accounts where audit is applicable, which makes the 30 September audit deadline the real gate. Start the audit conversation with your CA by July, not October.</p>

    <h2>How to never miss a deadline again</h2>
    <ol>
      <li><strong>Maintain records continuously.</strong> A donation recorded today with donor details and PAN is one less row to reconstruct at filing time.</li>
      <li><strong>Reconcile monthly.</strong> Match gateway payouts and bank statements to your donation register every month; breaks found in October are cheap, breaks found in May are expensive.</li>
      <li><strong>Calendar your renewals.</strong> 12A/80G approvals and FCRA registration have validity windows — diarise them nine months before expiry, not nine days.</li>
      <li><strong>Use reports, not spreadsheets.</strong> Donexia's audit-ready reports give your CA donor-wise statements, receipt registers and campaign summaries on demand, so filing season stops being a rebuild.</li>
    </ol>
    <p>Related reading: <a href="./80g-donation-receipt-guide.html">80G receipt rules</a> · <a href="../form-10bd-software.html">Form 10BD records in Donexia</a></p>
"""
g3_qa = [
    ("What is the due date for Form 10BD?",
     "31 May following the end of the financial year — for FY 2026-27, that means 31 May 2027. Late filing attracts a fee of ₹200 per day under Section 234G."),
    ("When is the FCRA annual return due?",
     "The FCRA annual return (FC-4) is due by 31 December for the preceding financial year, for NGOs holding FCRA registration or prior permission."),
    ("Which ITR do NGOs file?",
     "Most trusts, societies and Section 8 companies file ITR-7. Where an audit is applicable, the audit report must generally be completed before filing, which makes the 30 September audit deadline the practical first gate."),
    ("How can donation software help with compliance deadlines?",
     "It keeps donation and donor records complete throughout the year, reconciles receipts against bank and gateway payouts, and produces donor-wise reports your CA can work from — turning filing season from a rebuild into an export."),
]
render_page("ngo-compliance-calendar-2026-27.html",
    "NGO Compliance Calendar 2026-27: Every Deadline You Need | Donexia",
    "Form 10BD, Form 10BE, FCRA FC-4, ITR-7, audit reports and TDS deadlines for Indian NGOs, with a practical plan to never miss one.",
    "ngo-compliance-calendar-2026-27.html", "NGO Compliance Calendar 2026-27",
    "Updated September 2026 · By the Donexia team · 7 min read", g3_body, g3_qa)

# ============================================================ GUIDE 4: Donor management
g4_body = """    <p>Most Indian NGOs do not lose donors because the cause is weak — they lose them because records are. A donor who gave in 2024 and never heard back is a donor who will not give in 2026. Good <strong>donor management</strong> is mostly discipline: capture, receipt, thank, report, repeat. Here is how to build that discipline, whether you use a spreadsheet or a platform like Donexia.</p>

    <h2>The five habits of well-run donor registers</h2>
    <h3>1. Capture every donor once, completely</h3>
    <p>For every donation, record: name, phone, email, address, PAN (where deduction will be claimed), amount, date, mode and purpose. Incomplete records are the root cause of most filing-season pain — and of donors you can no longer reach.</p>
    <h3>2. Receipt instantly, every time</h3>
    <p>Send the numbered receipt the moment the donation is recorded, by WhatsApp, SMS or email. Instant receipts do two jobs at once: they build trust, and they create the audit trail your CA and Form 10BD filing depend on. See the <a href="./80g-donation-receipt-guide.html">80G receipt guide</a> for what the receipt must contain.</p>
    <h3>3. Thank beyond the receipt</h3>
    <p>A tax receipt is compliance; a thank-you is relationship. Within 48 hours, send a short personal note. Mid-year, tell donors what their money did — one concrete outcome beats a glossy brochure. Donors who see impact renew; donors who only see receipts lapse.</p>
    <h3>4. Segment and follow up with intention</h3>
    <ul>
      <li><strong>First-time donors:</strong> a welcome call or message within a week dramatically improves second-gift rates.</li>
      <li><strong>Recurring donors:</strong> protect them fiercely — acknowledge every instalment, flag failed payments immediately.</li>
      <li><strong>Lapsed donors (12+ months):</strong> a simple "we miss you, here is what changed" message outperforms silence.</li>
      <li><strong>Major donors:</strong> personal updates, site visits, and involvement in decisions appropriate to their level.</li>
    </ul>
    <h3>5. Report before you are asked</h3>
    <p>Send a year-end summary — amounts, outcomes, financials — before donors ask for it. Transparency is not just ethics; it is your strongest renewal argument, especially for CSR and institutional funders.</p>

    <h2>From spreadsheet to system</h2>
    <p>A spreadsheet works until about two people and a few hundred donors. Beyond that, version conflicts, missing PANs, unreceipted donations and untraceable edits start costing real time. A donor management system removes the fragile parts:</p>
    <ul>
      <li>One shared, searchable donor record per person — no duplicates across team members</li>
      <li>Automatic receipts on every channel, tied to sequential numbering</li>
      <li>Donation history, campaign attribution and communication in one timeline</li>
      <li>Role-based access, so volunteers see what they need and nothing more</li>
      <li>Reports your CA, board and funders can each read</li>
    </ul>
    <p><a href="../ngo-donor-management-software.html">See how Donexia manages NGO donor records</a>, or start with the <a href="./ngo-compliance-calendar-2026-27.html">compliance calendar</a> to plan the year around your donors' tax needs.</p>

    <h2>A simple 30-day reset</h2>
    <ol>
      <li><strong>Week 1:</strong> gather every donor list you have into one deduplicated register.</li>
      <li><strong>Week 2:</strong> fill the gaps — PANs, phone numbers, last gift dates.</li>
      <li><strong>Week 3:</strong> issue any pending receipts and thank-yous.</li>
      <li><strong>Week 4:</strong> set your renewal rhythm — reminders, updates and the year-end report calendar.</li>
    </ol>
    <p>Thirty days of cleanup buys you years of renewals.</p>
"""
g4_qa = [
    ("What is donor management for an NGO?",
     "Donor management is the practice of keeping complete records of every donor and donation, issuing receipts promptly, communicating impact, and following up in a planned way — so donors keep giving year after year."),
    ("What information should we record for each donor?",
     "Name, phone, email, address, PAN where a tax deduction will be claimed, and a full giving history: amounts, dates, payment modes and purposes. The PAN and contact details are what most registers miss."),
    ("How do we get lapsed donors back?",
     "Reach out personally before the lapse becomes silence: acknowledge the gap, share one concrete outcome from their past giving, and make renewing effortless with a payment link. A simple honest message outperforms a generic newsletter."),
    ("When should an NGO switch from Excel to donor management software?",
     "When more than one person handles donations, when donors cross a few hundred, or when receipt numbers, PAN details or reconciliation start slipping — whichever comes first. Those are the points where spreadsheets quietly start losing donors and audit time."),
]
render_page("donor-management-best-practices.html",
    "Donor Management Best Practices for Indian NGOs | Donexia",
    "How Indian NGOs can capture donor data, issue instant 80G receipts, thank donors, win back lapsed donors and move beyond Excel.",
    "donor-management-best-practices.html", "Donor Management Best Practices for Indian NGOs",
    "Updated September 2026 · By the Donexia team · 6 min read", g4_body, g4_qa)

# ============================================================ HUB
hub_body = """    <p>Practical, no-fluff guides for Indian NGOs on donation receipts, Form 10BD, compliance deadlines and donor management — written by the team behind <a href="../index.html">Donexia</a>, an NGO CRM built for India.</p>

    <div class="row g-4 mt-2">
      <div class="col-md-6">
        <div class="p-4 h-100" style="border:1px solid #e8eaf0; border-radius:14px;">
          <h3 style="margin-top:0;"><a href="./form-10bd-filing-guide.html" style="color:#d8530d;">Form 10BD Filing Guide for Indian NGOs</a></h3>
          <p>Who must file, the 31 May deadline, ₹200/day late fees, and how to keep donation records ready all year.</p>
        </div>
      </div>
      <div class="col-md-6">
        <div class="p-4 h-100" style="border:1px solid #e8eaf0; border-radius:14px;">
          <h3 style="margin-top:0;"><a href="./80g-donation-receipt-guide.html" style="color:#d8530d;">80G Donation Receipts: Format, Rules & Template</a></h3>
          <p>The fields every 80G receipt needs, cash-donation limits, numbering discipline and a ready-to-use template.</p>
        </div>
      </div>
      <div class="col-md-6">
        <div class="p-4 h-100" style="border:1px solid #e8eaf0; border-radius:14px;">
          <h3 style="margin-top:0;"><a href="./ngo-compliance-calendar-2026-27.html" style="color:#d8530d;">NGO Compliance Calendar 2026-27</a></h3>
          <p>Form 10BD, 10BE, FCRA FC-4, ITR-7, audit reports and TDS — every recurring deadline in one place.</p>
        </div>
      </div>
      <div class="col-md-6">
        <div class="p-4 h-100" style="border:1px solid #e8eaf0; border-radius:14px;">
          <h3 style="margin-top:0;"><a href="./donor-management-best-practices.html" style="color:#d8530d;">Donor Management Best Practices</a></h3>
          <p>Capture, receipt, thank, renew — the five habits that keep donors giving, plus a 30-day register reset.</p>
        </div>
      </div>
    </div>

    <h2 class="mt-5">Tools, not just reading</h2>
    <p>Every guide above reflects how <a href="../index.html">Donexia</a> handles donations day to day: instant digital receipts on WhatsApp, SMS and email, organized donor records, campaign tracking and audit-ready reports. You can start on the <a href="../pricing.html#free-plan">free plan</a> — no credit card — and put any of these practices to work this week.</p>
"""
render_page("index.html",
    "NGO Guides: Form 10BD, 80G Receipts, Compliance & Donor Management | Donexia",
    "Free guides for Indian NGOs — Form 10BD filing, 80G donation receipts, the 2026-27 compliance calendar and donor management best practices.",
    "", "NGO Guides & Resources",
    "Free guides for Indian nonprofits · Updated September 2026", hub_body, [])
print("All guide pages generated.")
