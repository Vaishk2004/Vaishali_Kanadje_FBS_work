#Calculate the total salary of employee based on basic, da=10% , ta=12% , hra=15%

basic = int(input("Enter the basic salary of the Employee:"))
da = 0.10 * basic
ta = 0.12 * basic
hra = 0.15 * basic

total_salary = basic + da + ta + hra

print("The Total salary of Employee is :",total_salary)