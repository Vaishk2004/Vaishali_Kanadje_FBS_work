#To check given number is Perfect number or not
num = int(input("Enter Number: "))
sum = 0

for i in range(1,num):
    if(num % i == 0):
        sum = sum + i
    

if(num == sum):
    print("Perfect number")
else:
    print("Not perfect number.")


