# Excel Templates

Reusable Python templates for creating Excel workbooks in the Amplifier Keynote style.

## Available Templates

### dashboard-template.py
Complete dashboard with header, metrics section, and instructions sheet.

**Features:**
- Black header with blue accents
- Metrics table with formulas
- Status indicators (✓, ↓, →)
- Professional number formatting
- Instructions sheet

**Usage:**
```python
from dashboard_template import create_dashboard

metrics = {
    'Active Users': 150,
    'Features Shipped': 45,
    'Code Generated': 125000,
}

create_dashboard('output.xlsx', 'Dashboard Title', metrics)
```

### metrics-template.py
Metrics tracking sheet with trend analysis.

**Features:**
- Before/current/target columns
- Automatic status calculation
- Blue header styling
- Formula-driven improvements

**Usage:**
```python
from metrics_template import create_metrics_sheet

metrics = [
    {'name': 'Users', 'current': 150, 'previous': 120, 'target': 200},
    {'name': 'Features', 'current': 45, 'previous': 40, 'target': 50},
]

wb = Workbook()
create_metrics_sheet(wb, 'Monthly Metrics', metrics)
wb.save('output.xlsx')
```

### comparison-template.py
Before/after comparison table.

**Features:**
- Side-by-side metrics
- Percentage improvement formulas
- Green highlighting for "after" values
- Blue improvement percentages

**Usage:**
```python
from comparison_template import create_comparison_sheet

before = {'Lines of Code': 1500, 'Hours': 40}
after = {'Lines of Code': 0, 'Hours': 2}

wb = Workbook()
create_comparison_sheet(wb, 'Impact Analysis', before, after)
wb.save('output.xlsx')
```

## Style Guide

### Color Palette
```python
COLORS = {
    'blue': '0A84FF',      # Amplifier blue for accents
    'green': '30D158',     # Success/positive
    'orange': 'FF9F0A',    # Warning/attention
    'gray_light': 'F3F2F1', # Backgrounds
    'black': '000000',     # Text
}
```

### Typography
- Headers: Arial, 16pt, bold, blue
- Section labels: Arial, 11pt, bold, black on gray background
- Data: Arial, 10pt
- Emphasis: Bold blue for important numbers

### Number Formatting
- Use `#,##0` for whole numbers
- Use `#,##0.0` for decimals
- Use `-` for zeros: `#,##0;(#,##0);-`
- Percentages: `0.0%`

### Formulas
Always use Excel formulas, not hardcoded calculations:
```python
# Good
ws['C4'] = '=B4-B3'

# Bad
ws['C4'] = calculated_value
```

## Validation

After creating any Excel file with formulas:

```bash
python ~/dev/anthropic-skills/skills/xlsx/recalc.py output.xlsx
```

Must return zero errors before presenting to user.

## Dependencies

```bash
pip install openpyxl pandas
brew install libreoffice  # For formula recalculation
```
