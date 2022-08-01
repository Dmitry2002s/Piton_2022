count = int(input())
A = count%10
if(A==0 or 5<=A):
    print(str(count) + " программистов")
elif(2<=A<=4 ):
    
    if(10 <=count % 100 <=20 ):
        print(str(count) + " программистов")
    else: 
        print(str(count) + " программиста")
else:
    if(10 <=count % 100 <=20 ):
        print(str(count) + " программистов")
    else: 
        print(str(count) + " программист")