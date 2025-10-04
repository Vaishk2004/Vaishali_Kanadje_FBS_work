#Program to print list after removing even numbers

n = int(input("Enter range: "))
list1 = []
for i in range(n):
    list1.append(int(input()))
print("Before list: ",list1)

list2 = []
for i in range(n):
    if list1[i] % 2 != 0:
        list2.append(list1[i])
print("List after removing even number: ",list2)