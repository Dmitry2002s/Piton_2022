string = open('C:\\programming\\test.txt','r+')
result = open('C:\\programming\\result.txt','r+')
s = string.readline()
while(s!= ''): 
    lenght = len(s)  
    i = 0
    a = 0 
    b = 0 
    c = 0 
    sum_a = 0 
    sum_b = 0 
    sum_c = 0 
    q = 0 
    while(s[i] >= 'A'): 
        i+=1 
    i+=1 
    while(s[i] != ';'):
        a = a*10 + int(s[i])
        i+=1 
    i+=1 
    while(s[i] != ';'):
        b = b*10 + int(s[i])
        i+=1
    i+=1 
    while(i < lenght and s[i] != '\n'):
        c = c*10 + int(s[i])
        i+=1 
    sum_a += a 
    sum_b += b 
    sum_c += c 
    i = 0 
    q += 1 
    s = string.readline() 
    result.write(str(round((a+b+c)/3,9)) + '\n')
    print((a+b+c) / 3 )
string.close() 
result.write(str(round(sum_a/q,9))  + ' ') 
result.write(str(round(sum_b/q,9)) + ' ') 
result.write(str(round(sum_c/q,9)) )
result.close() 
print(sum_a/q , sum_b/q , sum_c/q ) 