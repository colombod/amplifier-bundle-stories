#!/usr/bin/env python3
"""
pptx2images.py - Render PowerPoint slides to PNG images for visual inspection.

Uses LibreOffice to convert PPTX -> PDF, then ImageMagick to convert PDF -> PNGs.

Usage:
    python pptx2images.py <input.pptx> [output_dir]

Output:
    Creates slide-01.png, slide-02.png, etc. in the output directory.
"""

import argparse
import subprocess
import sys
import tempfile
from pathlib import Path


def convert_pptx_to_pdf(pptx_path: Path, output_dir: Path) -> Path:
    """Convert PPTX to PDF using LibreOffice."""
    cmd = [
        "libreoffice",
        "--headless",
        "--convert-to", "pdf",
        "--outdir", str(output_dir),
        str(pptx_path)
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"LibreOffice error: {result.stderr}", file=sys.stderr)
        sys.exit(1)
    
    pdf_path = output_dir / pptx_path.with_suffix('.pdf').name
    return pdf_path


def convert_pdf_to_images(pdf_path: Path, output_dir: Path, prefix: str = "slide") -> list[Path]:
    """Convert PDF pages to PNG images using ImageMagick."""
    output_pattern = output_dir / f"{prefix}-%02d.png"
    
    cmd = [
        "convert",
        "-density", "150",  # DPI for rendering
        "-background", "white",
        "-alpha", "remove",
        str(pdf_path),
        str(output_pattern)
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"ImageMagick error: {result.stderr}", file=sys.stderr)
        sys.exit(1)
    
    # Find all generated images
    images = sorted(output_dir.glob(f"{prefix}-*.png"))
    return images


def main():
    parser = argparse.ArgumentParser(
        description="Render PowerPoint slides to PNG images for visual inspection."
    )
    parser.add_argument("input", help="Input PPTX file path")
    parser.add_argument("output_dir", nargs="?", help="Output directory (default: same as input)")
    parser.add_argument("--prefix", default="slide", help="Output filename prefix")
    
    args = parser.parse_args()
    
    pptx_path = Path(args.input).resolve()
    if not pptx_path.exists():
        print(f"Error: Input file not found: {pptx_path}", file=sys.stderr)
        sys.exit(1)
    
    if args.output_dir:
        output_dir = Path(args.output_dir)
    else:
        output_dir = pptx_path.parent / "slides"
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Converting: {pptx_path}")
    print(f"Output directory: {output_dir}")
    
    # Step 1: PPTX -> PDF
    print("Step 1: Converting PPTX to PDF...")
    with tempfile.TemporaryDirectory() as tmpdir:
        pdf_path = convert_pptx_to_pdf(pptx_path, Path(tmpdir))
        
        # Step 2: PDF -> PNGs
        print("Step 2: Converting PDF pages to PNG images...")
        images = convert_pdf_to_images(pdf_path, output_dir, args.prefix)
    
    print(f"\nCreated {len(images)} slide images:")
    for img in images:
        print(f"  {img.name}")
    
    return images


if __name__ == "__main__":
    main()
