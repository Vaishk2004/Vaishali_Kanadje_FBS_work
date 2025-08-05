#write a program to check given number is armstrong number or not
def countDigit(num):
    count = 0
    while(num!=0):
        num = num // 10
        count+=1
    return count

def armstrongNum(num):
    num_dig = countDigit(num)
    sum = 0
    while(num!=0):
        a = num % 10
        num = num // 10
        sum = sum + (a**num_dig)
    return sum

num = int(input("Enter number: "))
ans = armstrongNum(num)
if(num == ans):
    print("Armstrong number")
else:
    print("Not armstrong")

