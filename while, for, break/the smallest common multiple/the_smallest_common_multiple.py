A = int(input())
B = int(input())
if (A>B): 
    p = A
    c = B
else: 
    p = B
    c = A
min = p 
while (min % c) != 0: 
    min+=p 
print(min) 

