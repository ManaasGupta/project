import os
import win32com.client
from pdfminer.high_level import extract_text


def docx_to_pdf(input_file, output_file):
    
    # Create a new Word application
    word_app = win32com.client.Dispatch('Word.Application')

    # Get the absolute paths for input and output files
    input_file = os.path.abspath(input_file)
    output_file = os.path.abspath(output_file)
    print(f"Converting {input_file} .....")
    # Open the Word document
    doc = word_app.Documents.Open(input_file)
    # Save the document as PDF
    doc.SaveAs(output_file, FileFormat=17)
    # Close the Word document and application
    doc.Close()
    word_app.Quit()
        
def convert_pdf_to_text(input_file,output_file):
    text = extract_text(input_file)
    with open(output_file,"w") as output:
        output.write(text)
    print("Done")
    
def convert_docx_to_txt(docx_file_path,txt_file_path):
    # convert txt to pdf
    docx_to_pdf(docx_file_path, "int.pdf")
    # convert pdf to docx file
    convert_pdf_to_text("int.pdf",txt_file_path)
    #remove intermediate files
    os.remove("int.pdf")
    return 

# Example usage
# if __name__=="__main__":
#     name=file_name[-1].split(".")
#     print(name[0])
#     print(file_name[-1])
#     convert_docx_to_txt(f'{file_name[-1]}', f'{name[0]}.txt')