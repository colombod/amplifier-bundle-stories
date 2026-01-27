# PDF Templates

Reusable Python templates for creating PDF documents in the Amplifier Keynote style.

## Available Templates

### one-pager-template.py
Executive one-page summary with key points and metrics.

**Features:**
- Bold blue headline
- Key points section (max 4 bullets)
- Metrics grid (up to 6 metrics in 3x2 layout)
- Clean single-page layout
- Professional footer

**Usage:**
```python
from one_pager_template import create_one_pager

key_points = [
    'Dramatically reduces development time',
    'Increases code reusability',
    'Improves security',
]

metrics = [
    ('1,500→0', 'Lines Saved'),
    ('60%', 'Less YAML'),
    ('50+', 'Security Effects'),
]

create_one_pager(
    'Feature Name',
    'One-line description',
    key_points,
    metrics,
    'output.pdf'
)
```

## Style Guide

### Typography
- Title: Helvetica-Bold, 36pt
- Subtitle: Helvetica, 14pt
- Section headers: Helvetica-Bold, 12pt
- Body text: Helvetica, 11pt
- Metric numbers: Helvetica-Bold, 24pt
- Metric labels: Helvetica, 9pt

### Colors
- Blue: #0A84FF (headlines, numbers)
- Black: #000000 (body text, headers)
- Gray: #595959 (subtitles, labels)
- Light Gray: #F3F2F1 (dividers, boxes)

### Layout
- Margins: 1 inch all sides
- Section spacing: 0.5 inch
- Metric boxes: Grid layout with borders
- Horizontal dividers: 2pt line

## Dependencies

```bash
pip install reportlab pypdf pdfplumber
```

## Workflow

1. Import template
2. Provide data (title, points, metrics)
3. Generate PDF to `workspace/pdf/output/`
4. Auto-open: `open workspace/pdf/output/filename.pdf`
