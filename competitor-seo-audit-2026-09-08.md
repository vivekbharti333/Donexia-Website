# Donexia vs Competitors — SEO & Conversion Audit
**Date:** 2026-09-08 · **Sites compared:** donexia.in vs donateazy.in, daanmitra.com, sevastack.in

## SEO Health Ratings (estimated from live technical + on-page inspection; Google PageSpeed API was rate-limited, so scores are estimates, not Lighthouse numbers)

| Factor | Donexia | Donateazy | Daan Mitra | Sevastack |
|---|---|---|---|---|
| **Overall SEO rating** | **6/10** | **8/10** | **7/10** | **9/10** |
| Technical foundation | 8/10 | 8/10 | 8/10 | 7/10 |
| On-page (titles/meta/H1) | 8/10 | 8/10 | 8/10 | 7/10 |
| Content depth / topical coverage | 2/10 | 8/10 | 3/10 | 10/10 |
| Schema markup | 5/10 | 9/10 | 7/10 | 10/10 |
| Conversion funnel | 4/10 | 9/10 | 8/10 | 9/10 |
| Speed (proxy: page weight) | 9/10 (~35 KB HTML, 0.94s) | 7/10 (267 KB, 1.47s) | 8/10 (124 KB, 0.54s) | 4/10 (1.1 MB, 1.33s) |

### Page inventory (sitemap URLs)
- **Donexia: 12 pages** (static HTML, no blog)
- **Daan Mitra: 1 page** (pre-launch waitlist — "launching in 10 days")
- **Donateazy: 136 URLs** (blog, guides, free tools, case studies, donor portal)
- **Sevastack: 966 URLs** (blog, guides, comparison pages, NGO directory, careers, GiveHub)

## What competitors do that Donexia does not

1. **A free tier + self-serve signup.** Donateazy free → ₹999 → ₹2,999/mo. Sevastack free → ₹624 → ₹1,999/mo. Daan Mitra free tier + 15-day trial. **Donexia starts at ₹4,999/mo with no free plan, no trial, no pricing page self-serve** — that alone filters out most small NGOs before they ever contact you.
2. **Instant onboarding promise.** All three lead with "10-minute signup, no credit card, first receipt free/in minutes." Donexia's CTAs are "Book a Demo" / "Register Now" — a sales-call motion, not a product-led motion.
3. **Content moat (the biggest SEO gap).** Sevastack publishes compliance guides (85% rule, 12A/80G renewal, compliance calendar), an ROI calculator, comparison pages ("vs Tally", "vs Zoho Books"), and an NGO directory — hundreds of keyword-targeted pages. Donateazy has 30+ compliance guides, 6 free tools, FAQ schema everywhere. Donexia has 12 pages total. Google has almost nothing of yours to rank.
4. **Rich schema.** Donateazy and Sevastack emit FAQPage + SoftwareApplication + AggregateRating + Review schema (eligible for rich results and AI Overviews). Sevastack even serves `llms.txt` for AI search engines. Donexia emits only Organization + WebSite + SoftwareApplication.
5. **Proof with numbers.** Donateazy shows live counters (13,137 donations, ₹41.1Cr processed, 51 NGOs). Sevastack shows 100+ NGOs, named testimonials with metrics (₹3L raised, 10BE in 10 min). Donexia's social proof is one 4-year relationship and testimonials without numbers.
6. **Compliance breadth as the hook.** Competitors lead with 10BD/10BE/FC-4/CSR-1/DPDP/FCRA — the pain that actually wakes NGOs up. Donexia leads with "donation management made simple," a weaker, more generic promise.

## Donexia technical issues found

| Issue | Impact | Fix |
|---|---|---|
| `https://www.donexia.in/` returns **200 (duplicate content)** instead of 301 — your `_redirects` rule exists locally but is NOT live | High — splits ranking signals | Re-deploy / verify the www host is attached to the same Cloudflare Pages project |
| No free plan / no trial; entry price ₹4,999/mo vs competitors' free–₹999 | High — main reason new customers don't convert | Add a free tier (e.g., 50 receipts/yr) or 14-day trial |
| No blog, guides, tools, or directory — 12 pages total | High — near-zero organic keyword coverage | Start a blog/compliance-guide hub; 2 posts/week |
| No FAQ section + FAQPage schema on key pages | Medium | Add FAQ blocks with schema to homepage, pricing, 80G page |
| No AggregateRating/Review schema | Medium | Add product reviews schema once you collect ratings |
| No `llms.txt`, no AI-search optimization | Medium (growing) | Add llms.txt; keep schema rich for AI Overviews |
| Pricing page shows "Email Support" only on cheapest plan; no live chat | Medium | Add WhatsApp chat + response-time promise |
| Social proof lacks numbers | Medium | Add metrics: receipts issued, donors managed, hours saved |

## What Donexia already does well (keep it)
- Clean titles (55–61 chars), unique meta descriptions (~155 chars), one H1 per page, canonicals, hreflang, OG/Twitter cards, robots.txt + sitemap all correct.
- Excellent speed — 35 KB HTML is the lightest of all four; you beat Sevastack badly here.
- Testimonials are real and named (Be Rose, Spedara, etc.) — good trust base.
- Dedicated keyword landing pages (80G receipt software, Form 10BD, WhatsApp receipts) — right idea, too few of them.

## Prioritized action plan
1. **Fix the www redirect** (deploy the `_redirects` you already wrote).
2. **Add a free entry plan or free trial** + "no credit card" self-serve signup. This is the #1 conversion blocker.
3. **Publish content**: start with 20 compliance-guide pages targeting "form 10bd", "80g receipt format", "FCRA FC-4", "CSR-1", "NGO compliance calendar 2026-27" — the exact queries competitors rank for.
4. **Add FAQ + FAQPage schema** to homepage, pricing, and each solution page.
5. **Add numbers everywhere**: live counters or at least static stats (X receipts issued, Y NGOs, Z years).
6. **Add llms.txt** and register with Google Search Console + Bing Webmaster.
7. **Add comparison pages** ("Donexia vs Excel", "Donexia vs Tally", "Donexia vs generic CRM") like Sevastack does.
8. **Add an ROI/time-saved calculator** (all three competitors have one; it's a link magnet and lead magnet).
