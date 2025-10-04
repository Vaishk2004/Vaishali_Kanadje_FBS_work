#Python program to remove the characters at odd index in string
str = input("Enter string: ")
print("Before: ",str)

list1 = list(str)
list2 = []
for i in range(len(list1)):
    if i % 2 == 0:
        list2.append(list1[i])

str = ''.join(list2)
print("After remove character at odd index: ",str)