# Monetization Setup Guide — Jekyll + GitHub Pages

> **Strategy:** Build the ad infrastructure into your templates now, before you have an AdSense account. When approval comes, you drop in one ID and every page lights up. No refactoring.

---

## Phase 1 — AdSense Placeholder Architecture (Do This Now)

### 1.1 Create the ad include file

Create `_includes/ad_unit.html`:

```html
{% comment %}
  Ad Unit Include
  Usage: {% include ad_unit.html slot="sidebar" %}
  Slots: sidebar | in_article | footer | header_banner
  Set ADSENSE_ENABLED: true in _config.yml when approved.
{% endcomment %}

{% if site.adsense.enabled %}
<div class="ad-wrapper ad-{{ include.slot }}">
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={{ site.adsense.publisher_id }}"
       crossorigin="anonymous"></script>
  <ins class="adsbygoogle"
       style="display:block"
       data-ad-client="{{ site.adsense.publisher_id }}"
       data-ad-slot="{{ site.adsense.slots[include.slot] }}"
       data-ad-format="auto"
       data-full-width-responsive="true"></ins>
  <script>(adsbygoogle = window.adsbygoogle || []).push({});</script>
</div>
{% else %}
<!-- AD PLACEHOLDER: {{ include.slot }} — AdSense pending approval -->
<div class="ad-placeholder ad-{{ include.slot }}" aria-hidden="true" style="display:none;"></div>
{% endif %}
```

### 1.2 Wire up `_config.yml`

```yaml
# Monetization — flip enabled: true when AdSense approves you
adsense:
  enabled: false                    # ← change to true on approval day
  publisher_id: "ca-pub-XXXXXXXXXX" # ← paste your pub ID here
  slots:
    header_banner: "XXXXXXXXXX"
    in_article:    "XXXXXXXXXX"
    sidebar:       "XXXXXXXXXX"
    footer:        "XXXXXXXXXX"
```

### 1.3 Drop ad includes into your layout files

**`_layouts/post.html`** — Article pages (highest RPM placement):

```html
<!-- AFTER the article title, BEFORE the first paragraph -->
<article class="post-content">
  <header>
    <h1>{{ page.title }}</h1>
    <p class="post-meta">{{ page.date | date: "%B %d, %Y" }}</p>
  </header>

  {% include ad_unit.html slot="header_banner" %}  <!-- above the fold -->

  <div class="content">
    {{ content }}
  </div>

  {% include ad_unit.html slot="in_article" %}     <!-- after content body -->
  {% include ad_unit.html slot="footer" %}
</article>
```

> **Tip:** For `in_article` placement inside long posts, use Liquid to inject the ad after the 3rd paragraph. Add this to `_plugins/inject_ad.rb` (local builds only — GitHub Pages doesn't run custom plugins, so use a JavaScript DOM injection fallback instead):

```javascript
// assets/js/ad-inject.js — runs on every post page
document.addEventListener("DOMContentLoaded", function () {
  const paragraphs = document.querySelectorAll(".content p");
  if (paragraphs.length >= 4) {
    const adHTML = `<div class="ad-mid-content"><!-- in-article ad slot --></div>`;
    paragraphs[3].insertAdjacentHTML("afterend", adHTML);
  }
});
```

**`_layouts/default.html`** — Sidebar (if your theme has one):

```html
<aside class="sidebar">
  {% include ad_unit.html slot="sidebar" %}
  <!-- other sidebar content -->
</aside>
```

### 1.4 CSS — style the placeholders (prevents layout shift on approval)

Add to your main stylesheet:

```css
/* Ad containers — maintain reserved space before approval */
.ad-wrapper {
  margin: 1.5rem 0;
  text-align: center;
  min-height: 90px; /* prevent CLS — matches standard leaderboard */
}

.ad-wrapper.ad-in_article  { min-height: 250px; }
.ad-wrapper.ad-sidebar     { min-height: 600px; }
.ad-wrapper.ad-footer      { min-height: 90px;  }

/* Hide empty placeholders completely (pre-approval) */
.ad-placeholder { display: none !important; }
```

---

## Phase 2 — Google AdSense Approval Checklist

### Traffic threshold
AdSense has **no official minimum**, but approval is near-guaranteed with:
- 30+ published posts
- 20+ sessions/day (Google Search Console verified)
- Site age: 3+ months

### Pre-approval site requirements

| Requirement | What to do |
|---|---|
| Privacy Policy page | Create `/privacy/` — required. Mention data collection and cookies. |
| About page | Create `/about/` — establishes E-E-A-T (Experience, Expertise, Authority, Trust) |
| Contact page | Create `/contact/` — legitimacy signal |
| Original content only | No scraped, AI-only unedited, or thin content |
| No broken links | Run `htmlproofer` before submitting |
| HTTPS | GitHub Pages provides this automatically |
| Sitemap | Add `jekyll-sitemap` gem; submit to Google Search Console |
| robots.txt | Confirm `Disallow:` is not blocking Googlebot |

### How to submit

1. Sign in to [adsense.google.com](https://adsense.google.com)
2. Add your site URL
3. Paste the AdSense verification snippet into `_includes/head.html` (between `<head>` tags)
4. Flip `enabled: false` — leave it off until **after** approval
5. Wait 1–4 weeks for the review email

### AdSense verification snippet placement (`_includes/head.html`)

```html
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{ page.title | default: site.title }}</title>

  <!-- Google AdSense verification — remove after approval if desired -->
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-XXXXXXXXXX"
          crossorigin="anonymous"></script>

  <!-- other head content -->
</head>
```

---

## Phase 3 — Upgrade Path: Ezoic

### Eligibility requirements

| Factor | Minimum | Target |
|---|---|---|
| Monthly sessions | 10,000 | 25,000+ |
| Traffic source | Primarily organic | 70%+ Google Search |
| Content | Original, indexed | 40+ posts |
| Site age | No minimum | 6+ months preferred |
| Niche restrictions | None known | Faith content fully eligible |

### What Ezoic does differently

- **AI ad placement optimization** — tests hundreds of ad positions automatically; typically 2–4× AdSense RPM
- **Ezoic Access Now program** — allows sites under 10K sessions to start; lower RPMs but good for early monetization
- **LEAP (site speed tool)** — required, but improves Core Web Vitals

### Prepare for Ezoic now

1. **Install Google Analytics 4** — Ezoic requires verified analytics before approval
2. **Connect Google Search Console** — verifies organic traffic quality
3. **Create a Cloudflare account** — Ezoic runs through Cloudflare integration (DNS change required)
4. **Enable lazy loading on images** — add `loading="lazy"` to all `<img>` tags in your layouts
5. **Run PageSpeed Insights** on your site; fix any LCP or CLS issues before applying

### Ezoic application

Apply at [ezoic.com/publishers](https://www.ezoic.com/publishers). Use the **Cloudflare integration** path — easiest for static sites. Takes 1–7 days for approval.

---

## Phase 4 — Upgrade Path: Mediavine

### Eligibility requirements

| Factor | Requirement | Notes |
|---|---|---|
| Monthly sessions | **50,000 minimum** | Hard floor — no exceptions |
| Traffic source | Primarily organic search | Social-only traffic typically rejected |
| Content quality | Long-form, original | Short posts flagged in review |
| Niche | Most accepted | Faith/Christian content fully eligible |
| Ad experience | Clean (no violations) | Must not have AdSense policy violations |
| Google Analytics | Required | GA4 accepted |

### Why Mediavine is the target

- **RPM range: $15–$40+** vs AdSense's $2–$6 (same traffic, 5–10× revenue)
- Full-service — they handle all ad ops, you focus on content
- Strong community and creator support

### Prepare for Mediavine now (even at 0 sessions)

1. **Write exclusively long-form (1,500–2,500 words)** — Mediavine's algorithm rewards dwell time
2. **Add a recipe/content card plugin equivalent** — structured content boosts time-on-page
3. **Build an email list from day 1** — shows Mediavine your audience is loyal, not just passing traffic
4. **No more than 3 AdSense/Ezoic units visible at once** — aggressive ad density is a red flag in their review
5. **Document your traffic growth in Google Search Console** — screenshot monthly; use it in your application

### Mediavine application

[mediavine.com/get-started](https://www.mediavine.com/get-started) — apply when you hit 45,000 sessions (apply early, approval takes 4–6 weeks).

---

## Monetization Timeline Summary

| Month | Sessions (est.) | Action |
|---|---|---|
| 0–2 | 0–500 | Publish 30+ posts. Build architecture now. Apply AdSense at month 2. |
| 3–6 | 500–5,000 | AdSense approved. Flip `enabled: true`. Apply Ezoic Access Now. |
| 6–12 | 5,000–25,000 | Ezoic full approval. Begin RPM optimization. |
| 12–18 | 25,000–55,000 | Hit 50K sessions. Apply Mediavine. Switch within 4–6 weeks. |
| 18–24 | 50,000+ | Mediavine live. $500–$3,000/month realistic at this traffic level. |

---

## Quick Reference — Files to Create/Edit

```
your-jekyll-site/
├── _config.yml              ← Add adsense: block
├── _includes/
│   ├── ad_unit.html         ← CREATE — master ad component
│   └── head.html            ← EDIT — add AdSense verification snippet
├── _layouts/
│   ├── post.html            ← EDIT — insert {% include ad_unit.html %}
│   └── default.html         ← EDIT — sidebar ad
├── assets/
│   └── js/
│       └── ad-inject.js     ← CREATE — in-article JS injection
└── _pages/
    ├── privacy.md           ← CREATE — required for AdSense
    ├── about.md             ← CREATE — E-E-A-T signal
    └── contact.md           ← CREATE — legitimacy signal
```
