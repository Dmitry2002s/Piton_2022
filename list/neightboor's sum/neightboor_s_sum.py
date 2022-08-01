a = [int (i) for i in input().split()]
b = []
k = 0 
lenght = len(a)
i = 0 
if lenght==1: 
    print(a[0])
else :
    while i < lenght : 
        if i == 0 :
            k = a[1] + a[lenght-1]
        elif i == lenght-1: 
            k = a[0] + a[lenght-2] 
        else: 
            k = a[i-1]+a[i+1]
        i+=1 
        b.append(k) 
    i = 0 
    while i < lenght : 
        print(str(b[i]) , end =' ')
        i+=1 
