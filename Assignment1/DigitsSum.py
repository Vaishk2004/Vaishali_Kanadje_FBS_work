#Addition of digits in 2 digit number
num = int(input("Enter the 2 digit number : "))
digit1 = num // 10
digit2 = num % 10

add = digit1 + digit2

print("Addition of digits in two digit number is :",add)