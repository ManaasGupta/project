import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph
from pdf2docx import Converter


os.makedirs("media_files",exist_ok=True)
os.chdir("media_files")
file_name=[]
for files in os.listdir("."):
    if (files.endswith(".txt")) :
        file_name.append(files)
file_name.sort(key=os.path.getctime)


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
    
def convert_pdf_to_docx(pdf_path, docx_path):
    cv = Converter(pdf_path)
    cv.convert(docx_path, start=0, end=None)
    cv.close()
    print("Done")

def convert_txt_to_docx(txt_file_path, docx_file_path):
    # convert txt to pdf
    text_to_pdf(txt_file_path, "int.pdf")
    # convert pdf to docx file
    convert_pdf_to_docx("int.pdf",docx_file_path)
    #remove intermediate files
    os.remove("int.pdf")
    os.chdir("..")

# Example usage
if __name__=="__main__":
    name=file_name[-1].split(".")
    print(name)
    convert_txt_to_docx(f'{file_name[-1]}', f'{name[0]}.docx')