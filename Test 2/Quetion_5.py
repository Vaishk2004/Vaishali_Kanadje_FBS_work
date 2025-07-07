#Total Bill of Product
pro1 = int(input("Enter the price of First Product: "))
pro2 = int(input("Enter the price of Second Product: "))
pro3 = int(input("Enter the price of Third Product: "))
pro4 = int(input("Enter the price of Forth Product: "))
pro5 = int(input("Enter the price of Fifth Product: "))

total = pro1 + pro2 + pro3 + pro4 + pro5
gst = total * 0.18

bill = total + gst

print("Total bill: ",bill)