#Count the number of spaces in a string (take input from user)

str1 = input("Enter string: ")

spaces = [s for s in str1 if s == " "]
count = len(spaces)

print("Number of spaces in string: ",count)