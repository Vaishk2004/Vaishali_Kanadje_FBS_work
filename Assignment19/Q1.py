# Comprehension 
#find all numbers from 1-1000 that are divisible by 8

number = {x for x in range(1,1001)if x % 8 ==0}

print(number)