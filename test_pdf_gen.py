import os
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="PDF Generation Capability Test - Success!", ln=True, align='C')
pdf.output("test_capability.pdf")
