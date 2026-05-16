# Activation Guide — The Way & Truth

This file is the single source of truth for getting from "site is built" to "site is making money."

---

## The Products Are Now Ready

Two product files were generated overnight:

| File | Purpose |
|---|---|
| `assets/products/kingdom-mindset-guide.html` | The full $27 product — 30-day Kingdom Mindset Guide |
| `assets/products/first-7-days.html` | The lead magnet — free first 7 days |

These files are **NOT** in the public Jekyll build (excluded in `_config.yml`). They live in the repo for you to convert and distribute.

### Convert each to PDF (30 seconds each)

1. Open the HTML file in Chrome or Safari:
   - `open "assets/products/kingdom-mindset-guide.html"`
   - `open "assets/products/first-7-days.html"`
2. Press **⌘+P**
3. In the print dialog, click **PDF → Save as PDF**
4. Save as `kingdom-mindset-guide.pdf` and `first-7-days.pdf`

The CSS is print-optimized — cover page, proper margins, page breaks between sections, no nav/footer chrome.

---

## Activation Checklist — Make Money Order

### TODAY (30 min)

**☐ 1. Amazon Associates** ([affiliate-program.amazon.com](https://affiliate-program.amazon.com))
- Sign up with your site URL
- Get your tag (e.g., `mikalburr-20`)
- Open `_config.yml`, replace `"YOURTAG-20"` (line 39)
- `git commit` + `git push` → All ~25 affiliate book cards activate

**☐ 2. Gumroad** ([gumroad.com](https://gumroad.com))
- Free account
- Upload `kingdom-mindset-guide.pdf` as product
- Title: "30-Day Kingdom Mindset Guide" • Price: $27
- Copy product ID (URL path after `gum.co/`)
- Open `_config.yml`, replace `"YOURPRODUCTID"` (line 41)
- `git commit` + `git push` → Sales page goes live

**☐ 3. Logos Affiliate** ([logos.com/affiliate-program](https://www.logos.com/affiliate-program))
- Apply. ~1-3 day approval.
- When approved, replace `"YOURLOGOSTAG"` (line 40)
- 10-30% commission on $200-$1500 Logos packages

### THIS WEEK

**☐ 4. Email Service** (MailerLite recommended, free up to 1,000)
- Sign up at [mailerlite.com](https://www.mailerlite.com)
- Create form. Copy embed code.
- Open `_includes/newsletter-cta.html`, replace the `<form>` block (lines 5-9)
- Create automation: signup → deliver `first-7-days.pdf` → 4 days later, email sales page link

**☐ 5. Custom Domain** (~$10/year)
- Buy at [Cloudflare Registrar](https://www.cloudflare.com/products/registrar/) or Namecheap
- DNS: CNAME → `mikalburr.github.io`
- GitHub Settings → Pages → Custom domain
- Update `_config.yml` `url:` and the `CNAME` file in the repo

### WEEK 2-3

**☐ 6. Google AdSense** ([google.com/adsense](https://www.google.com/adsense))
- Apply only after custom domain is live (rejection rate is high on `*.github.io`)
- When approved, in `_config.yml`: set `adsense.enabled: true` + your publisher ID + 4 slot IDs
- Ads appear automatically in the 4 placement zones across every post

**☐ 7. Google Search Console** ([search.google.com/search-console](https://search.google.com/search-console))
- Add your property
- Submit sitemap: `https://yourdomain.com/sitemap.xml`
- 170 posts indexed over 2-6 weeks

---

## What's Already Live

| Asset | URL |
|---|---|
| Home | `/` |
| Free 7-day lead magnet page | `/first-7-days/` |
| Sales page | `/kingdom-mindset-30-day-guide/` |
| Resources hub (all affiliate book cards) | `/resources/` |
| Kingdom Mindset pillar | `/kingdom-mindset-guide/` |
| True Teachings pillar | `/true-teachings-of-jesus-guide/` |
| Biblical Masculinity pillar | `/biblical-masculinity-guide/` |
| Privacy + affiliate disclosure | `/privacy/` |

170 posts in `_posts/`. ~100 live now. The rest publish automatically on their scheduled dates via the GitHub Actions cron (rebuilds daily at 08:00 UTC).

---

## Where to Find the Money

| Revenue Stream | First Dollar | Long-Term |
|---|---|---|
| Gumroad product ($27) | Same day after upload | Highest margin |
| Email → upsell to product | Week 1 | Compounds over time |
| Amazon affiliate | Days | Low % but high volume |
| Logos affiliate | 1-3 days (approval) | Highest AOV |
| AdSense | 2-4 weeks (approval) | Scales with traffic |

---

## Contact / Recovery

- Email: miburrage@gmail.com
- Repo: github.com/mikalburr/the-way-and-truth
- Live site: thewayandtruth.com (once domain is configured)

This file is in `.gitignore` deliberately not — it's checked in so the activation knowledge is preserved.
