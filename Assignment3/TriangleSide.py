#take input of side to check the triangle is valid or not
side1 = int(input("Enter the side: "))
side2 = int(input("Enter the side: "))
side3 = int(input("Enter the side: "))

if((side1 + side2 )> side3 and (side2 + side3)> side1 and (side1 + side3)> side2 ):
    print(" Valid Triangle.")

else:
    print("Not a Valid Triangle.")
