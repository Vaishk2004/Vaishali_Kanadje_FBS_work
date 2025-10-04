# Program to remove the given key from a dictionary
dict1 = {}
for i in range(5):
    k = input("Enter key in string: ")
    dict1[k] = int(input("Enter value in number: "))
print(dict1)

k = input("Enter key you want to remove: ")
dict1.pop(k,0)
print("After remove key: ",dict1)