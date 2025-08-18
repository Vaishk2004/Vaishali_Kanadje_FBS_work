# Program to find the union of two list. Without using set

li1 = []
num = int(input("Enter range for list: "))
for i in range(num):
    li1.append(int(input()))
print("First list: ",li1)

li2 = []
for i in range(num):
    li2.append(int(input()))
print("First list: ",li2)

for i in li2:
    if i not in li1:
        li1.append(i)

print("Union: ",li1)
