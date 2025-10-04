#Python program to find the union of two list
n = int(input("Enter range of lists: "))
list1 = []
list2 = []

for i in range(n):
    list1.append(int(input()))
print("First list: ",list1)


for i in range(n):
    list2.append(int(input()))
print("Second list: ",list2)


union = []

for i in range(n):
    if list1[i] not in union:
        union.append(list1[i])

for i in range(n):
    if list2[i] not in union:
        union.append(list2[i])
    
print("Union of two lists: ",union)
    