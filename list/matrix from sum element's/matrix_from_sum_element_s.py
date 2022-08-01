a = input().split()
i = 0 
j = 0 
b = []
while a != ['end']:
    b.append(a) 
    a = input().split() 
print()
с = [] 
lenght = len(b) 
witdh = len(b[0])
c = [[0]*witdh for i in range(lenght)]
i_1 = 0 
for i in c: 
    j_1 = 0 
    for j in i:
        j = 0
        if(j_1+1==len(i)):
            j+=int(b[i_1][0])
        else: 
            j+=int(b[i_1][j_1+1])
        if(j_1-1==-1):
            j+=int(b[i_1][len(i)-1])
        else:
            j+=int(b[i_1][j_1-1])
        j+=int(b[(i_1+1) % len(c)][j_1])
        j+=int(b[i_1-1][j_1])
        c[i_1][j_1]=j 
        j_1+=1 
    i_1+=1 
for i in c: 
    for j in i: 
        print(j, end = ' ')
    print()
