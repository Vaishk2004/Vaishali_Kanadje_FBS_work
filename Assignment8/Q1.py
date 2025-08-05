#write program to calculate area of rectangle
def areaRect(length,breadth):
    area = length * breadth
    return area

length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))

print("Area of rectangle: ",areaRect(length,breadth))