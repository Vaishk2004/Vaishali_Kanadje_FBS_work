#Program to print list after removing even numbers
list1 = []
num = int(input("Enter number of element in list: "))
for i in range(num):
    list1.append(int(input()))
print(list1)


list2 = []
for i in range(num):
    if list1[i] % 2 != 0:
        list2.append(list1[i])

print("List After removing all even numbers: ",list2)