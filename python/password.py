import string
from colorama import Fore,Style
import argparse
import sys

num_char=['1','2','3','4','5','6','7','8','9','0']
def convert(arr):
    lst=[]
    for i in arr:
        lst.append(i)
    return lst

def pass_check(args):
    alphabet = list(string.ascii_lowercase)
    cap_alpha=list(string.ascii_uppercase)
    alpha_score=0
    cap_score=0
    num_score=0
    sym_score=0
    char_list=convert(args.password)
    if (len(char_list) < 8):
        print(Fore.RED +"Password length too small should contain atleast 8 characters ")
        print(Style.RESET_ALL)
    elif (len(char_list) > 20):
        print(Fore.RED + "Password length too large should contain at max 256 characters")
        print(Style.RESET_ALL)
    
    for char in char_list:
        if char in alphabet:
            alpha_score+=1
        elif char in cap_alpha:
            cap_score+=1
        elif char in num_char:
            num_score+=1
        else:
            sym_score+=1
        
    
    if alpha_score == 0:
        print(Fore.RED + "Password should contain atleast 1 alphabet")
    if cap_score == 0:
        print(Fore.RED + "Password should contain atleast 1 capital letter")
    if num_score == 0:
        print(Fore.RED + "Password should contain atleast 1 number")
    if sym_score == 0:
        print(Fore.RED + "Password should contain atleast 1 symbol")
    if all([alpha_score,cap_score,num_score,sym_score])>0:
        print(Fore.GREEN+'You entered valid Password') 
    print(Style.RESET_ALL)
    return "RUN Sucessful"
if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument('-p','--password',help="Enter path to input_file you want to convert with extension",required=True)
    args=parser.parse_args()
    sys.stdout.write(str(pass_check(args)))