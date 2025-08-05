#Sum of element of list
list1 = []
n = int(input("How many number you want in list: "))
for i in range(n):
    list1.append(int(input()))
print(list1)


sum = 0
for i in range(len(list1)):
    sum += list1[i]

print("Sum of element in list: ",sum)
