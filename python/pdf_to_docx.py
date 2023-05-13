from pdf2docx import Converter
import os

os.makedirs("media_files",exist_ok=True)
os.chdir("media_files")
file_name=[]
for files in os.listdir("."):
    if (files.endswith(".pdf")) :
        file_name.append(files)
file_name.sort(key=os.path.getctime)


def convert_pdf_to_docx(pdf_path, docx_path):
    print(f"Converting {pdf_path} .....")
    cv = Converter(pdf_path)
    cv.convert(docx_path, start=0, end=None)
    cv.close()
    print("Done")
    os.chdir("..")

# Example usage
name,ext=file_name[-1].split(".")
convert_pdf_to_docx(f'{file_name[-1]}', f'{name}.docx')
