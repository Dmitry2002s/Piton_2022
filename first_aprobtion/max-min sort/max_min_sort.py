A = int(input())
B = int(input())
C = int(input())
min = 0
max = 0
mid = 0 
if(A<=B and A<=C): 
    min = A
    if(B<C):
        max = C 
        mid = B 
    else: 
        max = B 
        mid = C 
        
elif (B<=C and B<=A): 
    min = B
    if(C<A):
        max = A 
        mid = C 
    else: 
        max = C 
        mid = A
        
elif (C<=A and C<=B): 
    min = C
    if(A<B):
        max = B 
        mid = A 
    else: 
        max = A 
        mid = B
print(max)
print(min)
print(mid)
