# Check if user has entered correct userid and password
userid = input("Enter the Userid: ")
password = input("Enter the Password: ")

if(userid == "Vaishali" and  password == "Vaishali123"):
    print("Valid!! Successfully login.")

else:
    print("Invalid userid and password.")