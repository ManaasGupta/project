from docx_to_txt import convert_docx_to_txt
from docx2pdf import docx_to_pdf
from pdf_to_docx import convert_pdf_to_docx
from pdf_to_txt import convert_pdf_to_text
from txt_to_docx import convert_txt_to_docx
from txt2pdf import text_to_pdf
import argparse
import sys

list_of_operations=["Word File to TXT file","Word File to PDF file","PDF File to Word file","PDF File to TXT file","TXT File to Word file","TXT File to PDF file"]

def main(args):
    print("Welome to Format converter\n")
    for idx,value in enumerate(list_of_operations):
        print(f"{idx+1}: {value} \n")
    print("Please select the option from the menu below\n")
    oper_num=int(input())
    print("/n")
    if oper_num==1:
        convert_docx_to_txt(args.input_file,args.output_file)
    elif oper_num==2:
        docx_to_pdf(args.input_file,args.output_file)
    elif oper_num==3:
        convert_pdf_to_docx(args.input_file,args.output_file)
    elif oper_num==4:
        convert_pdf_to_text(args.input_file,args.output_file)
    elif oper_num==5:
        convert_txt_to_docx(args.input_file,args.output_file)
    elif oper_num==6:
        text_to_pdf(args.input_file,args.output_file)
    else:
        print("Invalid Operation Number !")
    
if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument('-i','--input_file',help="Enter path to input_file you want to convert with extension",required=True)
    parser.add_argument('-o','--output_file',help="Enter path to ouput_file you want to converted in extension",required=True)
    args=parser.parse_args()
    sys.stdout.write(str(main(args)))