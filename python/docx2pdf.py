import os
import win32com.client
from docx import Document

os.makedirs("media_files",exist_ok=True)
os.chdir("media_files")
file_name=[]
for files in os.listdir("."):
    if (files.endswith(".docx")) or (files.endswith(".doc")) :
        file_name.append(files)
file_name.sort(key=os.path.getctime)


def docx_to_pdf(input_file, output_file):
    
    # Create a new Word application
    word_app = win32com.client.Dispatch('Word.Application')

    try:
        # Get the absolute paths for input and output files
        input_file = os.path.abspath(input_file)
        output_file = os.path.abspath(output_file)
        print(f"Converting {input_file} .....")
        # Open the Word document
        doc = word_app.Documents.Open(input_file)

        # Save the document as PDF
        doc.SaveAs(output_file, FileFormat=17)
        print("Done")

    finally:
        # Close the Word document and application
        doc.Close()
        word_app.Quit()
        os.chdir("..")

# Usage example
name,ext=file_name[-1].split(".")
docx_to_pdf(f'{file_name[-1]}', f'{name}_converted.pdf')
