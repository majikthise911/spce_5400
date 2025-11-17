# Building Professional PDFs from Your Submission

You have **two options** for creating beautiful PDFs with sidebar navigation:

## ✅ Prerequisites (Already Installed!)
- ✓ Pandoc 3.8.2.1
- ✓ XeLaTeX (from MacTeX)

---

## Option 1: Basic Professional PDF (Recommended to start)

**Simple, clean, professional formatting**

```bash
./build_pdf.sh
```

**Output:** `outputs/Assignment4_Submission_Optical_vs_RF_Crosslinks.pdf`

**Features:**
- Clean academic paper formatting
- Clickable table of contents (3 levels deep)
- PDF bookmarks (shows as sidebar in PDF readers)
- Numbered sections
- Syntax-highlighted formulas
- Embedded figures
- Headers with assignment info
- Page numbers

**When to use:** Quick build, submission-ready format

---

## Option 2: Enhanced PDF with Eisvogel Template (BEAUTIFUL!)

**Publication-quality, magazine-style formatting**

```bash
./build_pdf_enhanced.sh
```

**Output:** `outputs/Assignment4_Submission_ENHANCED.pdf`

**Features:**
- ✨ Gorgeous Eisvogel template (used in academic publications)
- ✨ Professional title page with color accent
- ✨ Separate TOC page with better formatting
- ✨ Color-coded section headers
- ✨ Better table formatting (alternating row colors)
- ✨ Enhanced code block styling
- ✨ Improved typography and spacing
- ✨ Professional footer with page numbers
- ✨ PDF bookmarks for sidebar navigation

**When to use:** Final submission, presentations, portfolio piece

**Note:** First run will auto-download the Eisvogel template (~2MB)

---

## The "Sidebar" Feature

Both PDFs include **PDF bookmarks** which appear as a **sidebar/navigation pane** when opened in:
- Adobe Acrobat Reader
- macOS Preview (View → Sidebar → Table of Contents)
- Chrome PDF viewer
- Firefox PDF viewer

This gives you clickable navigation through all sections!

---

## Quick Start

**Try the basic version first:**
```bash
./build_pdf.sh
open outputs/Assignment4_Submission_Optical_vs_RF_Crosslinks.pdf
```

**Then try the enhanced version:**
```bash
./build_pdf_enhanced.sh
open outputs/Assignment4_Submission_ENHANCED.pdf
```

**Compare them and choose which you prefer!**

---

## Customization

### Change metadata (title, author, date):
Edit `pdf_metadata.yaml`

### Change PDF styling:
- **Basic:** Edit variables in `build_pdf.sh` (margins, font size, etc.)
- **Enhanced:** Edit metadata flags in `build_pdf_enhanced.sh`

### Add figures to the document:
Already configured! Just ensure figure paths in markdown are relative to `outputs/`:
```markdown
![Link Margin Comparison](figures/01_link_margin_comparison.png)
```

---

## Troubleshooting

**PDF opens but no sidebar?**
- In Preview: View → Sidebar → Show Sidebar, then click Table of Contents tab
- In Acrobat: Click bookmark icon on left side

**Build fails with LaTeX error?**
- Check that all figure paths are correct
- Ensure no special characters in section headings
- Try basic version first to isolate issues

**Figures not showing?**
- Make sure `--resource-path=outputs` is set (already done)
- Check figure paths are relative to outputs directory

---

## Tips for Best Results

1. **Before building:** Ensure all your plots are generated:
   ```bash
   python3 generate_plots.py
   ```

2. **Add figure captions** in your markdown:
   ```markdown
   ![Link Margin Comparison showing 9× advantage](figures/01_link_margin_comparison.png)
   *Figure 1: Link margin comparison between optical and RF crosslinks*
   ```

3. **Keep equations in code blocks** for proper formatting:
   ````markdown
   ```
   P_rx = P_tx × G_tx × G_rx × L_fs
   ```
   ````

4. **Use the enhanced version** for final submission - it looks amazing!

---

## What You Get

### Basic PDF:
- Professional but simple
- Fast to build (~10 seconds)
- Easy to troubleshoot
- Great for quick reviews

### Enhanced PDF:
- Publication-quality
- Slower to build (~20-30 seconds)
- Worth it for final submission
- Impressive visual impact

**Both have the sidebar navigation you wanted!**
