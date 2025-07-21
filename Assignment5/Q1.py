# Give prompt to user enter userid and password if wrong then give 
#3 chances after  terminate

userid = input("Enter Userid: ")
password = input("Enter Password: ")

username = "Vaishali"
passw = "Pass@123"

if(userid == username and password == passw):
    print("Successfully Login!!")
else:
    i = 1
    while(i<3):
        print("Wrong userid and password. ")
        print("Re-enter credentials:.")
        userid = input("Enter Userid: ")
        password = input("Enter Password: ")
        if(userid == username and password == passw):
            print("Successfully Login!!")
            break
        i += 1
    else:
        print("Terminate")

