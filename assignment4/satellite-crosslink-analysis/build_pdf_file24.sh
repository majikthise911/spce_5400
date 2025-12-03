#!/bin/bash
# Build PDF from File 24 (Concise Version)

echo "================================================"
echo "Building PDF from File 24 (Concise Version)"
echo "================================================"

INPUT="outputs/24_Assignment4_Submission_With_Calculations_Concise.md"
OUTPUT="outputs/Assignment4_Concise_FINAL.pdf"

echo ""
echo "Input:  $INPUT"
echo "Output: $OUTPUT"
echo ""

# Create temporary cleaned version (remove any attachment: references just in case)
TEMP_INPUT="/tmp/submission_24_cleaned.md"
sed 's/attachment:[^)]*/.gif/g' "$INPUT" > "$TEMP_INPUT"

echo "Building PDF..."
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
    --metadata title="Optical vs. RF Crosslinks Trade Study" \
    --metadata subtitle="LEO Satellite Constellation Communication Analysis (Concise Version)" \
    --metadata author="Jordan Clayton" \
    --metadata date="November 2025" \
    --metadata course="SpCE 5400 - Assignment 4" \
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
    echo "  ✓ PDF bookmarks (sidebar navigation)"
    echo "  ✓ Clickable table of contents"
    echo "  ✓ Numbered sections"
    echo "  ✓ Blue hyperlinks"
    echo "  ✓ Embedded figures (including Gaussian beam image)"
    echo ""
    echo "To view with sidebar:"
    echo "  Preview: View → Sidebar → Table of Contents"
    echo "  Acrobat: Click bookmark icon on left"
    echo ""
    echo "Open with: open '$OUTPUT'"
    echo ""
else
    echo ""
    echo "ERROR: PDF generation failed"
    exit 1
fi
