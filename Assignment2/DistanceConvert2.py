#Convert the given distance in feet and inches into meter and centimeter

feet = int(input("Enter the distance in feet:"))
inches = int(input("Enter the distance in inches:"))

meter = feet * 0.3048
cm = inches * 2.54

print("THe distance convert feet to meter is:",meter)
print("The distance convert from inches to centimeter is :",cm)