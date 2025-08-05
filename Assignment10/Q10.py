# Remove all occurence of a given element in the list
list1 = []
n = int(input("Enter number of element in list: "))
for i in range(n):
    list1.append(int(input()))
print(list1)

num = int(input("Enter the element: "))
for i in range(n):
    if num in list1:
        list1.remove(num)
print("After list: ",list1)