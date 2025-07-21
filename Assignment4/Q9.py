#Program to print all numbers in range divisible by a given number
start = int(input("Enter start point: "))
end = int(input("Enter end point: "))
num = int(input("Enter Number: "))

for i in range(start,end+1):
    if(i % num == 0):
        print(i)