import os
import win32com.client

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
    print("Done")
    # Close the Word document and application
    doc.Close()
    word_app.Quit()
    
# Usage example
# if __name__=="__main__":
#     name,ext=file_name[-1].split(".")
#     docx_to_pdf(f'{file_name[-1]}', f'{name}_converted.pdf')
