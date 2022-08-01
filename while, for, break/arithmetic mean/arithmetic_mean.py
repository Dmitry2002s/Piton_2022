A,B = int(input()), int(input()) 
if B%3==0: 
    B+=1
while(A % 3 != 0):
    A+=1 
j = 0
sum = 0 
for i in range(A,B,3):
    j+=1
    sum += i     
print (sum/j)

