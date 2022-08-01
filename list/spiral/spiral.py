a = int(input())
mas = [[0]*a for i in range(a)]
s= 1
i = 0 
j = 0 
i_= 1 
j_= 1
while(s<=a**2): 
    while (j<a and j>=0):
        mas[i][j] = s 
        s+=1 
        if(-1>j+j_ or j+j_>=a or mas[i][j+j_] != 0):
            i+=i_ 
            break 
        j = j+j_ 
    j_*=-1 
    if(s<=a**2):
        while(i<a and i>=0 ): 
            mas[i][j] = s 
            s+=1 
            if(-1>i+i_ or i+i_>=a or mas[i+i_][j] != 0 ):
                j+=j_
                break 
            i = i+i_ 
        i_*=-1 
for i in mas: 
    for j in i: 
        print(j, end = ' ')
    print()
    

