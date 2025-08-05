#write a program to check the year is leap or not
def leapYear(year):
    if(year%4==0 ):
        if(year % 100):
            if(year % 400):
                return "Leap year"
            else:
                return "Not leap year"
        else:
            return " Leap year"
    else:
        return " not a leap year"
        

year = int(input("Enter year: "))
print(leapYear(year))