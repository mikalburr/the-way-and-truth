#!/usr/bin/env python3
"""
Build print-ready standalone HTML files for the digital products.

Output:
  assets/products/kingdom-mindset-guide.html  — Full 30-day guide ($27 product)
  assets/products/first-7-days.html           — Free 7-day lead magnet

To produce PDFs: open each .html in a browser, Cmd+P, "Save as PDF".
The CSS @media print rules format them properly.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "_pages" / "the-kingdom-mindset-guide-content.md"
OUT_DIR = ROOT / "assets" / "products"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def strip_front_matter(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            return text[end + 5 :]
    return text


def md_to_html(md: str) -> str:
    """Minimal markdown to HTML for the subset used in our guide content."""
    # Drop HTML wrapper divs from the source (we provide our own)
    md = re.sub(r'<div[^>]*>', '', md)
    md = re.sub(r'</div>', '', md)

    lines = md.split("\n")
    html_lines = []
    i = 0
    in_para = False
    para_buffer = []

    def flush_paragraph():
        nonlocal para_buffer, in_para
        if para_buffer:
            txt = " ".join(para_buffer).strip()
            if txt:
                html_lines.append(f"<p>{inline_md(txt)}</p>")
            para_buffer = []
            in_para = False

    def inline_md(text: str) -> str:
        # Bold
        text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
        # Italic (single *)
        text = re.sub(r'(?<!\*)\*([^*\n]+)\*(?!\*)', r'<em>\1</em>', text)
        # Underscore italic
        text = re.sub(r'(?<![_a-zA-Z0-9])_([^_\n]+)_(?![_a-zA-Z0-9])', r'<em>\1</em>', text)
        # Code
        text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
        # Links
        text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
        # Em dashes already in text are fine
        return text

    while i < len(lines):
        line = lines[i].rstrip()

        # Horizontal rule
        if re.match(r'^-{3,}\s*$', line):
            flush_paragraph()
            html_lines.append('<hr>')
            i += 1
            continue

        # Headings
        m = re.match(r'^(#{1,4})\s+(.+)$', line)
        if m:
            flush_paragraph()
            level = len(m.group(1))
            content = inline_md(m.group(2).strip())
            html_lines.append(f"<h{level}>{content}</h{level}>")
            i += 1
            continue

        # Blockquote
        if line.startswith('> '):
            flush_paragraph()
            quote_lines = []
            while i < len(lines) and lines[i].startswith('> '):
                quote_lines.append(lines[i][2:].rstrip())
                i += 1
            content = inline_md(" ".join(quote_lines))
            html_lines.append(f"<blockquote><p>{content}</p></blockquote>")
            continue

        # Unordered list
        if re.match(r'^[-*]\s+', line):
            flush_paragraph()
            html_lines.append('<ul>')
            while i < len(lines) and re.match(r'^[-*]\s+', lines[i]):
                item = re.sub(r'^[-*]\s+', '', lines[i].rstrip())
                html_lines.append(f"<li>{inline_md(item)}</li>")
                i += 1
            html_lines.append('</ul>')
            continue

        # Empty line
        if not line.strip():
            flush_paragraph()
            i += 1
            continue

        # Otherwise: paragraph text
        para_buffer.append(line)
        in_para = True
        i += 1

    flush_paragraph()
    return "\n".join(html_lines)


PRINT_CSS = """
@page { size: letter; margin: 0.75in 0.75in 1in 0.75in; }
* { box-sizing: border-box; }
body {
  font-family: Georgia, 'Times New Roman', serif;
  font-size: 11pt;
  line-height: 1.6;
  color: #1a1a2e;
  max-width: 6.5in;
  margin: 0 auto;
  padding: 0.5in;
  background: #fff;
}
.cover {
  text-align: center;
  padding: 1.5in 0 1in;
  page-break-after: always;
}
.cover h1 {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: 32pt;
  line-height: 1.15;
  color: #1a1a2e;
  margin: 0 0 .5em;
  letter-spacing: -.01em;
}
.cover .subtitle {
  font-size: 14pt;
  color: #666;
  font-style: italic;
  margin: 0 0 2em;
}
.cover .author {
  font-size: 11pt;
  color: #c9a84c;
  text-transform: uppercase;
  letter-spacing: .15em;
  margin-top: 3em;
}
.cover .gold-rule {
  width: 80px;
  height: 3px;
  background: #c9a84c;
  margin: 2em auto;
}
h1 {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: 20pt;
  color: #1a1a2e;
  margin: 1em 0 .5em;
  page-break-after: avoid;
}
h2 {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: 16pt;
  color: #1a1a2e;
  margin: 1.4em 0 .4em;
  padding-bottom: .3em;
  border-bottom: 1px solid #e0e0d8;
  page-break-after: avoid;
}
h3 {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: 13pt;
  color: #c9a84c;
  margin: 1.1em 0 .4em;
  page-break-after: avoid;
}
h4 {
  font-size: 11pt;
  color: #1a1a2e;
  margin: 1em 0 .3em;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: .05em;
}
p { margin: 0 0 .8em; orphans: 3; widows: 3; }
strong { color: #1a1a2e; font-weight: 700; }
em { font-style: italic; }
hr {
  border: 0;
  border-top: 1px solid #e0e0d8;
  margin: 1.5em 0;
  page-break-after: avoid;
}
blockquote {
  margin: 1em 0;
  padding: .5em 1em;
  border-left: 3px solid #c9a84c;
  background: #faf7ee;
  font-style: italic;
}
ul { margin: .5em 0 1em 1.25em; padding: 0; }
li { margin: .3em 0; }
a { color: #c9a84c; text-decoration: none; }
.section-break {
  page-break-before: always;
  padding-top: .5in;
}
.section-marker {
  text-align: center;
  font-size: 9pt;
  color: #999;
  text-transform: uppercase;
  letter-spacing: .2em;
  margin: 0 0 .25em;
}
.footer-note {
  text-align: center;
  margin-top: 2em;
  font-size: 9pt;
  color: #999;
  font-style: italic;
}
@media screen {
  body {
    background: #f5f5f0;
    box-shadow: 0 0 20px rgba(0,0,0,.08);
    margin: 2em auto;
    padding: 1in;
  }
  .print-hint {
    position: fixed;
    top: 1em; right: 1em;
    background: #1a1a2e;
    color: #c9a84c;
    padding: .5em 1em;
    border-radius: 4px;
    font-family: -apple-system, system-ui, sans-serif;
    font-size: 10pt;
    z-index: 99;
  }
}
@media print {
  .print-hint { display: none; }
  body { box-shadow: none; padding: 0; }
}
"""


def make_html(title: str, body_html: str, cover_subtitle: str, footer: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{title}</title>
<style>
{PRINT_CSS}
</style>
</head>
<body>
<div class="print-hint">Press ⌘+P → Save as PDF</div>

<div class="cover">
  <h1>{title}</h1>
  <p class="subtitle">{cover_subtitle}</p>
  <div class="gold-rule"></div>
  <p class="author">Michael Burrage<br><span style="font-size:9pt;color:#999;letter-spacing:.1em;">The Way &amp; Truth</span></p>
</div>

{body_html}

<p class="footer-note">{footer}</p>

</body>
</html>
"""


def main():
    raw = SRC.read_text()
    md = strip_front_matter(raw)

    # Find the start of the actual content (after the first ---)
    # Our content has the title and intro at the top — keep it.

    # Build full 30-day guide
    body_full = md_to_html(md)
    full_html = make_html(
        title="30-Day Kingdom Mindset Guide",
        body_html=body_full,
        cover_subtitle="Foundation • Identity • Warfare • Leadership • Integration",
        footer="© 2026 The Way & Truth — Michael Burrage. For personal use only. Not for redistribution. Questions: miburrage@gmail.com",
    )
    full_out = OUT_DIR / "kingdom-mindset-guide.html"
    full_out.write_text(full_html)
    print(f"✓ Wrote {full_out.relative_to(ROOT)} ({len(full_html):,} chars)")

    # Build free 7-day lead magnet — first 7 days only (Foundation section).
    # Split on Day markers, keep header through Day 7's content, stop at "## IDENTITY"
    seven_day_md = md
    # Cut at the start of IDENTITY section
    marker = "## IDENTITY: Days 8"
    idx = seven_day_md.find(marker)
    if idx > 0:
        seven_day_md = seven_day_md[:idx].rstrip()
        # Add a graceful closing for the lead magnet
        seven_day_md += "\n\n---\n\n## Where to Go from Here\n\n"
        seven_day_md += "You've completed the Foundation week. The full 30-Day Kingdom Mindset Guide continues with four more movements:\n\n"
        seven_day_md += "- **Days 8–14: Identity** — Romans 8, Ephesians 1-2. Who you are as a Kingdom citizen.\n"
        seven_day_md += "- **Days 15–21: Warfare** — Ephesians 6. Prayer, fasting, the disciplines that keep you sharp.\n"
        seven_day_md += "- **Days 22–28: Leadership** — Kingdom authority in family, work, and community.\n"
        seven_day_md += "- **Days 29–30: Integration** — Building the daily rhythm.\n\n"
        seven_day_md += "Get the full guide at: **thewayandtruth.com/kingdom-mindset-30-day-guide/**\n\n"
        seven_day_md += "*$27 — one-time, lifetime access, 30-day money-back guarantee.*\n"

    body_7 = md_to_html(seven_day_md)
    seven_html = make_html(
        title="First 7 Days: Free",
        body_html=body_7,
        cover_subtitle="The Foundation Week of the Kingdom Mindset Guide",
        footer="Free preview — full guide at thewayandtruth.com/kingdom-mindset-30-day-guide/",
    )
    seven_out = OUT_DIR / "first-7-days.html"
    seven_out.write_text(seven_html)
    print(f"✓ Wrote {seven_out.relative_to(ROOT)} ({len(seven_html):,} chars)")


if __name__ == "__main__":
    main()
