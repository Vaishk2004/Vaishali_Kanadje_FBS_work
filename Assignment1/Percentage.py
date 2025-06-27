#To calculate the percentage of student
m1 = int(input("Enter the Math Marks : "))
m2 = int(input("Enter the phy Marks : "))
m3 = int(input("Enter the chem Marks : "))
m4 = int(input("Enter the hindi Marks : "))
m5 = int(input("Enter the english Marks : "))

obtain_marks = m1+m2+m3+m4+m5
total_marks = 500

percen = (obtain_marks/total_marks)*100

print("Percentage : ", percen)