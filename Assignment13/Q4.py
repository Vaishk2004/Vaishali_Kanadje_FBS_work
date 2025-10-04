#Program to generate a dictionary that contains numbers (between 1 and n )in the form of (x,x*x)

power = {}
num = int(input("Enter number for range: "))
for x in range(1,num+1):
    k = x
    power[k]=x*x

print(power)