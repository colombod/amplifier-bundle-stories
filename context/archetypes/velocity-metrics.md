# Story Archetype: Velocity & Metrics

Data-driven narrative showcasing development speed, adoption trends, and quantified impact.

## When to Use

- Quarterly/monthly ecosystem reports
- Adoption tracking and growth stories
- Performance benchmarking
- Development velocity showcases
- ROI and efficiency demonstrations

## Narrative Structure

### Part 1: Context (15%)

**What we're measuring and why**
- Metrics being tracked
- Why these metrics matter
- Time period covered
- Baseline for comparison

**Example:**
"Over the past 90 days, we tracked Amplifier ecosystem activity across 12 repositories and 150+ sessions. These metrics reveal development velocity, feature adoption, and real-world impact on developer productivity."

### Part 2: The Numbers (50%)

**Present the data**
- Key metrics with context
- Trends over time
- Comparisons (before/after, expected/actual)
- Distributions and patterns

**Categories:**
- **Development Velocity:** Commits, PRs, features shipped
- **Adoption:** Users, sessions, downloads
- **Impact:** Time saved, errors prevented, productivity gains
- **Engagement:** Contributors, discussions, stars
- **Quality:** Test coverage, bug rates, performance

**Visualization:**
- Big numbers for key metrics
- Line charts for trends
- Bar charts for comparisons
- Tables for detailed breakdowns

### Part 3: Analysis (25%)

**What the numbers mean**
- Interpret trends
- Identify insights
- Explain anomalies
- Draw conclusions

**Example:**
"The 250% increase in session creation coincides with the launch of recipe workflows. This suggests recipes are driving higher engagement - users are tackling more complex, multi-step projects that require automated orchestration."

### Part 4: Implications (10%)

**So what?**
- What actions should be taken
- What this predicts for the future
- Opportunities identified
- Areas needing attention

**Example:**
"With adoption accelerating, documentation will be critical. We should prioritize tutorial content and onboarding improvements. The data also reveals power users (10+ sessions) who could be great case study subjects."

## Format-Specific Adaptations

### For Excel Dashboard
**Layout:**
```
Sheet 1: Executive Summary
- Top 5 metrics as big numbers
- Week-over-week trend chart
- Key insights (3-4 bullets)

Sheet 2: Development Velocity
- Commits per repo (table + bar chart)
- PR velocity (line chart over time)
- Contributors breakdown
- Lines changed by type

Sheet 3: Adoption Metrics
- Active users trend
- Session creation over time
- Feature usage breakdown
- Geographic distribution (if available)

Sheet 4: Impact Analysis
- Time savings calculations
- Productivity improvements
- Error reduction
- Cost savings

Sheet 5: Raw Data
- All source data for transparency
```

**Templates:**
- `workspace/xlsx/templates/dashboard-template.py`
- `workspace/xlsx/templates/metrics-template.py`

### For PowerPoint (10-15 slides)
**Structure:**
1. **Title** - "Amplifier Ecosystem: Q1 2026 Metrics"
2. **Overview** (1 slide) - Context and time period
3. **Highlights** (1 slide) - Top 3-5 key metrics as big numbers
4. **Development Velocity** (2-3 slides) - Commits, PRs, features
5. **Adoption** (2-3 slides) - Users, sessions, growth trends
6. **Impact** (2-3 slides) - Time saved, productivity, ROI
7. **Insights** (1-2 slides) - What we learned
8. **Next Steps** (1 slide) - Actions and focus areas

**Templates:**
- `workspace/pptx/templates/slide-metrics.html` - Big numbers
- `workspace/pptx/templates/slide-big-number.html` - Single key metric
- Charts exported as PNG and inserted

### For Blog Post (800-1000 words)
**Structure:**
- **Hook** (100 words) - Interesting trend or number
- **Overview** (150 words) - What we measured
- **Key Metrics** (400 words) - The numbers with analysis
- **Insights** (200 words) - What it means
- **Conclusion** (150 words) - Looking ahead

**Style:**
- Data-driven but accessible
- Charts/graphs as images
- Highlight surprising findings
- Make trends obvious

## Metrics Taxonomy

### Development Velocity Metrics
```
Commits:
- Total commits
- Commits per repo
- Commits per contributor
- Commit frequency (commits/week)
- Semantic breakdown (feat/fix/chore %)

Pull Requests:
- PRs opened
- PRs merged
- PR velocity (open → merge time)
- PR size distribution

Features:
- Features shipped
- Features in progress
- Feature development time
- Feature adoption rate
```

### Adoption Metrics
```
Users:
- Active users (by period)
- New users
- Power users (>10 sessions)
- User retention rate

Sessions:
- Total sessions
- Sessions per user
- Session duration avg/median
- Session complexity (tool calls, agents)

Engagement:
- GitHub stars/forks
- Discord activity
- Discussion participation
- Documentation page views
```

### Impact Metrics
```
Productivity:
- Time saved per session
- Code generated (lines)
- Tasks automated
- Iterations reduced

Quality:
- Errors prevented
- Test coverage improvements
- Bug fix rate
- Performance improvements

Efficiency:
- Resource utilization
- Cost per session
- Token efficiency
- Time to value
```

## Visualization Best Practices

### Big Numbers
Use for single key metrics:
```
  3,000
  ──────
Features Generated
```

Show as gradient blue numbers (180pt) on metric slides.

### Trend Lines
Show change over time:
```
Sessions Created Over Time

500 ┤        ╭──
400 ┤     ╭──╯
300 ┤  ╭──╯
200 ┤──╯
    └──────────────
   W1  W2  W3  W4
```

Use line charts in Excel or PowerPoint.

### Comparisons
Show before/after or comparative data:
```
Development Time

Before: ████████████ 3 weeks
After:  ██ 2 days
```

Use bar charts or comparison slides.

### Distributions
Show how things break down:
```
Agent Usage Distribution

explorer:        ████████████ 35%
modular-builder: ████████ 25%
zen-architect:   ██████ 18%
bug-hunter:      ████ 12%
other:           ███ 10%
```

Use pie charts or horizontal bar charts.

## Storytelling with Data

### Find the Story in the Numbers
Numbers alone aren't stories. Look for:
- **Surprising trends:** "Adoption tripled after X"
- **Unexpected patterns:** "80% of sessions use Y"
- **Inflection points:** "Growth accelerated in week 3"
- **Anomalies:** "February had unusual spike because..."

### Contextualize Everything
```markdown
# Weak
"45 commits last week"

# Strong
"45 commits last week - up 125% from our 20/week average.
The spike came from 3 major feature pushes (Shadow, Recipes, Surface),
all shipping in the same week."
```

### Highlight What Matters
Don't bury the lede:
```markdown
# Buried lede
"We had various metrics this quarter including sessions, commits, and
users. There were 3,000 code generation events, which was significant."

# Clear lead
"3,000 code generation events this quarter - that's 125,000 lines of
AI-generated code helping developers build faster. Up 250% from last quarter."
```

## Templates to Use

### Excel Metrics Dashboards
```python
from templates.dashboard_template import create_dashboard
from templates.metrics_template import create_metrics_sheet

# Main dashboard
metrics = {
    'Sessions Created': 450,
    'Active Users': 150,
    'Code Generated (lines)': 125000,
    'Features Shipped': 45,
}

create_dashboard('ecosystem-metrics.xlsx', 'Q1 2026 Metrics', metrics)

# Add trend sheet
trends = [
    {'name': 'Week 1', 'current': 100, 'previous': 80, 'target': 120},
    {'name': 'Week 2', 'current': 135, 'previous': 100, 'target': 140},
    {'name': 'Week 3', 'current': 180, 'previous': 135, 'target': 160},
]

# Use openpyxl to create the workbook first
wb = openpyxl.Workbook()
create_metrics_sheet(wb, 'Weekly Trends', trends)
```

### PowerPoint Metrics Presentations
Focus on visual impact:
- One key metric per slide
- Use gradient numbers for impact
- Charts as background or featured elements
- Minimal text, maximum data

## Checklist

Before publishing velocity/metrics content:
- [ ] All numbers are accurate and sourced
- [ ] Trends are correctly calculated
- [ ] Comparisons have proper baselines
- [ ] Insights are backed by data
- [ ] Anomalies are explained
- [ ] Visualizations are clear and accurate
- [ ] Context provided for all metrics
- [ ] Implications are actionable

## Success Criteria

Velocity/metrics story succeeds when:
- Key trends are immediately obvious
- Numbers tell a compelling story
- Insights are surprising or valuable
- Data drives action or decisions
- Visualizations are professional and clear

---

**Reference:** Use this archetype for quarterly reports, weekly digests (metrics section), and adoption tracking.
