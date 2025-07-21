num = int(input("Enter number of employe: "))
total = 0
for i in range(1,num+1):
    total_sal = 0
    basic_sal = int(input("Enter basic salary: "))
    if(basic_sal<20000):
        da= basic_sal* 0.1 #da = 10%
        ta = basic_sal * 0.12   # ta = 12%
        hra = basic_sal * 0.15  # hra = 15%
    else:
        da= basic_sal* 0.15 #da = 15%
        ta = basic_sal * 0.18   # ta = 18%
        hra = basic_sal * 0.20  # hra = 20%

    total_sal = basic_sal + da + ta + hra
    print("Salary of emplayee: ",total_sal)
    total = total+total_sal

print("Total salary of all employe: ",total)


