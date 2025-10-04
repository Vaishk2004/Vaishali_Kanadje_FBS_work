# Program to detect two strings are Anagrams
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")


if len(str1) != len(str2):
    print("Not Anagrams (different lengths)")
else:
    dict1 = {}
    dict2 = {}
     
    for i in str1:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1

    for i in str2:
        if i in dict2:
            dict2[i] +=1
        else:
            dict2[i] = 1

    if dict1 == dict2:
        print("Strings are anagrams")
    else:
        print("Strings not Anagrams")
    

            
    
     

        


    