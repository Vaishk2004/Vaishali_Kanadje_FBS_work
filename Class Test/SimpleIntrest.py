#The program to calculate simple interest
p = int(input("Enter the Principle Amount:"))
rate = float(input("Enter the rate:"))
time = int(input("Enter the time:"))

simple_int = (p * rate * time)/100

print("The Simple interest is :",simple_int)