# Program to three list of numbers ,their squares and cubes
n = int(input("Enter the range: "))
number = [] 
cube = []
square = []

for i in range(n):
    number.append(int(input()))
print("Numbers list:",number)


for i in range(n):
    ans = number[i]**2
    square.append(ans)
print("Square list: ",square)


for i in range(n):
    ans = number[i]**3
    cube.append(ans)
print("Cube list: ",cube)