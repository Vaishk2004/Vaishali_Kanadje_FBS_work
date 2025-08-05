# write a program to find reverse of number

def reversNum(num):
    rever = 0
    while(num!=0):
        a = num % 10
        num = num // 10
        rever =(rever*10)+a
    return rever

num = int(input("Enter number: "))
print("Revers number: ",reversNum(num))
