import os
from docx2pdf import docx_to_pdf
from pdf_to_txt import convert_pdf_to_text


os.makedirs("media_files",exist_ok=True)
os.chdir("media_files")
file_name=[]
for files in os.listdir("."):
    if (files.endswith(".docx")) or (files.endswith(".doc")) :
        file_name.append(files)
file_name.sort(key=os.path.getctime)

print(file_name)

def convert_docx_to_text(input_file,output_file):
    docx_to_pdf(input_file,"int.pdf")
    os.chdir("media_files")
    convert_pdf_to_text("int.pdf",output_file)
    os.chdir("media_files")
    infile=input_file.split(".")
    os.remove(f"{infile[0]}.pdf")
    os.remove("int.pdf")
    print(f"{input_file} converted to {output_file} sucessfully")
    os.chdir("..")

# usage example
out_file=file_name[-1].split(".")
print(out_file)
convert_docx_to_text(f'{file_name[-1]}', f'{out_file[0]}.txt')