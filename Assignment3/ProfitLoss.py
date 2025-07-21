#To calculate profit or loss
sell_price = int(input("Enter the selling price: "))
cost_price = int(input("Enter the Cost Price: "))

if(sell_price > cost_price):
    print("Profit is: ",sell_price - cost_price)

elif(sell_price < cost_price):
    print("Loss is: ",cost_price - sell_price)

else:
    print("Neither loss nor Profit")
