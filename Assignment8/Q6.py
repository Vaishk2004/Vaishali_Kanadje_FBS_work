# Write a function to print the fibonacci series
# 1 1 2 3 5 8...n term

def fibonacci(num):
    a = -1
    b = 1
    for i in range(1,num+1):
        c = a + b
        print(c)
        a = b
        b = c


num = int(input("Enter number: "))
print("The Fibonacci series: ")
fibonacci(num)
