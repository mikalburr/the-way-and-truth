# The Evidence-Based Marketer

Research-backed marketing strategy. No gurus. No hacks.

A Jekyll static site deployable to GitHub Pages at zero cost.

---

## Quick Start (local preview)

```bash
# 1. Install Ruby + Bundler if not already installed
gem install bundler

# 2. Install dependencies
bundle install

# 3. Serve locally with live reload
bundle exec jekyll serve --livereload

# Site runs at http://localhost:4000
```

---

## Deploy to GitHub Pages (zero cost)

### Step 1 — Create your GitHub repo

1. Go to [github.com/new](https://github.com/new)
2. Name it `yourusername.github.io` (replace with your actual GitHub username)
3. Set it to **Public**
4. Do NOT initialize with README — you'll push your own

### Step 2 — Push this project

```bash
cd evidence-based-marketer
git init
git add .
git commit -m "Initial site build"
git branch -M main
git remote add origin https://github.com/yourusername/yourusername.github.io.git
git push -u origin main
```

### Step 3 — Enable GitHub Pages

1. In your repo: **Settings → Pages**
2. Source: **Deploy from a branch**
3. Branch: `main` / `/ (root)`
4. Save

Your site will be live at `https://yourusername.github.io` within 2–5 minutes.

### Step 4 — Update your URLs

Before or after deploy, update these two files:

**`_config.yml`**
```yaml
url: "https://yourusername.github.io"   # your actual URL
```

**`robots.txt`**
```
Sitemap: https://yourusername.github.io/sitemap.xml
```

---

## Custom Domain (optional, still free)

1. Buy a domain (~$10–15/yr from Namecheap or Cloudflare Registrar)
2. In GitHub repo: **Settings → Pages → Custom domain** → enter your domain
3. At your DNS provider, add these records:

| Type | Name | Value |
|------|------|-------|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | yourusername.github.io |

4. Wait for DNS propagation (up to 24h), then enable **Enforce HTTPS** in Pages settings.
5. Update `url` in `_config.yml` to your custom domain.

---

## File Structure

```
evidence-based-marketer/
├── _config.yml              # Site config, plugins, defaults
├── _layouts/
│   ├── default.html         # Base HTML shell
│   ├── post.html            # Article layout (TOC, schema, related)
│   ├── page.html            # Static page layout
│   └── category.html        # Category archive layout
├── _includes/
│   ├── head.html            # <head> with meta/OG/Twitter/schema
│   ├── header.html          # Nav (sticky, mobile-responsive)
│   ├── footer.html          # Footer with nav links
│   └── schema-article.html  # Article JSON-LD structured data
├── _posts/
│   └── YYYY-MM-DD-slug.md   # Blog posts (see template below)
├── category/
│   ├── consumer-psychology.html
│   ├── research-methods.html
│   └── content-strategy.html
├── assets/
│   ├── css/main.css         # Full stylesheet (no framework)
│   └── img/                 # Images (create this folder)
│       ├── logo.png
│       ├── favicon.png
│       ├── apple-touch-icon.png
│       ├── default-og.png   # 1200×630 fallback OG image
│       └── posts/           # Post-specific images
├── index.html               # Homepage
├── about.md                 # About page
├── feed.xml                 # RSS feed
├── sitemap.xml              # XML sitemap
├── robots.txt               # Crawl directives
└── Gemfile                  # Ruby dependencies
```

---

## Writing a New Post

Create a file in `_posts/` named `YYYY-MM-DD-your-slug.md` with this front matter:

```yaml
---
layout: post
title: "Your Full SEO Title Here (include primary keyword)"
description: "One-sentence meta description, 120–160 chars. Include keyword naturally."
date: 2026-05-20
modified_date:               # Update if you revise; leave blank on first publish
author: Michael Burrage
categories: [Consumer Psychology]   # Pick ONE: Consumer Psychology | Research Methods | Content Strategy
tags: [keyword1, keyword2, keyword3]
reading_time: 8              # Estimated minutes; add ~1 min per 200 words
image: /assets/img/posts/your-image.jpg
image_alt: "Descriptive alt text for accessibility and image SEO"
---

Your post content in Markdown here.

## Use H2 for main sections

H2s are auto-linked in the table of contents.

### H3 for subsections

Keep H1 reserved for the post title (set in front matter).
```

---

## SEO Checklist (per post)

- [ ] Title includes primary keyword, under 60 characters
- [ ] `description` is 120–160 characters, includes keyword naturally
- [ ] H1 = title (auto from front matter), H2s = section headers with secondary keywords
- [ ] At least one internal link to a category or related post
- [ ] `image` set (1200×630 for OG; compress to <200KB)
- [ ] `reading_time` set
- [ ] Sources cited at bottom (builds E-E-A-T)
- [ ] `modified_date` updated on any substantive revision

---

## Adding Images

Create `/assets/img/` folder and add:
- `logo.png` — 200×50px, transparent background
- `favicon.png` — 32×32px
- `apple-touch-icon.png` — 180×180px
- `default-og.png` — 1200×630px (shown when post has no image)
- `posts/` subfolder for post-specific hero images (1200×630, compressed)

---

## Next 10 Articles to Write

These represent high-value, low-competition keyword clusters in marketing education:

**Consumer Psychology**
1. Loss aversion in pricing: what the research actually shows
2. The mere exposure effect: why frequency works (and when it doesn't)
3. Peak-end rule: why the last 10 seconds of an experience matter most

**Research Methods**
4. How to design a survey that doesn't lie to you
5. Common variable validity mistakes in marketing research
6. Why your A/B test is probably underpowered

**Content Strategy**
7. Topical authority vs. domain authority: what actually drives rankings in 2026
8. The information gain framework: write content search engines can't replicate
9. Internal linking strategy backed by crawl budget research
10. How to build a content calendar from keyword clusters, not a posting schedule

---

## Questions?

miburrage@gmail.com
