A = int(input())
if (A % 4 ==0) :
    if(A % 100 ==0) : 
        if(A%400 == 0): 
            print("Високосный")
        else: 
            print("Обычный")
    else: 
        print("Високосный")
else: 
    print("Обычный")
