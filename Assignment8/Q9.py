#write a program to check entered number is palindrome or not

def palindrome(num):
    rever = 0
    while(num!=0):
        a = num % 10
        num = num//10
        rever =(rever*10)+a
    return rever


num = int(input("Enter number: "))
temp = num
ans = palindrome(num)
if( temp == ans):
    print("Palindrome number")
else:
    print("Not Palindrome")
