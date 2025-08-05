#Program to remove duplicates from the list
list1 = []
n = int(input("How many number you want in list: "))
for i in range(n):
    list1.append(int(input()))
print(list1)

list2 = []
for i in range(n):
    if list1[i] not in list2:
        list2.append(list1[i])

print("List Without duplicates: ",list2)

