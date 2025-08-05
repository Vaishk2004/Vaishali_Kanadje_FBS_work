# Write a program to check if given number is armstrong or not using recursion
def count(num):
    if(num != 0):
        return 1 + count(num//10)
    else:
        return 0
    
def armstrong(num,c):
    if(num!=0):
        a=num % 10
        return (a**c)+ armstrong(num//10,c)
    else:
        return 0
    

num = int(input("Enter number: "))
c = count(num)
ans = armstrong(num,c)
if num == ans:
   print("Armstrong number")
else:
    print("Not armstrong")
