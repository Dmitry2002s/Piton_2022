A = int(input())
B = int(input())
C = int(input())
D = int(input())
D += 1
B += 1 
print('\t',end = '')
for j in range(C,D,1):
    print(str(j)+'\t', end ='') 
print()
for i in range(A,B,1): 
    print(str(i)+'\t', end='')
    for j in range(C,D,1) : 
        print ( str(i*j)+'\t'  , end=''), 
    print()