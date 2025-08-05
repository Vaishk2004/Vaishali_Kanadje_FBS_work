#Write a program to find sum of digits in number using recursion
def sumDigit(num):
    if num == 0 :
        return 0
    else:
        a = num % 10
        return a + sumDigit(num//10)
    
num = int(input("Enter number: "))
print(sumDigit(num))