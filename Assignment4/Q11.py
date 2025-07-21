# check the number is strong number or not
num = int(input("Enter number: "))
sum = 0
temp = num
while(num != 0):
    a = num % 10
    num = num // 10
    
    fact = 1
    for i in range(1,a+1):
        fact = fact * i
    sum = sum + fact

if(sum == temp):
    print("Strong number")
else: 
    print("Not strong")
        