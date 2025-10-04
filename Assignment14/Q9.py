#Python program to find the unique combination of 3 numbers from list numbers ,adding upto a target number

list1 = [2,4,5,6,7,4,9,1,2,4,3,4]

target_num = int(input("Enter the target number: "))

uniq_comb = set()

for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        for k in range(j+1,len(list1)):
            sum =list1[i] + list1[j] + list1[k]
            if sum == target_num:
                uniq_comb.add(tuple((list1[i],list1[j],list1[k])))
            
print("Unique combination of numbers: ",uniq_comb)