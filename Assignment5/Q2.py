#Enter th number of student for those student enter the marks of 5 subject and calculate percentage .
# Display percentage and average percent of student
num = int(input("Enter number of student: "))

avg = 0
for i in range(1,num+1):
    sum = 0
    for x in range(1,6):
        mark = int(input("Enter the marks: "))
        sum = sum + mark
    per = (sum/500)*100
    print(per,"%")
    avg = avg+ per

avrg = avg / num
print("Average percentage of student: ",avrg)
        