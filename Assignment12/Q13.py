# Count number of digits and letters in string
str = input("Enter string: ")

c_digit = 0
c_letter = 0
for i in str:
    if i.isalpha():
        c_letter += 1
    elif i.isdigit():
        c_digit += 1
    
print("Number of digits: ",c_digit)
print("Number of letters: ",c_letter)