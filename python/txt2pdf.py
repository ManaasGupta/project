from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph
import os



def text_to_pdf(input_file, output_file):
    print(f"Converting {input_file} .....")
    styles = getSampleStyleSheet()
    style = styles['Normal']
    style.fontName = 'Helvetica'
    style.fontSize = 12

    paragraphs = []

    with open(input_file, 'r',encoding='cp1252') as f:
        lines = f.readlines()
        for line in lines:
            p = Paragraph(line.strip(), style)
            paragraphs.append(p)

    doc = SimpleDocTemplate(output_file, pagesize=letter)
    doc.build(paragraphs)
    print("Done")

# Usage example
# if __name__=="__main__":
#     out_file=file_name[-1].split(".")
#     text_to_pdf(f'{file_name[-1]}', f'{out_file[0]}.pdf')
