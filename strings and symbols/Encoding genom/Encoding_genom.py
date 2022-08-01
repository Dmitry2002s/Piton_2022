string = input ()
m = 0 
k = string[0]
i = k
position = 0 
for i in string :
    if(i==string[position]):
        m+=1
    else:
        print(k+str(m), end = '')  
        position += m
        if(position == len(string)):
           break 
        k = string[position]
        m = 1   
print(i+str(m))  

        
    