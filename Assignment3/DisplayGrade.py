#Input 5 subject marks and display grade
sub1 = int(input("Enter the marks: "))
sub2 = int(input("Enter the marks: "))
sub3 = int(input("Enter the marks: "))
sub4 = int(input("Enter the marks: "))
sub5 = int(input("Enter the marks: "))

if(sub1 > 40 and sub2 > 40 and sub3 > 40 and sub4 > 40 and sub5 > 40):
    obtain_mark = sub1 + sub2 + sub3 + sub4 +sub5
    per = (obtain_mark / 500) * 100
    print("Percentage:",per)

    if(per >= 80  and per <= 100):
        print("Grade: First Class With Distinction.")
    elif(per >= 70 and per < 80):
        print("Grade: First Class.")
    elif(per >= 60 and per < 70):
        print("Grade: Higher Second Class.")
    elif(per >= 40 and per < 60 ):
        print("Grade: Second class")
    elif(per < 40 and per > 0):
        print("Fail")
    else:
        print("Fail")

else:
    print("Fail")



