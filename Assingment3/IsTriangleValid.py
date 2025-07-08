#Input angle of triangle and triangle is valid or not

angle1 = int(input("Enter First angle: "))
angle2 = int(input("Enter Second angle: "))
angle3 = int(input("Enter Third angle: "))

if((angle1+ angle2 +angle3) == 180):
    print("Triangle is valid.")
else:
    print("Triangle is not valid.")