#sum of all odd number between 1 to n
def sumOdd(num):
    sum = 0
    for i in range(1,num+1):
        if(i % 2 != 0):
            sum = sum + i
    return sum

num = int(input("Enter number: "))
print("Sum of all odd number: ",sumOdd(num))