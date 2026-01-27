/**
 * Word Case Study Template - Amplifier Stories Style
 * 
 * Creates a professional case study with:
 * - Challenge/Solution/Results structure
 * - Quote boxes
 * - Metrics highlights
 * - Clean narrative flow
 * 
 * Usage:
 *   const { createCaseStudy } = require('./case-study-template');
 *   const doc = createCaseStudy(title, challenge, solution, results);
 */

const { Document, Paragraph, TextRun, HeadingLevel, AlignmentType, Table, TableRow, TableCell, WidthType } = require('docx');

function createCaseStudy(title, challenge, solution, results) {
  const doc = new Document({
    sections: [{
      properties: {},
      children: [
        // Title
        new Paragraph({
          text: title,
          heading: HeadingLevel.TITLE,
          alignment: AlignmentType.LEFT,
          spacing: { after: 400 },
        }),
        
        // Challenge
        new Paragraph({
          text: 'THE CHALLENGE',
          heading: HeadingLevel.HEADING_1,
          spacing: { before: 200, after: 200 },
        }),
        
        new Paragraph({
          text: challenge,
          spacing: { after: 400 },
        }),
        
        // Solution
        new Paragraph({
          text: 'THE SOLUTION',
          heading: HeadingLevel.HEADING_1,
          spacing: { before: 200, after: 200 },
        }),
        
        new Paragraph({
          text: solution,
          spacing: { after: 400 },
        }),
        
        // Results
        new Paragraph({
          text: 'THE RESULTS',
          heading: HeadingLevel.HEADING_1,
          spacing: { before: 200, after: 200 },
        }),
        
        new Paragraph({
          text: results,
          spacing: { after: 400 },
        }),
        
        // Key Takeaways
        new Paragraph({
          text: 'KEY TAKEAWAYS',
          heading: HeadingLevel.HEADING_1,
          spacing: { before: 200, after: 200 },
        }),
        
        new Paragraph({
          text: '• Takeaway point one',
          spacing: { after: 100 },
        }),
        
        new Paragraph({
          text: '• Takeaway point two',
          spacing: { after: 100 },
        }),
        
        new Paragraph({
          text: '• Takeaway point three',
          spacing: { after: 100 },
        }),
      ],
    }],
  });
  
  return doc;
}

module.exports = { createCaseStudy };
