# Use nested list comprehension  to find all of the numbers from 1-1000 that are divible by any single unit

number = [num for num in range(1,1001) if any(num % div ==0 for div in range(2,9))]

print(number)