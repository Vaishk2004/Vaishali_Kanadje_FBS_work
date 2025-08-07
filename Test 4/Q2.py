# Factorial of of number in given range
def fact(n):
    if n ==1:
        return 1
    else:
        return n * fact(n-1)

num = int(input("Enter number: "))  
 
for i in range(1,num+1):
    print("Fatorial of ",i,":",fact(i))
    

