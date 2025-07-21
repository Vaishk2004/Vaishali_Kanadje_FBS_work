#To find which number are divisible by 7 and and multiple of 5 in given range
start = int(input("Enter start point: "))
end = int(input("Enter end point: "))

for i in range(start,end+1):
    if(i % 7 == 0 and i % 5 == 0):
        print(i)
