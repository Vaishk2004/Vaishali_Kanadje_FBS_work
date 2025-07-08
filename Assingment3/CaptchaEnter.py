#Varify userid and password entered by user and  display 4 digit random number and ask user to enter same. 
import random

userid = input("Enter Userid: ")
password = input("Enter the password: ")

if(userid == "Vaishali" and password == "Pass@123"):
    captcha = random.randint(1000,9999)
    print("Captcha: ",captcha)
    user_captcha = int(input("Enter Captcha: "))

    if(user_captcha == captcha ):
        print("Successfully Login!!!")
    else:
        print("Wrong Captcha.")

else:
    print("Fail.")