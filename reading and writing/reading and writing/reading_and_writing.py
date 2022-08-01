string = open('C:\\programming\\test.txt','r+')
s = string.readline() 
symbol = ''
lenght = len(s) -1 
t = 0 
q = 0 
m = 1 
string.write('\n')
while t < lenght  : 
    symbol = s[t] 
    while (s[t+m]) < 'A' :
        q = q*10 + int(s[t+m]) 
        m+=1 
        if(t+m>=lenght):
            break 
    t = t + m 
    m = 1
    string.write(symbol* q)
    q = 0 
    if(t+m>=lenght):
        break 

string.close() 