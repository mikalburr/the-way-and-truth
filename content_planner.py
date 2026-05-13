"""
content_planner.py
------------------
Generates 50 SEO article titles for a given niche topic using question-based,
long-tail keyword patterns. Scores each by search intent and outputs a
structured content calendar CSV.

Usage:
    python content_planner.py
    python content_planner.py --topic "keto diet for women over 40"
    python content_planner.py --topic "keto diet" --output content/pipeline/content_calendar.csv
"""

import argparse
import csv
import os
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal

# ---------------------------------------------------------------------------
# Types
# ---------------------------------------------------------------------------

SearchIntent = Literal["informational", "commercial", "navigational"]


@dataclass
class Article:
    title: str
    target_keyword: str
    word_count_target: int
    internal_linking_suggestions: list[str]
    priority_score: float          # 1–10
    search_intent: SearchIntent
    pattern: str                   # which template generated it


# ---------------------------------------------------------------------------
# Title generation templates
# ---------------------------------------------------------------------------

# Each template is a tuple: (format_string, intent, base_priority_modifier)
# {topic} = raw niche topic
# {Topic} = title-cased version
# Modifiers nudge the base priority up or down within the 1-10 band.

TEMPLATES: list[tuple[str, SearchIntent, float]] = [
    # --- WHO ---
    ("Who Should {Topic}? A Complete Guide", "informational", 0.0),
    ("Who Benefits Most from {topic}?", "informational", -0.5),
    ("Who Created {Topic} and Why Does It Matter?", "informational", -1.0),
    ("Who Needs {Topic} in Their Life?", "informational", -0.5),

    # --- WHAT ---
    ("What Is {Topic}? Everything Beginners Need to Know", "informational", 1.0),
    ("What Are the Benefits of {topic}?", "informational", 0.5),
    ("What Are the Biggest Mistakes People Make with {topic}?", "informational", 0.5),
    ("What Does {topic} Actually Do? Science Explained", "informational", 0.0),
    ("What to Expect in Your First 30 Days of {Topic}", "informational", 0.5),
    ("What Is the Best Way to Start {topic}?", "commercial", 0.5),
    ("What Are the Side Effects of {topic}?", "informational", 0.0),
    ("What Nobody Tells You About {topic}", "informational", 1.0),

    # --- HOW ---
    ("How to Start {topic}: Step-by-Step for Beginners", "informational", 1.5),
    ("How to Get Results with {topic} Faster Than You Think", "informational", 1.0),
    ("How to Choose the Right {topic} for Your Goals", "commercial", 1.0),
    ("How to Avoid the Top 5 {Topic} Mistakes", "informational", 1.0),
    ("How Long Does {topic} Take to Work?", "informational", 0.5),
    ("How Much Does {topic} Cost? Full Breakdown", "commercial", 1.0),
    ("How to Build a {topic} Habit That Actually Sticks", "informational", 0.5),
    ("How to Track Your Progress with {topic}", "informational", 0.0),
    ("How to Combine {topic} with Other Strategies for Better Results", "informational", 0.5),
    ("How to Do {topic} on a Budget", "commercial", 0.5),

    # --- WHY ---
    ("Why {topic} Works (And Why Most People Quit Too Soon)", "informational", 0.5),
    ("Why You're Not Seeing Results with {topic}", "informational", 1.0),
    ("Why {Topic} Is More Effective Than You Think", "informational", 0.0),
    ("Why Experts Recommend {topic} for Long-Term Results", "commercial", 0.5),

    # --- BEST ---
    ("Best {Topic} Tips for Beginners in {year}", "commercial", 2.0),
    ("Best {Topic} Tools and Resources You Need Right Now", "commercial", 1.5),
    ("Best Ways to Stay Consistent with {topic}", "informational", 0.5),
    ("Best {Topic} Plan for Results in 90 Days", "commercial", 1.5),
    ("Best Books and Courses on {Topic} Reviewed", "commercial", 1.0),
    ("Best {Topic} Apps to Track Your Progress", "commercial", 1.0),
    ("Best Time to Do {topic}: Morning vs. Evening", "informational", 0.5),

    # --- VS / COMPARISON ---
    ("{Topic} vs. Traditional Methods: Which Actually Works?", "commercial", 1.5),
    ("{Topic} for Beginners vs. Advanced: What's the Difference?", "informational", 0.5),
    ("{Topic} vs. Other Approaches: An Honest Comparison", "commercial", 1.5),
    ("Free vs. Paid {Topic} Resources: Which Is Worth It?", "commercial", 1.0),

    # --- LONG-TAIL QUESTION ---
    ("Is {topic} Worth It? Honest Pros and Cons", "commercial", 2.0),
    ("Can You Do {topic} Without [Equipment/Supplements/Experience]?", "informational", 0.5),
    ("Does {topic} Work for Everyone? Real-World Results", "informational", 1.0),
    ("{Topic} for Beginners: Where to Start When You Know Nothing", "informational", 1.5),
    ("{Topic} for Weight Loss: What the Research Says", "informational", 1.0),
    ("{Topic} for Busy People: A Realistic 15-Minute Routine", "informational", 1.0),
    ("{Topic} Success Stories: Before and After Results", "commercial", 0.5),
    ("The Ultimate {Topic} Checklist for Beginners", "informational", 1.5),
    ("10 Reasons You Should Try {topic} This Year", "informational", 0.5),
    ("{Topic} FAQ: 20 Questions Answered by Experts", "informational", 1.0),
    ("{Topic} Myths Debunked: What Science Really Says", "informational", 0.5),
    ("The Complete {Topic} Glossary: Terms You Need to Know", "informational", -0.5),
]


# ---------------------------------------------------------------------------
# Priority scoring logic
# ---------------------------------------------------------------------------

INTENT_BASE_PRIORITY: dict[SearchIntent, float] = {
    "informational": 6.0,
    "commercial":    8.0,
    "navigational":  4.0,
}

INTENT_WORD_COUNT: dict[SearchIntent, int] = {
    "informational": 1800,
    "commercial":    1200,
    "navigational":  800,
}


def score_priority(intent: SearchIntent, modifier: float) -> float:
    base = INTENT_BASE_PRIORITY[intent]
    raw = base + modifier
    return round(min(10.0, max(1.0, raw)), 1)


# ---------------------------------------------------------------------------
# Keyword extraction
# ---------------------------------------------------------------------------

def extract_keyword(title: str, topic: str) -> str:
    """
    Build a clean long-tail keyword from the title.
    Strategy: strip filler words from the title, keep the topic + key qualifier.
    """
    topic_lower = topic.lower().strip()

    # Remove common leading filler
    fillers = r"^(the ultimate|a complete|complete|an honest|honest|real-world|full)\s+"
    clean = re.sub(fillers, "", title.lower(), flags=re.IGNORECASE)

    # Remove trailing filler
    clean = re.sub(r"\s*:.*$", "", clean)  # strip subtitle after colon
    clean = re.sub(r"\?.*$", "", clean)    # strip after question mark

    # If the topic already appears, use as-is (truncated)
    if topic_lower in clean:
        kw = clean.strip()
    else:
        kw = f"{topic_lower} {clean.strip()}"

    # Clean up whitespace and lowercase
    kw = re.sub(r"\s+", " ", kw).strip().lower()

    # Cap at ~60 chars for readability
    if len(kw) > 60:
        kw = kw[:57] + "..."

    return kw


# ---------------------------------------------------------------------------
# Internal linking suggestions
# ---------------------------------------------------------------------------

def generate_internal_links(index: int, total: int, topic: str) -> list[str]:
    """
    Suggest 2-3 internal link targets based on position in the content plan.
    Links flow from pillar → cluster → supporting pages.
    """
    suggestions: list[str] = []

    # Always link to the cornerstone "What Is" piece
    suggestions.append(f"What Is {topic.title()}? Everything Beginners Need to Know")

    # Mid-funnel pieces link to conversion-oriented content
    if index > total // 3:
        suggestions.append(f"Best {topic.title()} Tips for Beginners")

    # Lower-funnel pieces link to comparison content
    if index > (total * 2) // 3:
        suggestions.append(f"Is {topic.title()} Worth It? Honest Pros and Cons")

    return suggestions


# ---------------------------------------------------------------------------
# Main generation function
# ---------------------------------------------------------------------------

def generate_articles(topic: str) -> list[Article]:
    import datetime
    year = datetime.date.today().year
    topic_title = topic.strip().title()
    topic_lower = topic.strip().lower()

    articles: list[Article] = []

    for i, (template, intent, modifier) in enumerate(TEMPLATES):
        title = (
            template
            .replace("{topic}", topic_lower)
            .replace("{Topic}", topic_title)
            .replace("{year}", str(year))
        )

        keyword = extract_keyword(title, topic_lower)
        word_count = INTENT_WORD_COUNT[intent]
        priority = score_priority(intent, modifier)
        links = generate_internal_links(i, len(TEMPLATES), topic_lower)

        articles.append(Article(
            title=title,
            target_keyword=keyword,
            word_count_target=word_count,
            internal_linking_suggestions=links,
            priority_score=priority,
            search_intent=intent,
            pattern=template,
        ))

    # Sort by priority descending for the calendar
    articles.sort(key=lambda a: a.priority_score, reverse=True)

    return articles


# ---------------------------------------------------------------------------
# CSV output
# ---------------------------------------------------------------------------

CSV_FIELDNAMES = [
    "priority_score",
    "title",
    "target_keyword",
    "search_intent",
    "word_count_target",
    "internal_linking_suggestions",
]


def write_csv(articles: list[Article], output_path: str) -> None:
    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)

    with open(out, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDNAMES)
        writer.writeheader()

        for art in articles:
            writer.writerow({
                "priority_score":               art.priority_score,
                "title":                        art.title,
                "target_keyword":               art.target_keyword,
                "search_intent":                art.search_intent,
                "word_count_target":            art.word_count_target,
                "internal_linking_suggestions": " | ".join(art.internal_linking_suggestions),
            })

    print(f"\n✓ Content calendar saved → {out.resolve()}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate a 50-article SEO content calendar for a niche topic."
    )
    parser.add_argument(
        "--topic", "-t",
        type=str,
        default=None,
        help="The niche topic (e.g. 'intermittent fasting for women')",
    )
    parser.add_argument(
        "--output", "-o",
        type=str,
        default="content/pipeline/content_calendar.csv",
        help="Output CSV path (default: content/pipeline/content_calendar.csv)",
    )
    args = parser.parse_args()

    # Interactive prompt if no topic passed
    topic = args.topic
    if not topic:
        topic = input("Enter your niche topic: ").strip()
    if not topic:
        print("Error: topic cannot be empty.")
        raise SystemExit(1)

    print(f"\nGenerating 50 SEO titles for: \"{topic}\"")
    articles = generate_articles(topic)

    # Print preview table to console
    print(f"\n{'#':<4} {'P':>4}  {'Intent':<15} {'WC':>5}  Title")
    print("-" * 90)
    for i, art in enumerate(articles, 1):
        short_title = art.title[:60] + ("…" if len(art.title) > 60 else "")
        print(f"{i:<4} {art.priority_score:>4}  {art.search_intent:<15} {art.word_count_target:>5}  {short_title}")

    # Intent summary
    intent_counts = {}
    for art in articles:
        intent_counts[art.search_intent] = intent_counts.get(art.search_intent, 0) + 1
    print(f"\nIntent mix → ", " | ".join(f"{k}: {v}" for k, v in sorted(intent_counts.items())))

    write_csv(articles, args.output)


if __name__ == "__main__":
    main()
