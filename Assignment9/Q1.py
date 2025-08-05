# function to calculate the sum of series
#  1!+2!+3!+......n!

def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)

# Recursive function to calculate sum of factorials
def sumFact(n):
    if n == 1:
        return 1
    return factorial(n) + sumFact(n - 1)


num = int(input("Enter number: "))
print("Sum of factorials:", sumFact(num))

        
