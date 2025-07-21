#Program to check given number is armstrong or not
num = int(input("Enter number: "))
temp = num
count = 0
sum = 0
while(num !=0):
    a = num % 10
    num = num // 10
    count += 1

num = temp
while(num != 0):
    a = num % 10
    num = num // 10
    sum = sum + (a ** count)

if(sum == temp):
    print("Armstrong number.")
else:
    print("Not Armstrong")
