/**
 * Word Technical Document Template - Amplifier Stories Style
 * 
 * Creates a professional technical document with:
 * - Clean hierarchy and table of contents
 * - Code blocks with syntax highlighting
 * - Professional section headers
 * - Consistent spacing and typography
 * 
 * Usage:
 *   node technical-doc-template.js "Document Title" "Description"
 */

const { Document, Paragraph, TextRun, HeadingLevel, TableOfContents, AlignmentType } = require('docx');
const fs = require('fs');

// Amplifier Keynote Color Palette (Word RGB format: RRGGBB)
const COLORS = {
  blue: '0A84FF',
  black: '000000',
  gray: '595959',
  code_green: '98D4A0',
};

function createTechnicalDoc(title, description) {
  const doc = new Document({
    sections: [{
      properties: {},
      children: [
        // Title
        new Paragraph({
          text: title,
          heading: HeadingLevel.TITLE,
          alignment: AlignmentType.LEFT,
          spacing: { after: 200 },
          style: {
            font: { name: 'Arial', size: 32, bold: true, color: COLORS.blue },
          },
        }),
        
        // Description
        new Paragraph({
          text: description,
          spacing: { after: 400 },
          style: {
            font: { name: 'Arial', size: 12, color: COLORS.gray },
          },
        }),
        
        // Table of Contents
        new Paragraph({
          text: 'Table of Contents',
          heading: HeadingLevel.HEADING_1,
          spacing: { before: 200, after: 200 },
        }),
        new TableOfContents('Contents', {
          hyperlink: true,
          headingStyleRange: '1-3',
        }),
        
        // Section 1
        new Paragraph({
          text: 'Overview',
          heading: HeadingLevel.HEADING_1,
          spacing: { before: 400, after: 200 },
        }),
        
        new Paragraph({
          text: 'This section provides an overview of the feature or system.',
          spacing: { after: 200 },
        }),
        
        // Section 2
        new Paragraph({
          text: 'Architecture',
          heading: HeadingLevel.HEADING_1,
          spacing: { before: 400, after: 200 },
        }),
        
        new Paragraph({
          text: 'Technical architecture details go here.',
          spacing: { after: 200 },
        }),
        
        // Code example
        new Paragraph({
          text: 'Example Usage',
          heading: HeadingLevel.HEADING_2,
          spacing: { before: 200, after: 200 },
        }),
        
        new Paragraph({
          children: [
            new TextRun({
              text: '# Example code\ncommand --flag value\noutput result',
              font: { name: 'Courier New', size: 10 },
              color: COLORS.code_green,
            }),
          ],
          spacing: { after: 200 },
          style: { shading: { fill: 'F3F2F1' } },
        }),
      ],
    }],
  });
  
  return doc;
}

module.exports = { createTechnicalDoc };
