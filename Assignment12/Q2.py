#Remove the nth index character from non empty string
str = input("Enter string: ")
n = int(input("Enter index: "))

list1 = list(str)
list1.pop(n)
output = ''.join(list1)

print(output)