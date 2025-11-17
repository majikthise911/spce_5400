#!/bin/bash
# Build PDF from markdown using Pandoc
# Creates professional PDF with sidebar navigation (bookmarks)

echo "================================================"
echo "Building PDF: Optical vs RF Crosslinks Analysis"
echo "================================================"

# Check if pandoc is installed
if ! command -v pandoc &> /dev/null; then
    echo "ERROR: pandoc is not installed"
    echo "Install with: brew install pandoc"
    exit 1
fi

# Check if LaTeX is installed (needed for PDF generation)
if ! command -v pdflatex &> /dev/null; then
    echo "ERROR: LaTeX is not installed"
    echo "Install with: brew install --cask mactex-no-gui"
    echo "Or full MacTeX: brew install --cask mactex"
    exit 1
fi

# Input and output files
INPUT="outputs/12_Assignment4_Submission_With_Calculations.md"
OUTPUT="outputs/Assignment4_Submission_Optical_vs_RF_Crosslinks.pdf"
METADATA="pdf_metadata.yaml"

echo ""
echo "Input:  $INPUT"
echo "Output: $OUTPUT"
echo ""

# Build PDF with pandoc
pandoc "$INPUT" \
    --metadata-file="$METADATA" \
    --from=markdown \
    --to=pdf \
    --output="$OUTPUT" \
    --pdf-engine=xelatex \
    --toc \
    --toc-depth=3 \
    --number-sections \
    --highlight-style=tango \
    --variable=geometry:margin=1in \
    --variable=fontsize:11pt \
    --variable=linestretch:1.2 \
    --variable=colorlinks:true \
    --variable=linkcolor:blue \
    --variable=urlcolor:blue \
    --variable=toccolor:black \
    --resource-path=outputs \
    --standalone

if [ $? -eq 0 ]; then
    echo ""
    echo "================================================"
    echo "✓ PDF generated successfully!"
    echo "================================================"
    echo "Location: $OUTPUT"
    echo ""
    echo "Features:"
    echo "  ✓ Clickable table of contents"
    echo "  ✓ PDF bookmarks (sidebar navigation)"
    echo "  ✓ Numbered sections"
    echo "  ✓ Syntax-highlighted formulas"
    echo "  ✓ Embedded figures"
    echo ""
    echo "Open with: open '$OUTPUT'"
    echo ""
else
    echo ""
    echo "ERROR: PDF generation failed"
    echo "Check the error messages above"
    exit 1
fi
