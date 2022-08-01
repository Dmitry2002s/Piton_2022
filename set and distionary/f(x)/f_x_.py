def f(x): 
    return x*-1 
n = int(input())
d = {}
count = {}
m = 0 
List = []
while m < n: 
    m+=1  
    argument = int(input())
    if argument not in d: 
        d[argument] = f(argument)
    List.append(argument) 
for i in List: 
        print(d[i])