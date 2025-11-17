#!/bin/bash
# Build ENHANCED PDF using Eisvogel template
# Creates publication-quality PDF with beautiful formatting

echo "========================================================"
echo "Building ENHANCED PDF with Eisvogel Template"
echo "========================================================"

# Check if Eisvogel template exists
TEMPLATE_DIR="$HOME/.pandoc/templates"
TEMPLATE_FILE="$TEMPLATE_DIR/eisvogel.latex"

if [ ! -f "$TEMPLATE_FILE" ]; then
    echo ""
    echo "Eisvogel template not found. Installing..."
    mkdir -p "$TEMPLATE_DIR"
    curl -o "$TEMPLATE_FILE" \
        https://raw.githubusercontent.com/Wandmalfarbe/pandoc-latex-template/master/eisvogel.tex
    echo "✓ Eisvogel template installed"
fi

# Input and output
INPUT="outputs/12_Assignment4_Submission_With_Calculations.md"
OUTPUT="outputs/Assignment4_Submission_ENHANCED.pdf"

echo ""
echo "Input:  $INPUT"
echo "Output: $OUTPUT"
echo ""
echo "Building enhanced PDF..."
echo ""

# Build with Eisvogel template
pandoc "$INPUT" \
    --from=markdown \
    --to=pdf \
    --output="$OUTPUT" \
    --template=eisvogel \
    --pdf-engine=xelatex \
    --toc \
    --toc-depth=3 \
    --number-sections \
    --listings \
    --shift-heading-level-by=-1 \
    --resource-path=outputs \
    --metadata-file=pdf_metadata.yaml \
    --metadata title="Optical vs. RF Crosslinks Trade Study" \
    --metadata subtitle="LEO Satellite Constellation Communication Analysis" \
    --metadata author="Jordan Clayton" \
    --metadata date="November 2025" \
    --metadata titlepage=true \
    --metadata titlepage-rule-color="360049" \
    --metadata titlepage-background="backgrounds/background1.pdf" \
    --metadata toc-own-page=true \
    --metadata listings-no-page-break=true \
    --metadata code-block-font-size="\small" \
    --metadata table-use-row-colors=true \
    --metadata linkcolor="blue" \
    --metadata urlcolor="blue"

if [ $? -eq 0 ]; then
    echo ""
    echo "========================================================"
    echo "✓ ENHANCED PDF generated successfully!"
    echo "========================================================"
    echo "Location: $OUTPUT"
    echo ""
    echo "Enhanced features:"
    echo "  ✓ Beautiful Eisvogel template styling"
    echo "  ✓ Professional title page"
    echo "  ✓ Clickable table of contents (separate page)"
    echo "  ✓ PDF bookmarks for sidebar navigation"
    echo "  ✓ Color-coded sections and links"
    echo "  ✓ Syntax-highlighted code blocks"
    echo "  ✓ Professional typography"
    echo "  ✓ Numbered equations and sections"
    echo ""
    echo "Open with: open '$OUTPUT'"
    echo ""
else
    echo ""
    echo "ERROR: PDF generation failed"
    echo ""
    echo "Falling back to basic PDF..."
    ./build_pdf.sh
fi
