from pdfminer.high_level import extract_text
import os


def convert_pdf_to_text(input_file,output_file):
    print(f"Converting {input_file} .....")
    text = extract_text(input_file)
    with open(output_file,"w",encoding='utf-8') as output:
        output.write(text)
    print("Done")
# if __name__=="__main__":
#     outfile=file_name[-1].split(".")
#     convert_pdf_to_text(f'{file_name[-1]}', f'{outfile[0]}.txt')
