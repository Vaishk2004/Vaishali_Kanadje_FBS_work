# Python program to sum all the items in dictionary
number = {}
for i in range(5):
    k = int(input("Enter key: "))
    number[k] = int(input("Enter value: "))
print(number)

sum = 0
for i,j in number.items():
    sum += i+j
print("Sum of all items in Dictionary: ",sum)
