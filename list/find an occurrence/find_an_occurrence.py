a = [int(i) for i in input().split()]
b = int(input()) 
count = a.count(b) 
if(count == 0): 
    print("Отсутствует")
else : 
    c = 0
    while(count != 0) :
        print(a.index(b,c), end = ' ')
        c = a.index(b,c)+1 
        count-=1 
        
        