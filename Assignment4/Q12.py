#Armstrong number from range
start = int(input("Enter start point: "))
end = int(input("Enter end point: "))

for num in range(start,end+1):
    temp = num
    count = 0
    while(num != 0):
        num = num // 10
        count += 1
    
    num = temp
    sum = 0
    while(num != 0):
        a = num % 10
        num = num // 10
        sum = sum + (a ** count)

    if(sum == temp):
        print(temp)
    