import string
from colorama import Fore,Style


num_char=['1','2','3','4','5','6','7','8','9','0']
def convert(arr):
    lst=[]
    for i in arr:
        lst.append(i)
    return lst

def pass_check(arr):
    alphabet = list(string.ascii_lowercase)
    cap_alpha=list(string.ascii_uppercase)
    alpha_score=0
    cap_score=0
    num_score=0
    sym_score=0
    char_list=convert(arr)
    if (len(char_list) < 8):
        print(Fore.RED +"Password length too small should contain atleast 8 characters ")
        print(Style.RESET_ALL)
    elif (len(char_list) > 256):
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
    
if __name__=="__main__":
    enter_password=str(input("Enter the Password: "))
    pass_check(enter_password)