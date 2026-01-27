# Presentation Styles

Two remembered styles for different use cases.

## Useful Apple Keynote (Preferred)

Higher information density while maintaining polish. Use for most decks.

**Characteristics:**
- Black backgrounds (#000)
- Clean sans-serif typography (SF Pro Display, Segoe UI, system fonts)
- Section labels: 14px uppercase, accent color, letter-spacing: 2px
- Headlines: 48-72px, font-weight 600-700, letter-spacing: -1px to -2px
- Cards with titles and descriptions for feature grids
- Code blocks with syntax highlighting (green for code, gray for comments)
- Comparison tables and before/after layouts
- Flow diagrams with colored step boxes
- Velocity/stats grids near the end
- Navigation dots at bottom center
- Slide counter at bottom right

**CSS Essentials (Responsive):**

See `context/responsive-design.md` for complete responsive guidelines.

```css
:root {
    /* Fluid typography - scales with viewport */
    --font-headline: clamp(32px, 8vw, 72px);
    --font-medium-headline: clamp(24px, 5vw, 48px);
    --font-subhead: clamp(16px, 3vw, 32px);
    --font-big-number: clamp(60px, 20vw, 180px);
    
    /* Fluid spacing */
    --padding-slide: clamp(20px, 5vw, 80px);
    --gap-grid: clamp(16px, 3vw, 40px);
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Segoe UI', Roboto, sans-serif;
    background: #000;
    color: #fff;
    overflow: hidden;
    overscroll-behavior: none;
}

.slide {
    min-height: 100vh;
    min-height: 100dvh; /* Dynamic viewport for mobile */
    padding: var(--padding-slide);
    overflow-y: auto;
    overflow-x: hidden;
}

.section-label {
    font-size: clamp(12px, 1.5vw, 14px);
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 2px;
    color: var(--accent-color, #0A84FF);
}

.headline {
    font-size: var(--font-headline);
    font-weight: 700;
    letter-spacing: clamp(-1px, -0.03em, -2px);
    line-height: 1.1;
}

.big-number {
    font-size: var(--font-big-number);
}

/* Responsive grids - collapse on mobile */
.thirds, .split {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(min(280px, 100%), 1fr));
    gap: var(--gap-grid);
}

.card {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: clamp(12px, 2vw, 16px);
    padding: clamp(16px, 4vw, 28px);
}

.code-block {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 12px;
    padding: clamp(12px, 3vw, 20px) clamp(16px, 4vw, 28px);
    font-family: 'SF Mono', 'Fira Code', 'Courier New', monospace;
    font-size: clamp(12px, 2vw, 15px);
    line-height: 1.6;
    white-space: pre-wrap;  /* WRAP long lines on mobile */
    word-wrap: break-word;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
}
```

## Apple Keynote (Pure)

Maximum visual impact, minimal information density. Use for executive summaries or high-level vision decks.

**Characteristics:**
- Pure black backgrounds
- San Francisco typography (or similar sans-serif)
- One major concept per slide
- Full-bleed imagery where applicable
- Bold, centered headlines
- Avoid bullet points entirely
- Use icons or 3-word phrases instead of lists
- Premium, quiet, powerful aesthetic

**When to use:**
- Executive presentations
- Vision/strategy decks
- When visual impact matters more than information density

## Choosing a Style

| Audience | Recommended Style |
|----------|-------------------|
| Engineers, developers | Useful Apple Keynote |
| Executives, leadership | Apple Keynote (Pure) |
| Mixed audience | Useful Apple Keynote |
| Feature deep-dive | Useful Apple Keynote |
| Vision/roadmap | Apple Keynote (Pure) |

Default to **Useful Apple Keynote** unless specifically asked for the pure style.
