#Program to find the two finds two numbers whose product is maximum among all the pairs in given list of numbers. use set

list1 = [23,64,113,4,23,8,34,9,47,110,2,1]


max_pro = list1[0] * list1[1]
pair = ()

for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        product = list1[i] * list1[j]
        if  product > max_pro:
            max_pro =  product
            pair = (list1[i],list1[j])

print("Pair with maximum product:", pair)
print("Maximum product:", max_pro)

