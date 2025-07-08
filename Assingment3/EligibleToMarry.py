#To check if person is eligible for marry or not
gender = input("Are you male or female: ")
age = int(input("Enter your age: "))

if(gender == "male" and age >= 21):
    print("You are eligible for Marry.")

elif(gender == "female" and age >= 18):
    print("You are eligible for Marry.")

else:
    print("You are not Eligible for marry.")