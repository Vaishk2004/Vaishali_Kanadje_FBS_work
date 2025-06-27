# Program to find the simpe intrest
p = int(input("Enter principle amount:"))
time = int(input("Enter no. of years:"))
rate = float(input("Enter rate of interest:"))

interest = (p*time*rate)/100

print("Simple interest: ", interest)