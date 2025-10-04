#python program to check the given key is exist or not
dict1 = {}
for i in range(5):
    k = int(input("Enter key: "))
    dict1[k] = input("Enter value: ")
print(dict1)

k = int(input("enter key you want to check: "))
for i in dict1:
    if k == i:
        print(f"Key is Present {k} : {dict1[k]}")
        break
else:
    print("Not present")