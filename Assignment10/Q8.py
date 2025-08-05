#Write a program to create duplicate of an existing list

list1 = []
n = int(input("How many number you want in list: "))
for i in range(n):
    list1.append(int(input()))


list2 = []
for i in list1:
    list2.append(i)

print("Orignal list: ",list1)
print("Duplicate list: ",list2)
print(id(list1))
print(id(list2))
