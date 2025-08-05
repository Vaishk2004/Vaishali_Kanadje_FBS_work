#Program to create three lists of numbers,their squares and cube
list1 = []
num = int(input("Enter number of element in list: "))
for i in range(num):
    list1.append(int(input()))
print("List of Numbers: ",list1)


square = []
for i in range(num):
    ans = list1[i] ** 2
    square.append(ans)
print("List of Squares: ",square)


cube = []
for i in range(num):
    ans = list1[i] ** 3
    cube.append(ans)
print("List of Cube: ",cube)