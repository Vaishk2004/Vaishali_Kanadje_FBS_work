#Python program multiply all the items in dictionary
dict1 = {}
for i in range(5):
    k = int(input("Enter integer key: "))
    dict1[k] = int(input("Enter integer value: "))
print(dict1)

k = int(input("Enter number which is used for multiplication: "))

dict1 = {x*k : y*k for x , y in dict1.items()}

print(dict1)
