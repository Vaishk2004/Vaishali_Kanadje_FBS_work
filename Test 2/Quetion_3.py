#Total cost of fencing the field
radius = 20
length = 50
breadth = 40
peri_circle = (2* 3.14 * radius)* 0.5
peri_rect = (2*(length + breadth))*0.5

cost = (peri_circle + peri_rect) * 35

total_cost = cost * 5

print("The Total cost of fencing the field: ",total_cost)
