#Put even and odd elements of a list into two different list
list1 = []
n = int(input("Enter how many number you want: "))
for i in range(n):
    list1.append(int(input()))
print(list1)

even = []
odd = []
for i in range(n):
    if list1[i]% 2 == 0:
        even.append(list1[i])
    else:
        odd.append(list1[i])

print('Even number list: ',even)
print("Odd number list: ",odd)