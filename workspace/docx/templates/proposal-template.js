/**
 * Word Proposal Template - Amplifier Stories Style
 * 
 * Creates a professional feature proposal with:
 * - Executive summary
 * - Problem statement
 * - Proposed solution
 * - Implementation plan
 * - Success metrics
 * 
 * Usage:
 *   const { createProposal } = require('./proposal-template');
 *   const doc = createProposal("Feature Name", "Executive Summary");
 */

const { Document, Paragraph, TextRun, HeadingLevel, AlignmentType, BorderStyle } = require('docx');

const COLORS = {
  blue: '0A84FF',
  black: '000000',
  gray: '595959',
};

function createProposal(featureName, executiveSummary) {
  const doc = new Document({
    sections: [{
      properties: {},
      children: [
        // Title
        new Paragraph({
          text: featureName,
          heading: HeadingLevel.TITLE,
          alignment: AlignmentType.LEFT,
          spacing: { after: 400 },
        }),
        
        // Executive Summary
        new Paragraph({
          text: 'EXECUTIVE SUMMARY',
          heading: HeadingLevel.HEADING_1,
          spacing: { before: 200, after: 200 },
        }),
        
        new Paragraph({
          text: executiveSummary,
          spacing: { after: 400 },
        }),
        
        // Problem Statement
        new Paragraph({
          text: 'PROBLEM',
          heading: HeadingLevel.HEADING_1,
          spacing: { before: 200, after: 200 },
        }),
        
        new Paragraph({
          text: 'Describe the problem this feature solves.',
          spacing: { after: 200 },
        }),
        
        // Proposed Solution
        new Paragraph({
          text: 'PROPOSED SOLUTION',
          heading: HeadingLevel.HEADING_1,
          spacing: { before: 200, after: 200 },
        }),
        
        new Paragraph({
          text: 'Describe the proposed solution.',
          spacing: { after: 200 },
        }),
        
        // Implementation Plan
        new Paragraph({
          text: 'IMPLEMENTATION',
          heading: HeadingLevel.HEADING_1,
          spacing: { before: 200, after: 200 },
        }),
        
        new Paragraph({
          text: 'Phase 1: Planning and design',
          spacing: { after: 100 },
        }),
        
        new Paragraph({
          text: 'Phase 2: Core implementation',
          spacing: { after: 100 },
        }),
        
        new Paragraph({
          text: 'Phase 3: Testing and rollout',
          spacing: { after: 400 },
        }),
        
        // Success Metrics
        new Paragraph({
          text: 'SUCCESS METRICS',
          heading: HeadingLevel.HEADING_1,
          spacing: { before: 200, after: 200 },
        }),
        
        new Paragraph({
          text: '• Metric 1: Target value',
          spacing: { after: 100 },
        }),
        
        new Paragraph({
          text: '• Metric 2: Target value',
          spacing: { after: 100 },
        }),
      ],
    }],
  });
  
  return doc;
}

module.exports = { createProposal };
