"""Insert 'works on mobile, tablet & laptop' messaging into site pages."""
import re, sys, pathlib

ROOT = pathlib.Path(r"D:\Websites\Donexia Website")

FOOTER_ANCHOR = "<p>\u00a9 2026 Datfuslab Technologies Pvt. Ltd. All Rights Reserved.</p>"
FOOTER_NOTE = ('<p class="footer-device-note"><i class="bi bi-phone"></i>'
               '<i class="bi bi-tablet"></i><i class="bi bi-laptop"></i>'
               "<span>Works on mobile, tablet &amp; laptop</span></p>")

DEVICE_LINE = ('<p class="seo-device-line"><i class="bi bi-phone"></i>'
               '<i class="bi bi-tablet"></i><i class="bi bi-laptop"></i>'
               "<span>Works on mobile, tablet &amp; laptop \u2014 sign in from any device</span></p>")

LANDING = ["80g-donation-receipt-software.html", "automatic-donation-receipts.html",
           "donation-management-software.html", "form-10bd-software.html",
           "ngo-donor-management-software.html", "ngo-reports-analytics-software.html",
           "ngo-volunteer-management-software.html", "whatsapp-donation-receipts.html"]

def patch_footer(path):
    html = path.read_text(encoding="utf-8")
    if 'footer-device-note' in html:
        return "skip"
    if FOOTER_ANCHOR not in html:
        return "NO-ANCHOR"
    html = html.replace(FOOTER_ANCHOR, FOOTER_ANCHOR + FOOTER_NOTE, 1)
    path.write_text(html, encoding="utf-8")
    return "ok"

def patch_landing(path):
    html = path.read_text(encoding="utf-8")
    if 'seo-device-line' in html:
        return "skip"
    # insert after the seo-actions div (not nested, so first </div> closes it)
    new, n = re.subn(r'(<div class="seo-actions">.*?</div>)',
                     r'\1' + DEVICE_LINE, html, count=1, flags=re.S)
    if n == 0:
        return "NO-ANCHOR"
    path.write_text(new, encoding="utf-8")
    return "ok"

results = []
for p in sorted(ROOT.glob("*.html")) + sorted((ROOT / "guides").glob("*.html")):
    results.append((str(p.relative_to(ROOT)), patch_footer(p)))
for name in LANDING:
    results.append((name + " [landing]", patch_landing(ROOT / name)))

for name, status in results:
    print(f"{status:10} {name}")
