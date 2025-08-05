#Write a progrsm to find the factorial of number using recursion
def factorial(num):
    if num == 1 :
        return 1
    else:
        return num * factorial(num-1)

num = int(input("Enter number: "))
print("Factorial of number is :",factorial(num))