#Calculate the Cost of Painting
int_area = int(input("Enter the area of interior wall:"))
ext_area = int(input("Enter the area of exterior wall:"))

int_cost = int(input("Enter the cost of interior wall:"))
ext_cost = int(input("Enter the cost of exterior wall:"))

cost = (8 * int_area ) * int_cost
cost2 = (8 * ext_area) * ext_cost

print("The Total Cost is",cost + cost2)