#Accept year from user and check if it is leap year or not
year = int(input("Enter the year:"))

if(year % 4 == 0):
    if(year % 100 != 0 ):
        print("Leap year.")
    else:
        if(year % 400 == 0):
            print("Leap year.")
        else:
            print("Not leap.")
    
else:
    print("Not Leap.")