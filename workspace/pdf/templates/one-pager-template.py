"""
PDF One-Pager Template - Amplifier Stories Style

Creates a single-page executive summary with:
- Bold headline
- Key points in boxes
- Metrics section
- Professional layout

Usage:
    from one_pager_template import create_one_pager
    create_one_pager("Feature Name", "Description", key_points, metrics, "output.pdf")
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas

# Amplifier Keynote Colors
COLORS = {
    "blue": HexColor("#0A84FF"),
    "black": HexColor("#000000"),
    "white": HexColor("#FFFFFF"),
    "gray": HexColor("#595959"),
    "gray_light": HexColor("#F3F2F1"),
}


def create_one_pager(title, subtitle, key_points, metrics, filename):
    """
    Create executive one-pager.

    Args:
        title: Main headline
        subtitle: Subtitle/description
        key_points: List of key takeaway strings
        metrics: List of (number, label) tuples
        filename: Output PDF filename
    """
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    # Title section
    c.setFillColor(COLORS["blue"])
    c.setFont("Helvetica-Bold", 36)
    c.drawString(inch, height - 1.5 * inch, title)

    c.setFillColor(COLORS["gray"])
    c.setFont("Helvetica", 14)
    c.drawString(inch, height - 2 * inch, subtitle)

    # Horizontal divider
    c.setStrokeColor(COLORS["gray_light"])
    c.setLineWidth(2)
    c.line(inch, height - 2.3 * inch, width - inch, height - 2.3 * inch)

    # Key Points section
    y_position = height - 3 * inch
    c.setFillColor(COLORS["black"])
    c.setFont("Helvetica-Bold", 12)
    c.drawString(inch, y_position, "KEY POINTS")

    y_position -= 0.4 * inch
    c.setFont("Helvetica", 11)
    for point in key_points[:4]:  # Max 4 points
        c.drawString(inch + 0.2 * inch, y_position, f"• {point}")
        y_position -= 0.3 * inch

    # Metrics section
    y_position -= 0.5 * inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(inch, y_position, "IMPACT")

    y_position -= 0.5 * inch

    # Draw metrics in grid
    metrics_per_row = 3
    metric_width = (width - 2 * inch) / metrics_per_row

    for idx, (number, label) in enumerate(metrics[:6]):
        col = idx % metrics_per_row
        row = idx // metrics_per_row
        x = inch + col * metric_width
        y = y_position - row * inch

        # Metric box
        c.setStrokeColor(COLORS["gray_light"])
        c.setLineWidth(1)
        c.rect(x, y - 0.7 * inch, metric_width - 0.2 * inch, 0.7 * inch)

        # Number
        c.setFillColor(COLORS["blue"])
        c.setFont("Helvetica-Bold", 24)
        c.drawCentredString(
            x + metric_width / 2 - 0.1 * inch, y - 0.3 * inch, str(number)
        )

        # Label
        c.setFillColor(COLORS["gray"])
        c.setFont("Helvetica", 9)
        c.drawCentredString(x + metric_width / 2 - 0.1 * inch, y - 0.6 * inch, label)

    # Footer
    c.setFillColor(COLORS["gray"])
    c.setFont("Helvetica", 8)
    c.drawString(inch, 0.5 * inch, "Generated with Amplifier")

    c.save()
    return filename


if __name__ == "__main__":
    sample_points = [
        "Dramatically reduces development time",
        "Increases code reusability across projects",
        "Improves security with fine-grained permissions",
        "Enables pip-installable distribution",
    ]

    sample_metrics = [
        ("1,500→0", "Lines Saved"),
        ("60%", "Less YAML"),
        ("50+", "Security Effects"),
        ("77", "Tests Passing"),
        ("1.7KB", "Package Size"),
        ("2%", "Overhead"),
    ]

    create_one_pager(
        "Amplifier Surface",
        "The 6th Module Type for AI Agent Collaboration",
        sample_points,
        sample_metrics,
        "one-pager-example.pdf",
    )
    print("One-pager created: one-pager-example.pdf")
