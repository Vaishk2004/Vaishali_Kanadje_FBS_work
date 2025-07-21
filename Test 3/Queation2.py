# write program to calculate sum of series
# 1/1!+2/2!+3/3!+......N/N!

num = int(input("Enter number: "))
sum = 0
for i in range(1,num+1):
    fact = 1
    for x in range(1,i+1):
        fact = fact*x
    sum = sum+(i/fact)

print("Sum of series: ",sum)
    