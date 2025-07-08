# Enter Three sides of triangle and check whether it is equilateral triangle or not

side1 = int(input("Enter the first side of triangle:"))
side2 = int(input("Enter the Second side:"))
side3 = int(input("Enter the third side:"))

if (side1 == side2 == side3):
    print("The triangle is Equilateral triangle.")
elif(side1 == side2 or side2 == side3 or side1 == side3):
    print("The triangle is Isosceles.")
else:
    print("The triangle is Scalene triangle.")