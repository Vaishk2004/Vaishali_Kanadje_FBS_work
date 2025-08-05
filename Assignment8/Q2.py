#write a program to calculate area of circle

def areaCircle(radius):
    area = 3.14 * radius * radius
    return area

radius = int(input("Enter radius: "))
print("Area of Circle",areaCircle(radius))