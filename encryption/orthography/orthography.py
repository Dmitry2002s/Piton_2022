a = int( input() )  
orf = set()
err = set()
while(a > 0 ):
    word = input() 
    orf.add(word.lower()) 
    a-=1 
a = int(input()) 
while(a > 0):
    string = str(input())
    length = len(string)
    i = 0 
    exp = ''
    while (i < length):
        while(i < length and string[i] != ' ') : 
            exp += string[i]
            i+=1
        exp = exp.lower()
        if(exp not in orf and exp not in err ):  
            err.add(exp) 
        exp = ''
        i+=1
    a-=1 
for i in err : 
    print(i)
