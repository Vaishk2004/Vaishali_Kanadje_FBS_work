# sum of all prime number between 1 to n
def sumPrime(num):
    sum = 0
    for i in range(2,num+1): # 1 is not prime number
        for x in range(2,i):
            if(i % x == 0 ):
                break
        else:
            sum = sum + i

    return sum  

num = int(input("Enter number: "))
print("Sum of all prime number: ",sumPrime(num))     
         