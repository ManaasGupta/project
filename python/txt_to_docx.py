import os
from txt2pdf import text_to_pdf
from pdf_to_docx import convert_pdf_to_docx

os.chdir("..")
os.makedirs("media_files",exist_ok=True)
os.chdir("media_files")
fname=[]
for files in os.listdir("."):
    if files.endswith(".txt"):
        fname.append(files)
fname.sort(key=os.path.getctime)


def txt2docx(input_file,output_file):
    # step 1) Text - PDF
    text_to_pdf(input_file,"int.pdf")
    os.chdir("media_files")
    # step 2) PDF - DOCX
    convert_pdf_to_docx("int.pdf",output_file)
    os.chdir("media_files")
    # step 3) Removing unnecessary files
    infile=input_file.split(".")
    os.remove(f"{infile[0]}.pdf")
    os.remove("int.pdf")
    print(f"{input_file} converted to {output_file} sucessfully")
    os.chdir("..")
    
# usage example
out_file=fname[-1].split(".")
print(out_file)
txt2docx(f'{fname[-1]}', f'{out_file[0]}.docx')