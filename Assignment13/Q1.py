#Python program to add the key-value pair in dictionary
dict1 = {}
for i in range(5):
    k = int(input("Enter key: "))
    dict1[k] = input("Enter value: ")

print(dict1)

dict1[6] = "Hello"
print(dict1)