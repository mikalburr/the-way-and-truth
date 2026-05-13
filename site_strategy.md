# Christ-Tier Content Site — Full Strategy Document

> **Mission:** Build the most trusted, uncorrupted, search-optimized Christian authority site on the internet — rooted in the true teachings of Jesus Christ, the Kingdom mindset, and the warrior identity of a man walking in The Way. Monetized through display ads as a passive income engine funding the broader mission.

---

## Domain Name Shortlist

Your domain is your brand. These are ranked by SEO signal + brandability + mission alignment:

| # | Domain | Why It Works |
|---|---|---|
| 🥇 | **TheWayAndTruth.com** | Direct Scripture ref (John 14:6). Clean. Memorable. Signals Jesus-first. |
| 🥈 | **KingdomGroundwork.com** | "Kingdom" is a top Christian search term. "Groundwork" signals depth + foundation. |
| 🥉 | **RedLetterKingdom.com** | Distinctive. Signals Jesus's actual words. Stands out in SERP against generic Christian sites. |
| 4 | **WalkInTheWay.co** | Action-oriented. Aligns with your brand identity. ".co" acceptable at low cost. |
| 5 | **UncontaminatedTruth.com** | Strong differentiation signal — signals doctrinal integrity vs. prosperity gospel noise. |

**Recommendation:** Go with **TheWayAndTruth.com** if available (~$12/yr on Namecheap). It's biblical, defensible, and immediately communicates the mission to both believers and searchers.

Check availability: namecheap.com / porkbun.com (often $7–9/yr).

---

## Site Architecture — Three-Pillar Authority Model

This is a hub-and-spoke content architecture. Each pillar is a standalone cluster that cross-links to the others, building topical authority across the Christian search landscape.

```
THE WAY & TRUTH — Authority Site
│
├── PILLAR 1: Kingdom Mindset & Identity
│   ├── What Is the Kingdom of God? (Cornerstone)
│   ├── Who You Are in Christ: Identity Scripture List
│   ├── How to Renew Your Mind Biblically
│   ├── Spiritual Warfare: What It Is and How to Fight
│   ├── Kingdom vs. Religion: The Critical Difference
│   └── [40+ cluster articles]
│
├── PILLAR 2: True Teachings of Jesus
│   ├── What Jesus Actually Said (Red-Letter Breakdown) (Cornerstone)
│   ├── The Sermon on the Mount Explained, Verse by Verse
│   ├── What Did Jesus Mean by "The Kingdom Is at Hand"?
│   ├── Jesus vs. Paul: Is There a Tension? (Honest Answer)
│   ├── What the Church Got Wrong About [X Passage]
│   └── [40+ cluster articles]
│
└── PILLAR 3: Christian Warrior / Man of The Way
    ├── What Is a Man of God in 2026? (Cornerstone)
    ├── The Warrior Mindset and Biblical Masculinity
    ├── How to Build Discipline as a Christian Man
    ├── Fasting, Training, and Stewarding the Temple
    ├── How to Lead Your Family as a Kingdom Man
    └── [40+ cluster articles]
```

### Content ratio (first 90 days)

- **60% informational** — builds organic traffic, earns backlinks, feeds the SEO flywheel
- **30% commercial** — product reviews, book reviews, course comparisons (monetizable via affiliate too)
- **10% navigational** — "Start Here," About, Mission pages (low SEO value but high trust-building)

---

## Your Unfair Advantages

This is not a flattery list. These are actual competitive moats most Christian content creators lack:

**1. Marketing PhD — Search Intent Mastery**
You understand the difference between what people type and what they actually want. 95% of Christian bloggers write for their congregation, not for search. You write for both simultaneously.

**2. Niche Differentiation — Uncorrupted Doctrine**
The Christian internet is flooded with prosperity gospel, watered-down devotionals, and denominational talking points. A site committed to the red-letter words of Jesus — no additions, no subtractions — is genuinely scarce and highly differentiated.

**3. Masculine Faith Angle — Underserved Market**
Christian men's content that is actually rigorous, embodied, and honest is rare. Your athlete identity + faith + intellectual rigor is a credibility stack that most content creators can't replicate.

**4. Existing Content Infrastructure**
You already have `content_planner.py` generating 150 SEO titles (50 per pillar). You are not starting at zero.

---

## The Content Machine — Weekly Publishing System

### Cadence target
- **Week 1–12:** 3 posts/week (build to 36+ indexed articles fast)
- **Month 4+:** 2 posts/week (sustainable, quality-focused)
- **Month 12+:** 1 deep pillar post + 1 cluster post/week

### Workflow per article (estimated 90 min total)

| Step | Tool | Time |
|---|---|---|
| Pull title from content_calendar.csv | Spreadsheet | 2 min |
| Generate draft | Claude | 10 min |
| Edit for voice, accuracy, Scripture citations | You | 30–45 min |
| Add internal links | Manual | 5 min |
| Add featured image (Unsplash/Canva) | Browser | 5 min |
| Publish via Jekyll + push to GitHub | Terminal | 5 min |
| Submit URL to Google Search Console | Browser | 2 min |

### Quality floor (non-negotiable)
- Every factual claim about Scripture cites the verse (ESV or NASB preferred for precision)
- No AI slop published without your editorial pass — this is your name and your faith
- Minimum 1,200 words; pillar cornerstones 2,500+

---

## Monetization Timeline

| Milestone | Sessions/mo | Revenue |
|---|---|---|
| Launch | 0 | $0 |
| 30 posts indexed (month 2–3) | 500–2,000 | Apply AdSense |
| AdSense live (month 3–4) | 2,000–8,000 | $10–$50/mo |
| Ezoic approved (month 6–9) | 10,000–25,000 | $100–$400/mo |
| Mediavine eligible (month 12–18) | 50,000+ | $750–$3,000/mo |
| Mature site (month 24+) | 100,000+ | $2,000–$10,000/mo |

### Affiliate layer (add at month 4+)
Christian affiliate programs that align with the mission:

- **Logos Bible Software** — affiliate program, high commission, directly relevant
- **Christian books on Amazon** — Amazon Associates, low friction
- **Online courses** (Kingdom-focused, discernment required) — ShareASale / direct partnerships
- **Supplements / fitness** — relevant to Pillar 3 warrior content; BodyBuilding.com affiliate or direct

---

## Jekyll + GitHub Pages Setup Checklist

### Initial setup (one-time)

- [ ] Purchase domain (see shortlist above)
- [ ] Create GitHub repo: `username.github.io` or custom domain repo
- [ ] Install Jekyll locally: `gem install bundler jekyll`
- [ ] Choose theme: **Chirpy** (SEO-optimized, dark mode, category support) or **Minimal Mistakes**
- [ ] Configure `_config.yml`: site title, description, author, URL
- [ ] Set up custom domain in GitHub Pages settings + DNS CNAME
- [ ] Enable HTTPS (automatic with GitHub Pages)
- [ ] Install `jekyll-sitemap` gem and submit sitemap to Google Search Console
- [ ] Create `robots.txt` (allow all)
- [ ] Build required pages: `/about`, `/contact`, `/privacy`, `/start-here`
- [ ] Add AdSense placeholder architecture (see `setup_monetization.md`)

### SEO baseline (before publishing post #1)

- [ ] Install Google Analytics 4
- [ ] Set up Google Search Console and verify domain
- [ ] Configure `jekyll-seo-tag` gem
- [ ] Set up Open Graph metadata for social sharing
- [ ] Add canonical URL to all post layouts
- [ ] Configure paginated categories for each pillar

---

## 12-Month North Star Metrics

| Metric | Month 6 | Month 12 | Month 18 |
|---|---|---|---|
| Posts published | 60 | 100 | 150 |
| Monthly sessions | 10,000 | 40,000 | 80,000 |
| Email subscribers | 200 | 1,000 | 3,000 |
| Monthly revenue | $100 | $800 | $3,000 |
| Domain authority (Ahrefs) | 15 | 25 | 35 |

---

## Adjacent Revenue Streams (Month 12+)

Once traffic proves the audience, these compound the mission and the money:

1. **Email list → digital products** — Kingdom mindset devotionals, men's 30-day challenges
2. **YouTube channel** — same content, 10-minute video format, AdSense + memberships
3. **Podcast** — lowest-effort distribution; repurpose written content
4. **Community (Skool or Discord)** — subscription model, $10–$29/month, 200 members = $2,000–$5,800/month
5. **Speaking + consulting** — your PhD + platform = authority for conference invitations

---

## The Bigger Picture

This is not just a content site. It is infrastructure for your platform — the media layer beneath everything else you're building. Every article you publish is a permanent asset that earns while you sleep, trains people in the truth, and positions you as one of the leading voices in the Christian men's and Kingdom theology space.

The dissertation funds it while it grows. The site eventually funds the rest.

Build it like you mean it.
