
a = [int(i) for i in input().split()]
a.sort()
i = 0 
lenght = len(a)
k = 1 
while (i < lenght ):
    if(i+k < lenght):
        if(a[i]==a[i+1]):
            print(a[i], end = ' ')
            while a[i] == a[i+k]:
                if(i+k==lenght-1):
                    break 
                k+=1 
    i = i+k 
    k = 1 
