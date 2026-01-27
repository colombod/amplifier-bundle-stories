# PowerPoint Slide Templates

Reusable HTML templates for creating PowerPoint presentations in the "Useful Apple Keynote" style.

## Available Templates

### 1. slide-title.html
Title slide with centered content.

**Use for:**
- Opening slide
- Section covers

**Elements:**
- Section label (14pt, blue, uppercase)
- Large headline (72pt, white, bold)
- Subtitle (32pt, white 70%)
- Date/metadata (16pt, white 50%)

### 2. slide-content.html
Standard content slide with bullets.

**Use for:**
- Main content slides
- Feature lists
- Key points

**Elements:**
- Section label (14pt, blue)
- Slide heading (48pt, white, bold)
- Bulleted list (24pt, generous spacing)

### 3. slide-code.html
Code example slide with syntax highlighting.

**Use for:**
- Code examples
- Command demonstrations
- Configuration snippets

**Elements:**
- Section label
- Heading
- Code block (green text, dark background, preserves whitespace)

### 4. slide-comparison.html
Two-column comparison layout.

**Use for:**
- Before/After comparisons
- Feature comparisons
- Pros/Cons

**Elements:**
- Heading
- Two equal columns with card backgrounds
- Column titles in blue
- Lists in each column

### 5. slide-metrics.html
Big numbers and metrics display.

**Use for:**
- Impact slides
- Statistics
- Key metrics

**Elements:**
- Heading
- 3-column grid
- Large gradient numbers (72pt+)
- Metric labels below

### 6. slide-cards.html
Feature grid with cards.

**Use for:**
- Feature overviews
- Capability grids
- Multi-item displays

**Elements:**
- Heading
- 3-column card grid
- Card titles (blue)
- Card descriptions

### 7. slide-section.html
Section divider with large number.

**Use for:**
- Separating major sections
- Chapter breaks

**Elements:**
- Large gradient number (120pt)
- Section title (56pt)

## How to Use

1. **Copy template** to `workspace/pptx/html-slides/`
2. **Rename** to match slide number: `slide-01.html`, `slide-02.html`, etc.
3. **Edit content** - replace placeholder text with actual content
4. **Maintain styling** - don't change CSS, only content in `<body>`
5. **Create conversion script** that processes all HTML files with html2pptx
6. **Generate thumbnails** for validation

## Style Consistency

All templates follow the Amplifier Keynote aesthetic:
- Black backgrounds (#000)
- Blue accents (#0A84FF)
- White text with varying opacity
- Green code (#98D4A0)
- Generous spacing and clean typography
- Proper whitespace preservation in code blocks

## Reference

See `context/powerpoint-template.md` for complete style specifications.
