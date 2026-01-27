# PowerPoint Workspace

This directory is used for creating PowerPoint presentations using the html2pptx workflow.

## Directory Structure

```
pptx-workspace/
├── html-slides/     # HTML files for each slide (temporary)
├── assets/          # Images, icons, charts (PNG/JPEG from Sharp)
├── output/          # Final .pptx files go here
├── thumbnails/      # Thumbnail previews for validation
└── README.md        # This file
```

## Workflow

When creating a PowerPoint presentation:

1. **HTML Slides** → Write to `html-slides/` directory
   - One HTML file per slide: `slide-01.html`, `slide-02.html`, etc.
   - Use proper dimensions (720pt × 405pt for 16:9)
   - Follow html2pptx.md guidelines

2. **Assets** → Generate and save to `assets/` directory
   - Rasterize gradients/icons to PNG using Sharp
   - Save chart images, background images
   - Reference from HTML: `../assets/filename.png`

3. **Conversion Script** → Create JavaScript file in workspace root
   - Import html2pptx library
   - Process each HTML slide
   - Add charts/tables to placeholders
   - Save to `output/presentation-name.pptx`

4. **Validation** → Generate thumbnails to `thumbnails/`
   - Create thumbnail grid for visual inspection
   - Verify layout, text positioning, contrast
   - Fix issues and regenerate if needed

5. **Final Output** → Copy approved .pptx from `output/` to `docs/`
   - Keep final presentations in `docs/` for deployment
   - Workspace files can be cleaned up after approval

## File Naming Convention

- HTML slides: `slide-01.html`, `slide-02.html`, etc.
- Assets: `gradient-bg.png`, `chart-velocity.png`, etc.
- Scripts: `create-presentation.js`
- Output: `feature-name-presentation.pptx`

## Cleanup

After a presentation is approved and moved to `docs/`:
- Keep the .pptx in `output/` for reference
- Archive or delete html-slides/ and assets/ to save space
- Keep conversion script for future reference/updates

## Dependencies

Required Node.js packages (install globally):
- pptxgenjs
- playwright
- sharp
- react-icons, react, react-dom

Required Python packages:
- markitdown (for text extraction)
- defusedxml (for OOXML validation)
- Pillow (for thumbnail generation)

See `~/dev/anthropic-skills/skills/pptx/SKILL.md` for complete dependency list.
