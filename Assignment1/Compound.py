#To find the compound interest
p = int(input("Enter principle amount:"))
time = int(input("Enter no. of years:"))
rate = float(input("Enter rate of interest:"))

compound_int = p*(1+rate)**time 

print("Compound Interest:", compound_int)