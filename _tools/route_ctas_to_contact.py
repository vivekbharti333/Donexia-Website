"""One-off: route all signup.html CTAs to contact.html and fix labels.

Usage: python _tools/route_ctas_to_contact.py
Edits root *.html, guides/*.html, assets/js/mobile-navigation.js and the
header/footer generator scripts in place.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

HTML_FILES = list(ROOT.glob("*.html")) + list((ROOT / "guides").glob("*.html"))
JS_FILE = ROOT / "assets" / "js" / "mobile-navigation.js"
TOOL_FILES = [ROOT / "_tools" / "unify_header_footer.py", ROOT / "_tools" / "build_guides.py"]

changes = {}


def apply(path, func):
    text = path.read_text(encoding="utf-8")
    new = func(text)
    if new != text:
        changes[str(path.relative_to(ROOT))] = True
        path.write_text(new, encoding="utf-8")


def fix_html(text):
    n = 0
    # 1. All signup links -> contact links
    text, c = re.subn(r'href="\.\./signup\.html"', 'href="../contact.html"', text); n += c
    text, c = re.subn(r'href="signup\.html"', 'href="contact.html"', text); n += c

    # 2. Nav button (root pages: multi-line, guides: single-line)
    text, c = re.subn(r'(class="request-demo-btn">\s*)Start Free', r'\1Contact Us', text); n += c
    # 3. Footer / CTA labels
    text, c = re.subn(r'>Start Free — No Card<', '>Contact Us<', text); n += c
    text, c = re.subn(r'(class="cta-btn">\s*)Start Free', r'\1Contact Us', text); n += c
    text, c = re.subn(r'(class="btn-explore">\s*)Start Free', r'\1Contact Us', text); n += c
    text, c = re.subn(r'(class="seo-btn" href="contact\.html">)Start [Ff]ree', r'\1Contact Us', text); n += c
    text, c = re.subn(r'(class="btn btn-light">)Start Free', r'\1Contact Us', text); n += c
    text, c = re.subn(r'(class="cta-btn">)Start free — no card', r'\1Contact us', text); n += c
    # 4. Pricing plan buttons
    text, c = re.subn(r'(class="plan-btn[^"]*"[^>]*>\s*)Get Started Free', r'\1Contact Us', text); n += c
    text, c = re.subn(r'(class="plan-btn[^"]*"[^>]*>\s*)Start Free Trial', r'\1Contact Us', text); n += c
    text, c = re.subn(r'aria-label="Start free with the Donexia Free plan"',
                      'aria-label="Contact us about the Donexia Free plan"', text); n += c
    text, c = re.subn(r'aria-label="Start a free trial of the Donexia Pro plan"',
                      'aria-label="Contact us about the Donexia Pro plan"', text); n += c
    text, c = re.subn(r'aria-label="Start a free trial of the Donexia Premium plan"',
                      'aria-label="Contact us about the Donexia Premium plan"', text); n += c
    return text


def fix_js(text):
    n = 0
    text, c = re.subn(r'href: prefix \+ "signup\.html"', 'href: prefix + "contact.html"', text); n += c
    text, c = re.subn(r'href: "\.\./signup\.html"', 'href: "../contact.html"', text); n += c
    text, c = re.subn(r'link: "Start free"', 'link: "Contact us"', text); n += c
    return text


def fix_tools(text):
    n = 0
    text, c = re.subn(r'\{P\}signup\.html', '{P}contact.html', text); n += c
    text, c = re.subn(r'\.\./signup\.html', '../contact.html', text); n += c
    text, c = re.subn(r'(class="request-demo-btn">\s*)Start Free', r'\1Contact Us', text); n += c
    text, c = re.subn(r'>Start Free — No Card<', '>Contact Us<', text); n += c
    text, c = re.subn(r'(class="btn btn-light">)Start Free', r'\1Contact Us', text); n += c
    return text


for f in HTML_FILES:
    apply(f, fix_html)
apply(JS_FILE, fix_js)
for f in TOOL_FILES:
    apply(f, fix_tools)

print("Modified files:")
for k in sorted(changes):
    print(" -", k)
