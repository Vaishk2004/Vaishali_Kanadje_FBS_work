# To find years , weeks and days from the given days
days = int(input("Enter the number of days :"))

year = days // 365
days = days % 365 #calculate the remaining days
weeks = days / 7
days = days  % 7

print("Years:",year, "Weeks:",weeks , "Days:",days)