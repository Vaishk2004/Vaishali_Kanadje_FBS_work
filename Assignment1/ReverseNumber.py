#Reverse of 2 digit number

num = int(input("Enter the number:"))
dig1 = num // 10
dig2 = num % 10

reverse = dig2 * 10 + dig1

print("Reverse of number:",reverse)