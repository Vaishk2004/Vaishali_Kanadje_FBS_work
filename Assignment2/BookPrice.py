#The selling price of book based on the cost price and discount
cost_price = int(input("Enter the cost price of book:"))
discount = int(input("Enter the discount:"))

dis_amount = discount *(cost_price/100)
sell_price = cost_price - dis_amount

print("The Cost price is:",cost_price)
print("The Selling price is:",sell_price)