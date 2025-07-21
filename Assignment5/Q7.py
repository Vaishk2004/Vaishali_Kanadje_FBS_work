#Program to print first n prime number
num = int(input("Enter number: "))
for i in range(1,num+1):
    for x in range(2,i):
        if(i % x == 0):
            break
    else:
        print(i)