# Count the occurance of each word in a string
str = input("Enter string: ")

unic = set(list(str))

for x in unic:
    print(x,":",str.count(x))