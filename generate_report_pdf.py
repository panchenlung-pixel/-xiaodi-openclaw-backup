from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# Create reports directory
os.makedirs("reports", exist_ok=True)

# Generate simple text report without encoding issues (using default font first)
c = canvas.Canvas("reports/AI_Enterprise_Management_Report_2026.pdf")
c.setFont("Helvetica-Bold", 16)
c.drawString(100, 800, "AI Management Report (Summary)")
c.setFont("Helvetica", 12)
text_lines = [
    "1. Executive Summary: AI is the core driver of strategic enterprise transformation.",
    "2. Strategic Paradigm: Automation -> Decision Optimization.",
    "3. Application: Supply Chain, Decision Support, HR Talent Management.",
    "4. Challenges: Data Silos, Talent Shortage, Data Governance.",
    "5. Conclusion: Data Governance is the new corporate infrastructure."
]

y = 750
for line in text_lines:
    c.drawString(50, y, line)
    y -= 20

c.save()
print("PDF generated successfully.")
