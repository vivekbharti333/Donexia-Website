# -*- coding: utf-8 -*-
import re, os, glob

BASE = r"D:\Websites\Donexia Website"

HEADER_TMPL = '''<!-- ================= HEADER ================= -->
    <header class="site-header">

        <!-- Announcement bar -->
        <div class="announcement-bar" role="region" aria-label="Announcement">
            <span>New: Free plan — start with no credit card. <a href="{P}pricing.html#free-plan">See what's included</a></span>
            <button type="button" class="announcement-close" aria-label="Dismiss announcement">&times;</button>
        </div>

        <div class="container custom-container">

            <nav class="navbar navbar-expand-lg donexia-navbar">

                <div class="container-fluid px-2">

                    <!-- Logo -->
                    <a class="navbar-brand d-flex align-items-center gap-2" href="{P}index.html">

                        <img src="{P}assets/images/brand/donexia-logo.png" alt="Donexia NGO CRM for Greater Impact" class="brand-logo-img" width="171" height="46">

                    </a>

                    <!-- Mobile Toggle -->
                    <button class="navbar-toggler border-0 shadow-none"
                        type="button"
                        data-bs-toggle="collapse"
                        data-bs-target="#mainNavbar"
                        aria-controls="mainNavbar"
                        aria-expanded="false"
                        aria-label="Open navigation menu">

                        <i class="bi bi-list fs-2"></i>

                    </button>

                    <div class="collapse navbar-collapse" id="mainNavbar">

                        <ul class="navbar-nav mx-auto align-items-lg-center">

                            <li class="nav-item">
                                <a class="nav-link{ACTIVE_HOME}" href="{P}index.html">Home</a>
                            </li>

                            <li class="nav-item">
                                <a class="nav-link{ACTIVE_ABOUT}" href="{P}about.html">About Us</a>
                            </li>

                            <!-- Features -->
                            <li class="nav-item dropdown">

                                <a class="nav-link dropdown-toggle"
                                    href="{P}index.html#features"
                                    data-bs-toggle="dropdown">

                                    Features

                                </a>

                                <ul class="dropdown-menu donexia-dropdown">

                                    <li><a class="dropdown-item" href="{P}index.html#donation-management">Donation Management</a></li>
                                    <li><a class="dropdown-item" href="{P}index.html#volunteer-management">Volunteer Management</a></li>
                                    <li><a class="dropdown-item" href="{P}campaign.html">Campaign Management</a></li>
                                    <li><a class="dropdown-item" href="{P}index.html#activities-management">Activities Management</a></li>
                                    <li><a class="dropdown-item" href="{P}index.html#automatic-receipts">Digital Receipts</a></li>

                                </ul>

                            </li>

                            <!-- Solutions -->
                            <li class="nav-item dropdown">

                                <a class="nav-link dropdown-toggle"
                                    href="{P}index.html#solutions"
                                    data-bs-toggle="dropdown">

                                    Solutions

                                </a>

                                <ul class="dropdown-menu donexia-dropdown">

                                    <li><a class="dropdown-item" href="{P}80g-donation-receipt-software.html">80G Donation Receipts</a></li>
                                    <li><a class="dropdown-item" href="{P}form-10bd-software.html">Form 10BD Records</a></li>
                                    <li><a class="dropdown-item" href="{P}ngo-donor-management-software.html">NGO Donor Management</a></li>
                                    <li><a class="dropdown-item" href="{P}whatsapp-donation-receipts.html">WhatsApp Donation Receipts</a></li>

                                </ul>

                            </li>

                            <li class="nav-item">
                                <a class="nav-link{ACTIVE_GUIDES}" href="{P}guides/">Guides</a>
                            </li>

                            <li class="nav-item">
                                <a class="nav-link{ACTIVE_PRICING}" href="{P}pricing.html">Pricing</a>
                            </li>

                            <li class="nav-item">
                                <a class="nav-link{ACTIVE_CONTACT}" href="{P}contact.html">Contact Us</a>
                            </li>

                        </ul>

                        <div class="nav-btn-wrap">

                            <a href="{P}signup.html" class="request-demo-btn">
                                Start Free
                                <i class="bi bi-arrow-right ms-2"></i>
                            </a>

                        </div>

                    </div>

                </div>

            </nav>

        </div>

    </header>'''

FOOTER_TMPL = '''<!-- ===== FOOTER ===== -->
  <footer class="donexia-footer">
    <div class="container custom-container">
      <div class="footer-inner">

        <div class="row g-4">

          <!-- about -->
          <div class="col-lg-3 col-md-6">
            <div class="footer-brand-block">
              <div class="footer-brand">
                <div class="footer-brand-icon">
                  <i class="bi bi-heart-pulse"></i>
                </div>
                <div class="footer-brand-text">
                  <h3>Donexia</h3>
                  <p>NGO CRM for Greater Impact</p>
                </div>
              </div>

              <p class="footer-about">
                Donexia is an all-in-one NGO CRM that helps you manage donations,
                volunteers, campaigns and communications efficiently.
              </p>
            </div>
          </div>

          <!-- quick links -->
          <div class="col-lg-2 col-md-6">
            <div class="footer-links-block">
              <h4>Quick Links</h4>
              <ul>
                <li><a href="{P}index.html">Home</a></li>
                <li><a href="{P}about.html">About Us</a></li>
                <li><a href="{P}index.html#features">Features</a></li>
                <li><a href="{P}pricing.html">Pricing</a></li>
                <li><a href="{P}campaign.html">Campaign Management</a></li>
                <li><a href="{P}contact.html">Contact Us</a></li>
              </ul>
            </div>
          </div>

          <!-- features -->
          <div class="col-lg-3 col-md-6">
            <div class="footer-links-block">
              <h4>Features</h4>
              <ul>
                <li><a href="{P}index.html#donation-management">Donation Management</a></li>
                <li><a href="{P}index.html#volunteer-management">Volunteer Management</a></li>
                <li><a href="{P}campaign.html">Campaign Management</a></li>
                <li><a href="{P}index.html#automatic-receipts">Digital Receipts</a></li>
                <li><a href="{P}index.html#reports-analytics">Reports & Analytics</a></li>
                <li><a href="{P}index.html#activities-management">Activities Management</a></li>
                <li><a href="{P}80g-donation-receipt-software.html">80G Receipt Software</a></li>
                <li><a href="{P}form-10bd-software.html">Form 10BD Records</a></li>
              </ul>
            </div>
          </div>

          <!-- get started -->
          <div class="col-lg-2 col-md-6">
            <div class="footer-links-block">
              <h4>Get Started</h4>
              <ul>
                <li><a href="{P}signup.html">Start Free — No Card</a></li>
                <li><a href="{P}pricing.html#free-plan">Free Plan Details</a></li>
                <li><a href="{P}contact.html">Book a Demo</a></li>
                <li><a href="{P}pricing.html">View Pricing</a></li>
                <li><a href="{P}guides/">NGO Guides & Resources</a></li>
              </ul>
            </div>
          </div>

          <!-- contact -->
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

        <!-- bottom bar -->
        <div class="footer-bottom">
          <p>© 2026 Datfuslab Technologies Pvt. Ltd. All Rights Reserved.</p>

          <div class="footer-bottom-links">
            <a href="{P}privacy-policy.html">Privacy Policy</a>
            <span>|</span>
            <a href="{P}terms-and-conditions.html">Terms & Conditions</a>
          </div>
        </div>

      </div>
    </div>
  </footer>'''

FAVICON = ('<link rel="icon" href="/favicon.ico" sizes="any" />\n  '
           '<link rel="icon" type="image/png" sizes="192x192" href="/assets/images/brand/icon-192.png" />\n  '
           '<link rel="apple-touch-icon" href="/assets/images/brand/apple-touch-icon.png" />')


def active_map(rel):
    m = {"ACTIVE_HOME": "", "ACTIVE_ABOUT": "", "ACTIVE_GUIDES": "",
         "ACTIVE_PRICING": "", "ACTIVE_CONTACT": ""}
    if rel in ("index.html",):
        m["ACTIVE_HOME"] = " active"
    elif rel == "about.html":
        m["ACTIVE_ABOUT"] = " active"
    elif rel == "pricing.html":
        m["ACTIVE_PRICING"] = " active"
    elif rel == "contact.html":
        m["ACTIVE_CONTACT"] = " active"
    elif rel.startswith("guides/"):
        m["ACTIVE_GUIDES"] = " active"
    return m


pages = sorted(glob.glob(BASE + "/*.html") + glob.glob(BASE + "/guides/*.html"))
for p in pages:
    rel = os.path.relpath(p, BASE).replace("\\", "/")
    s = open(p, encoding="utf-8").read()
    prefix = "../" if rel.startswith("guides/") else ""
    hdr = HEADER_TMPL.replace("{P}", prefix)
    for k, v in active_map(rel).items():
        hdr = hdr.replace("{%s}" % k, v)
    ftr = FOOTER_TMPL.replace("{P}", prefix)

    # favicon links in head
    if 'rel="icon"' not in s:
        anchor = '<meta name="theme-color" content="#f26b21" />'
        if anchor in s:
            s = s.replace(anchor, anchor + "\n  " + FAVICON, 1)
        else:
            print(rel + ": no theme-color anchor, favicon skipped")

    # header replace or insert
    hdr_re = re.compile(r'(?:[ \t]*<!--[^\n]*HEADER[^\n]*-->\s*)?<header class="(?:site-header|privacy-header|legal-header)"[^>]*>.*?</header>', re.S)
    if hdr_re.search(s):
        s = hdr_re.sub(lambda m: hdr, s, count=1)
    elif "<body>" in s:
        s = s.replace("<body>", "<body>\n\n" + hdr, 1)
        print(rel + ": header INSERTED")
    else:
        print(rel + ": NO HEADER APPLIED")
        continue

    # footer replace or insert
    ftr_re = re.compile(r'(?:[ \t]*<!-- ===== FOOTER ===== -->\s*)?<footer class="(?:donexia-footer|privacy-footer|legal-footer)"[^>]*>.*?</footer>', re.S)
    if ftr_re.search(s):
        s = ftr_re.sub(lambda m: ftr, s, count=1)
    elif "</body>" in s:
        s = s.replace("</body>", ftr + "\n\n</body>", 1)
        print(rel + ": footer INSERTED")

    open(p, "w", encoding="utf-8", newline="").write(s)
    print(rel + ": unified")

for p in pages:
    rel = os.path.relpath(p, BASE)
    s = open(p, encoding="utf-8").read()
    assert s.count('<header class="site-header">') == 1, rel
    assert s.count('<footer class="donexia-footer">') == 1, rel
print("sanity checks passed")
