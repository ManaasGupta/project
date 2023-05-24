from pdf2docx import Converter
import os



def convert_pdf_to_docx(pdf_path, docx_path):
    print(f"Converting {pdf_path} .....")
    cv = Converter(pdf_path)
    cv.convert(docx_path)
    cv.close()
    print("Done")

# Example usage
# if __name__=="__main__":
#     name,ext=file_name[-1].split(".")
#     convert_pdf_to_docx(f'{file_name[-1]}', f'{name}.docx')
