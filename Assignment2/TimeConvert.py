#Convert the given time into the seconds
hours = int(input("Enter the Hours:"))
min = int(input("Enter the minutes:"))
sec = int(input("Enter the seconds:"))

hours = hours * 60 * 60
min = min * 60
second = hours + min + sec

print("The time converted into the seconds:",second)