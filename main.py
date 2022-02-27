from multiprocessing.sharedctypes import Value
import string 
import random

s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.digits
s4 = string.punctuation

try:
    print("Welcome to password generator tool !\n")
    pwlen = int(input("Enter the length of the password you need to generate: \n"))
    
    s_1 = list(s1)
    s_2 = list(s2)
    s_3 = list(s3)
    s_4 = list(s4)
    
    list = []
    
    list.extend(s_1)
    list.extend(s_2)
    list.extend(s_3)
    list.extend(s_4)
    
    random.shuffle(list)
    
    print("Your password is: ")    
    print("".join(random.sample(list,pwlen)))
    
except:
    raise ValueError("Enter Integer !")