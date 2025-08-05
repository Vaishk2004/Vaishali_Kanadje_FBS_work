#Writw a program to print fibonacci series using recursion
def fibonacci(a,b,num):
    if(num>0):
        c = a+b
        print(c)
        fibonacci(b,c,num-1)

num = int(input("Enter number: "))
fibonacci(-1,1,num)