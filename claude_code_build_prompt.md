# Claude Code Build Prompt — The Way & Truth Jekyll Site

Paste everything below the line into Claude Code (`claude` in your terminal, inside your project folder).

---

Build me a complete Jekyll site for a Christian authority content site called "The Way & Truth." This is a three-pillar SEO content site targeting Christian men — Kingdom Mindset, True Teachings of Jesus, and Christian Warrior identity. It will be hosted on GitHub Pages and monetized through Google AdSense (pending approval) → Ezoic → Mediavine.

Do all of the following in one pass:

---

## 1. Jekyll Project Scaffold

Initialize a Jekyll project in the current directory with this structure:

```
.
├── _config.yml
├── Gemfile
├── .gitignore
├── robots.txt
├── _includes/
│   ├── head.html
│   ├── header.html
│   ├── footer.html
│   ├── ad_unit.html
│   └── seo.html
├── _layouts/
│   ├── default.html
│   ├── post.html
│   ├── page.html
│   └── category.html
├── _pages/
│   ├── about.md
│   ├── contact.md
│   ├── privacy.md
│   └── start-here.md
├── _posts/
│   ├── [sample post — pillar 1]
│   ├── [sample post — pillar 2]
│   └── [sample post — pillar 3]
├── assets/
│   ├── css/
│   │   └── main.scss
│   ├── js/
│   │   └── ad-inject.js
│   └── images/
├── category/
│   ├── kingdom-mindset.md
│   ├── true-teachings.md
│   └── warrior-mindset.md
└── .github/
    └── workflows/
        └── pages.yml
```

---

## 2. `_config.yml`

```yaml
title: "The Way & Truth"
tagline: "The uncorrupted teachings of Jesus Christ — Kingdom identity, warrior mindset, and the real Gospel."
description: "Deep-dive biblical content on Kingdom mindset, the true teachings of Jesus, and Christian manhood. No religion. No compromise. The Way."
url: "https://thewayandtruth.com"
baseurl: ""
author:
  name: "Michael Burrage"
  bio: "Marketing PhD candidate, man of The Way, and writer. Building on the rock."

# Navigation
nav_links:
  - title: "Kingdom Mindset"
    url: /category/kingdom-mindset/
  - title: "True Teachings"
    url: /category/true-teachings/
  - title: "Warrior Mindset"
    url: /category/warrior-mindset/
  - title: "Start Here"
    url: /start-here/

# Monetization — flip enabled: true when AdSense approves
adsense:
  enabled: false
  publisher_id: "ca-pub-XXXXXXXXXX"
  slots:
    header_banner: "XXXXXXXXXX"
    in_article:    "XXXXXXXXXX"
    sidebar:       "XXXXXXXXXX"
    footer:        "XXXXXXXXXX"

# Plugins
plugins:
  - jekyll-sitemap
  - jekyll-seo-tag
  - jekyll-feed
  - jekyll-paginate

paginate: 10
paginate_path: "/page/:num/"

# Collections
collections:
  pages:
    output: true
    permalink: /:name/

# Defaults
defaults:
  - scope:
      path: ""
      type: "posts"
    values:
      layout: "post"
      author: "Michael Burrage"
      show_ads: true

# Exclude from build
exclude:
  - Gemfile
  - Gemfile.lock
  - node_modules
  - README.md
  - content_planner.py
  - "content/pipeline"
```

---

## 3. `Gemfile`

```ruby
source "https://rubygems.org"
gem "jekyll", "~> 4.3"
gem "jekyll-sitemap"
gem "jekyll-seo-tag"
gem "jekyll-feed"
gem "jekyll-paginate"
gem "webrick"
```

---

## 4. `_includes/ad_unit.html`

Build the full conditional ad include exactly as described: when `site.adsense.enabled` is true, render the full AdSense `<ins>` tag with the correct publisher ID and slot pulled from `_config.yml`. When false, render a zero-height hidden placeholder div so layout is never broken. Accept a `slot` parameter (header_banner, in_article, sidebar, footer).

---

## 5. `_layouts/post.html`

Full article layout with:
- SEO meta via jekyll-seo-tag
- Header include
- Breadcrumb: Home > [Category] > [Post Title]
- `<article>` with schema.org `Article` structured data (JSON-LD)
- `{% include ad_unit.html slot="header_banner" %}` immediately after the H1
- Post content via `{{ content }}`
- `{% include ad_unit.html slot="in_article" %}` after the content body
- Estimated read time in the byline (calculate from word count: words / 200, round up)
- Internal links section at the bottom: "You might also like" pulling from `page.related_posts`
- Footer ad unit
- Footer include

---

## 6. `_layouts/default.html`

Clean base layout with:
- `<!DOCTYPE html>`, proper `<head>` with charset, viewport, canonical URL, jekyll-seo-tag
- AdSense verification script in `<head>` (conditional on `site.adsense.enabled`)
- Header include
- Main content area with optional sidebar (sidebar shown when `page.sidebar` is true)
- Sidebar includes `{% include ad_unit.html slot="sidebar" %}`
- Footer include

---

## 7. `_includes/head.html`

Include: charset, viewport, canonical, jekyll-seo-tag, main.css link, Google Fonts (Inter for body, Playfair Display for headings), and the AdSense `<script async>` tag (only when `site.adsense.enabled` is true).

---

## 8. `_includes/header.html`

Responsive navigation with:
- Site title/logo on the left
- Nav links from `site.nav_links` on the right
- Hamburger menu for mobile (pure CSS toggle, no JavaScript dependency)
- Active page highlighting

---

## 9. `_includes/footer.html`

- Site tagline
- Footer nav: About | Contact | Privacy | Start Here
- `{% include ad_unit.html slot="footer" %}`
- Copyright line with current year via `{{ 'now' | date: '%Y' }}`

---

## 10. `assets/css/main.scss`

Write complete, clean CSS (no frameworks) with:
- CSS custom properties for colors: deep charcoal `#1a1a2e`, gold accent `#c9a84c`, off-white `#f5f5f0`, muted text `#555`
- Responsive typography: fluid font sizes, 1.7 line-height for long-form reading
- Article max-width: 720px centered
- Ad container classes: `.ad-wrapper` with `min-height` pre-reserved per slot to prevent CLS
- Code block styling, blockquote styling (left border in gold, slightly indented)
- Mobile-first breakpoints at 768px and 1024px
- Print styles that hide all `.ad-wrapper` elements

---

## 11. `assets/js/ad-inject.js`

After DOM ready, if the `.content` div has 4 or more `<p>` tags, inject an in-article ad placeholder div after the 4th paragraph. Use the slot markup consistent with `ad_unit.html`.

---

## 12. `_pages/about.md`

Front matter: `title: About`, `layout: page`, `permalink: /about/`

Content: Write a genuine, non-generic About page in first person. Tone: confident, faithful, no corporate language. Cover: who Michael is (Marketing PhD candidate, man of The Way, lifelong athlete), the mission of the site (uncorrupted truth of Jesus Christ, no prosperity gospel, no religion as performance), and why this site exists (the internet needs more signal, less noise on what Jesus actually taught). 300–400 words. End with a clear call to action: "Start Here."

---

## 13. `_pages/privacy.md`

Front matter: `title: Privacy Policy`, `layout: page`, `permalink: /privacy/`

Content: Write a complete, Google AdSense-compliant privacy policy covering: data collection (Google Analytics, cookies), AdSense and third-party advertising (DoubleClick cookie, opt-out link), no sale of personal data, contact information. Keep it plain English, not legalese. Include today's effective date.

---

## 14. `_pages/contact.md`

Front matter: `title: Contact`, `layout: page`, `permalink: /contact/`

Simple contact page. Email: miburrage@gmail.com. No contact form needed.

---

## 15. `_pages/start-here.md`

Front matter: `title: Start Here`, `layout: page`, `permalink: /start-here/`

Content: A reader-oriented guide to the site. Introduce the three pillars with a 2-sentence description each and a link to the category page. Tell the new reader exactly where to start based on what they're looking for. Tone: direct, warm, not preachy. End with an invitation to go deep.

---

## 16. Category pages (`category/`)

Create three category landing pages. Each has:
- Front matter: `layout: category`, `title`, `permalink`, `category_slug`, `description`
- Descriptions:
  - **kingdom-mindset**: "Who you are in Christ, the Kingdom of God, renewing the mind, and spiritual identity — not religion, but reality."
  - **true-teachings**: "Verse-by-verse breakdowns of what Jesus actually said. Red-letter, unfiltered, without tradition added on top."
  - **warrior-mindset**: "Biblical manhood, discipline, stewardship of the body, and leading with Kingdom authority."

---

## 17. `_layouts/category.html`

Layout that lists all posts matching the page's `category_slug`, showing title, date, estimated read time, and excerpt. Paginated if more than 10.

---

## 18. Three sample posts (one per pillar)

Write a real, publish-ready article for each pillar. Not placeholder lorem ipsum — actual content. Minimum 800 words each. These are the first three articles on the site and set the quality bar.

**Post 1 — Pillar 1:**
Filename: `_posts/2026-05-12-what-is-kingdom-mindset.md`
Title: "What Is Kingdom Mindset? Everything Beginners Need to Know"
Category: kingdom-mindset
Target keyword: what is kingdom mindset
Content: Define the Kingdom of God as Jesus taught it (not heaven after death, but present reality). Cover Matthew 6:33, Mark 1:15, Luke 17:21. Distinguish Kingdom mindset from religious performance mindset. Practical application section. Scripture throughout. Authoritative but accessible.

**Post 2 — Pillar 2:**
Filename: `_posts/2026-05-12-what-jesus-actually-said.md`
Title: "What Jesus Actually Said: A Red-Letter Breakdown for Serious Believers"
Category: true-teachings
Target keyword: what did jesus actually teach
Content: Focus on the Sermon on the Mount (Matthew 5–7) as the core of Jesus's teaching. Walk through the Beatitudes with plain-language explanation — not Sunday school versions. Address what makes the Sermon on the Mount different from Old Testament law. Challenge readers to read it themselves. Authoritative, intellectual, reverent.

**Post 3 — Pillar 3:**
Filename: `_posts/2026-05-12-christian-warrior-mindset.md`
Title: "What Is a Christian Warrior Mindset? The Biblical Case for Spiritual Strength"
Category: warrior-mindset
Target keyword: christian warrior mindset
Content: Define spiritual warfare from Ephesians 6. Connect bodily discipline (1 Corinthians 9:27) to Kingdom purpose. Address the false dichotomy between gentleness and strength in Christian masculinity. Jesus flipping tables, driving out demons, building a movement — this was not a passive man. Practical: what does a warrior mindset look like in daily life? Discipline, prayer, training, fasting. Strong, masculine tone.

Each post must have proper YAML front matter: `layout`, `title`, `date`, `categories`, `tags`, `description` (150 chars for SEO meta), `image` (placeholder path), `author`.

---

## 19. `.github/workflows/pages.yml`

GitHub Actions workflow that builds the Jekyll site and deploys to GitHub Pages on every push to `main`. Use the official `actions/jekyll-build-pages` and `actions/deploy-pages` actions.

---

## 20. `robots.txt`

```
User-agent: *
Allow: /
Sitemap: https://thewayandtruth.com/sitemap.xml
```

---

## 21. `.gitignore`

Standard Jekyll gitignore: `_site/`, `.sass-cache/`, `.jekyll-cache/`, `Gemfile.lock`, `.DS_Store`

---

## After building all files:

1. Run `bundle install` to confirm the Gemfile resolves cleanly.
2. Run `bundle exec jekyll build` to confirm zero errors.
3. If there are any build errors, fix them before finishing.
4. Report a summary of every file created and confirm the build passed.
