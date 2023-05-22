from docx_to_txt import convert_docx_to_txt
from docx2pdf import docx_to_pdf
from pdf_to_docx import convert_pdf_to_docx
from pdf_to_txt import convert_pdf_to_text
from txt_to_docx import convert_txt_to_docx
from txt2pdf import text_to_pdf

list_of_operations=["Word File to TXT File","Word File to PDF File","PDF File to Word File","PDF File to TXT File","TXT File to Word File","TXT File to PDF File"]

def main():
    print("Welome to Format converter\n")
    print("Select Option number from below:\n ")
    for idx,value in enumerate(list_of_operations):
        print(f"{idx+1} : {value}\n")
    op_num=int(input("Enter Operation Number : " ))
    print("\n")
    # if op_num==1:
    #     print("Enter Word File Name : ",end="")
    #     word_file_name=input()
    #     print("Enter Output File Name : ",end="")
    #     output_file_name=input()
    #     convert_docx_to_txt(word_file_name,output_file_name)
    # elif op_num==2:
    #     print("Enter PDF File Name : ",end="")
    #     pdf_file_name=input()
    #     print("Enter Output File Name : ",end="")
    #     output_file_name=input()
    #     docx_to_pdf(pdf_file_name,output_file_name)
    # elif op_num==3:
    #     print("Enter PDF File Name : ",end="")
    #     pdf_file_name=input()
    #     print("Enter Output File Name : ",end="")
    #     output_file_name=input()
    #     convert_pdf_to_docx(pdf_file_name,output_file_name)
    # elif op_num==4:
    #     print("Enter PDF File Name : ",end="")
    #     pdf_file_name=input()
    #     print("Enter Output File Name : ",end="")
    #     output_file_name=input()
    #     convert_pdf_to_text(pdf_file_name,output_file_name)
    # elif op_num==5:
    #     print("Enter TXT File Name : ",end="")
    #     txt_file_name=input()
    #     print("Enter Output File Name : ",end="")
    #     output_file_name=input()
    #     convert_txt_to_docx(txt_file_name,output_file_name)
    # elif op_num==6:
    #     print("Enter TXT File Name : ",end="")
    #     txt_file_name=input()
    #     print("Enter Output File Name : ",end="")
    #     output_file_name=input()
    #     text_to_pdf(txt_file_name,output_file_name)
    # else:
    #     print("Invalid Operation Number !")
        
    
if __name__=="__main__":
    main()