d = { }
words  = [str(i) for i in input().upper().split()] 
for i in words : 
    if i in d : 
        d[i]+=1 
    else : 
        d[i] = 1
for i in d: 
    print (i +' ' +  str(d[i]) ) 
 