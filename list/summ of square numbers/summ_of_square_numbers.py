a = []
sum = 0 
a.append(int(input()))
sum += a[0]
i = 1 
while sum != 0 : 
    a.append(int(input())) 
    sum += a[i]
    i+=1
sum = 0 
for i in a : 
    sum += i**2
print(sum) 
