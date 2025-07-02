#Sum of digits in Three Digit number
num = int(input("Enter the three digit number:")) #234

a = num % 10 #4
num = num // 10 #23
b = num % 10 #3
c = num // 10 #2

sum = a + b + c

print("The Sum of digits in the three digit number:",sum)