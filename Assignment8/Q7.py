# writw a program to find sum of digits of a number

def sumDigit(num):
    sum = 0
    i = 1
    while(num!=0):
        a = num % 10
        num = num // 10
        sum = sum + a
    return sum

num = int(input("Enter number:"))
print("Sum of Digits: ",sumDigit(num))

