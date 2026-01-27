# Word Document Templates

Reusable JavaScript templates for creating Word documents in the Amplifier Keynote style.

## Available Templates

### technical-doc-template.js
Complete technical documentation with table of contents.

**Features:**
- Professional title and description
- Auto-generated table of contents
- Hierarchical section structure
- Code blocks with syntax highlighting
- Clean typography and spacing

**Usage:**
```javascript
const { createTechnicalDoc } = require('./technical-doc-template');
const { Packer } = require('docx');
const fs = require('fs');

const doc = createTechnicalDoc(
  'Amplifier Recipe System',
  'Complete guide to multi-step AI agent orchestration'
);

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync('technical-guide.docx', buffer);
});
```

**Structure:**
- Title (32pt, blue)
- Description (12pt, gray)
- Table of Contents
- Overview section
- Architecture section
- Code examples

### proposal-template.js
Feature proposal with standard sections.

**Features:**
- Executive summary
- Problem statement
- Proposed solution
- Implementation phases
- Success metrics

**Usage:**
```javascript
const { createProposal } = require('./proposal-template');

const doc = createProposal(
  'Shadow Environments',
  'Safe testing of local changes before pushing to production'
);
```

**Structure:**
- Title
- Executive Summary
- Problem
- Proposed Solution
- Implementation (phases)
- Success Metrics

### case-study-template.js
Case study with Challenge/Solution/Results narrative.

**Features:**
- Clean narrative structure
- Challenge/Solution/Results sections
- Key takeaways section
- Professional formatting

**Usage:**
```javascript
const { createCaseStudy } = require('./case-study-template');

const doc = createCaseStudy(
  'Cortex: Built with Amplifier',
  'Challenge description...',
  'Solution description...',
  'Results and impact...'
);
```

**Structure:**
- Title
- The Challenge
- The Solution
- The Results
- Key Takeaways

## Style Guide

### Typography
- Title: 28pt, bold
- Heading 1: 20pt, bold, ALL CAPS
- Heading 2: 16pt, bold
- Body: 11pt, regular
- Code: 10pt, Courier New

### Colors
- Title: Blue (#0A84FF)
- Headings: Black
- Body: Black
- Code: Green (#98D4A0) or black
- Emphasis: Blue

### Spacing
- After title: 400 units
- After headings: 200 units
- After paragraphs: 200 units
- Between bullets: 100 units

## Dependencies

```bash
npm install -g docx
```

## Workflow

1. Import template
2. Modify with actual content
3. Export to .docx using Packer
4. Save to `workspace/docx/output/`
5. Auto-open: `open workspace/docx/output/filename.docx`
