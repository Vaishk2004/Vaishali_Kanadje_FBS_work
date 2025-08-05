# Write a program sum of n number using recursion
def sumNum(num):
    if(num == 1):
        return 1
    else:
        return num + sumNum(num-1)
    
num = int(input("Enter number: "))
print("Sum of number is :",sumNum(num))