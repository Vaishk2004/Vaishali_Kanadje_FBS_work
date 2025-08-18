total_coin = int(input("Enter total number of coin: "))
number = []
for i in range(total_coin-1):
    number.append(int(input("Enter number printed on coin: ")))

print(number)
dict1 ={}
for i in number:
    if i in dict1:
        dict1[i]+=1
    else:
        dict1[i] = 1


for k in dict1:
    if dict1[k] %2 != 0:
        print("The coin is missing : ",k)