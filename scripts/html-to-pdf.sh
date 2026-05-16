#!/usr/bin/env bash
# Convert the product HTML files to PDF using headless Chrome (if available).
# Falls back to opening them in your browser for manual Cmd+P → Save as PDF.
#
# Usage: ./scripts/html-to-pdf.sh

set -e

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC_DIR="$ROOT/assets/products"
OUT_DIR="$ROOT/assets/products"

CHROME=""
if [ -x "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" ]; then
  CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
elif [ -x "/Applications/Chromium.app/Contents/MacOS/Chromium" ]; then
  CHROME="/Applications/Chromium.app/Contents/MacOS/Chromium"
elif command -v chromium >/dev/null 2>&1; then
  CHROME="$(command -v chromium)"
elif command -v google-chrome >/dev/null 2>&1; then
  CHROME="$(command -v google-chrome)"
fi

convert_one() {
  local html="$1"
  local pdf="${html%.html}.pdf"
  local name="$(basename "$html")"

  if [ -n "$CHROME" ]; then
    echo "  Converting $name → $(basename "$pdf")"
    "$CHROME" \
      --headless \
      --disable-gpu \
      --no-pdf-header-footer \
      --print-to-pdf="$pdf" \
      "file://$html" >/dev/null 2>&1
    echo "  ✓ $(basename "$pdf")"
  else
    echo "  Chrome not found — opening $name in default browser"
    echo "  Press ⌘+P in the browser, then choose Save as PDF"
    open "$html"
  fi
}

echo "Building product PDFs from HTML sources..."
echo

for html in "$SRC_DIR"/kingdom-mindset-guide.html "$SRC_DIR"/first-7-days.html; do
  if [ -f "$html" ]; then
    convert_one "$html"
  else
    echo "  ✗ Missing: $html"
    echo "    Run scripts/build-product-pdfs.py first."
  fi
done

echo
echo "Done. PDFs (or print dialogs) ready in $OUT_DIR"
echo "These files are excluded from the public Jekyll build."
echo "Upload kingdom-mindset-guide.pdf to Gumroad as your \$27 product."
echo "Upload first-7-days.pdf to your email service for the lead magnet delivery."
