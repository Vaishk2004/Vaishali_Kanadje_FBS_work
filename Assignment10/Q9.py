#Write a program having n number of element in list 
# and find out even and odd number
# Create seprate list for even and odd number
list1 = []
n = int(input("Enter the list length:"))
for i in range(n):
    num = int(input())
    list1.append(num)
print(list1)
       
evenlist = []
oddlist = []

for i in list1:
    if i % 2 == 0:
        evenlist.append(i)
    
    else:
        
        oddlist.append(i)

print("Even List:",evenlist)
print("Odd List: ",oddlist)
