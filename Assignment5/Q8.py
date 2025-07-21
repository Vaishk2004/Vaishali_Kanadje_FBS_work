#Solve the series

# # 1. 1!+2!+3!....n!
print("1.Sum of factorial upto the n.")
num = int(input("Enter number: "))

for i in range(1,num+1):
    fact = 1
    sum = 0
    for x in range(1,i+1):
       fact = fact * x
       sum = sum + fact
    
print("Addition of factorial: ",sum)


# # 2. n+n^2+n^3...+n^n
print("2.n+n^2+n^3...+n^n")
num = int(input("Enter Number: "))
sum = 0 
for i in range(1,num+1):
    ans = num ** i
    sum = sum + ans
print("Addition: ",sum)


# 3. Sum of geometric series from 1 to n where common ration is 2
print("Sum of geometric series from 1 to n where common ration is 2")
a = 1
n = int(input("Enter number of terms: "))
r = 2
sum = 0
for i in range(n):
    ans = a * (r ** i)
    sum += ans
print(sum)

# 4.S = a+a2/2+a3/3+....a10/10
print("4.S = a+a2/2+a3/3+....a10/10")
num = int(input("Enter number: "))
sum = 0 
for i in range(1,11):
    ans=(num**i)/i
    sum = sum + ans
print("Addition: ",sum)


# 5. x-x2/3+x3/5-x4/7+.....to n term
print(" 5. x-x2/3+x3/5-x4/7+.....to n term3")
x = int(input("Enter number: "))
n = int(input("Enter n term: "))
sum = 0
for i in range(1,n+1):
    term =(x ** i)/(2 * i)-1
    if(i % 2 == 0):
        sum -= term
    else:
        sum += term

print(sum)
