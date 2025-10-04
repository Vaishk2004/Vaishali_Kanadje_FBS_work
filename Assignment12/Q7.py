# Python program ro calculate the length of the string without using library function
str = input("Enter string: ")

count = 0
for i in str:
    count += 1
print("Length of string: ",count)