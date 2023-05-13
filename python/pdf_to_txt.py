from pdfminer.high_level import extract_text
import os

os.makedirs("media_files",exist_ok=True)
os.chdir("media_files")
file_name=[]
for files in os.listdir("."):
    if files.endswith(".pdf"):
        file_name.append(files)
file_name.sort(key=os.path.getctime)


def convert_pdf_to_text(input_file,output_file):
    print(f"Converting {input_file} .....")
    text = extract_text(input_file)
    outfile=file_name[-1].split(".")
    with open(output_file,"w") as output:
        output.write(text)
    print("Done")
    os.chdir("..")
outfile=file_name[-1].split(".")
convert_pdf_to_text(f'{file_name[-1]}', f'{outfile[0]}.txt')
