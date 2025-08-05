#Program to find the sum of series using function

#a. 1+2+3+....+n
def funSum(num):
    sum = 0
    for i in range(1,num+1):
        sum = sum + i
    return sum

print("Sum of 1+2+3+....+n ")
num = int(input("Enter number: "))
print(funSum(num))



#b.  1!+2!+3!+...+n!
def funFact(num):
    sum = 0
    for i in range(1,num+1):
        sum = 0
        fact = 1
        for j in range(1,i+1):
            fact= fact * j
            sum = sum +fact
    return sum

print("Sum of  1!+2!+3!+...+n!")
num = int(input("Enter number: "))
print(funFact(num))



# c.1^1+2^2+3^3+.....+n^n
def sumSquare(num):
    sum = 0
    for i in range(1,num+1):
        ans = i**i
        sum = sum + ans
    return sum

print("1^1+2^2+3^3+.....+n^n")
num = int(input("Enter number: "))
print(sumSquare(num))