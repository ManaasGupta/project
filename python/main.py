from docx_to_txt import convert_docx_to_txt
from docx2pdf import docx_to_pdf
from pdf_to_docx import convert_pdf_to_docx
from pdf_to_txt import convert_pdf_to_text
from txt_to_docx import convert_txt_to_docx
from txt2pdf import text_to_pdf
import argparse
import sys
import os

def main(args):
    print("Welome to Format converter\n")
    print("\n")
    oper_num=int(args.mode)
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
    parser.add_argument('-m','--mode',help="Enter path to ouput_file you want to converted in extension",required=True,type=int)
    args=parser.parse_args()
    sys.stdout.write(str(main(args)))