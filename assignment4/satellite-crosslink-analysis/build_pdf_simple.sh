#!/bin/bash
# Build PDF from markdown - SIMPLE VERSION
# No fancy packages, just clean PDF with sidebar bookmarks

echo "================================================"
echo "Building PDF: Simple & Reliable Version"
echo "================================================"

INPUT="outputs/12_Assignment4_Submission_With_Calculations.md"
OUTPUT="outputs/Assignment4_Submission.pdf"

# Create temporary cleaned version (remove attachment: references)
TEMP_INPUT="/tmp/submission_cleaned.md"
sed 's/attachment:[^)]*/.gif/g' "$INPUT" > "$TEMP_INPUT"

echo ""
echo "Building PDF with sidebar bookmarks..."
echo ""

pandoc "$TEMP_INPUT" \
    --from=markdown \
    --to=pdf \
    --output="$OUTPUT" \
    --pdf-engine=xelatex \
    --toc \
    --toc-depth=3 \
    --number-sections \
    --variable=geometry:margin=1in \
    --variable=fontsize:11pt \
    --variable=linestretch:1.15 \
    --variable=colorlinks:true \
    --variable=linkcolor:blue \
    --variable=urlcolor:blue \
    --variable=mainfont:"Helvetica" \
    --resource-path=outputs \
    --metadata title="SpCE 5400 Assignment 4: Optical vs. RF Crosslinks Trade Study" \
    --metadata author="Jordan Clayton" \
    --metadata date="November 2025" \
    --standalone

# Clean up
rm -f "$TEMP_INPUT"

if [ $? -eq 0 ]; then
    echo ""
    echo "================================================"
    echo "✓ PDF generated successfully!"
    echo "================================================"
    echo "Location: $OUTPUT"
    echo ""
    echo "Features:"
    echo "  ✓ PDF bookmarks (sidebar navigation in PDF readers)"
    echo "  ✓ Clickable table of contents"
    echo "  ✓ Numbered sections  "
    echo "  ✓ Blue hyperlinks"
    echo "  ✓ Professional formatting"
    echo ""
    echo "To view with sidebar:"
    echo "  - Preview: View → Sidebar → Table of Contents"
    echo "  - Acrobat: Click bookmark icon on left"
    echo ""
    echo "Open with: open '$OUTPUT'"
    echo ""
else
    echo ""
    echo "ERROR: PDF generation failed"
    exit 1
fi
