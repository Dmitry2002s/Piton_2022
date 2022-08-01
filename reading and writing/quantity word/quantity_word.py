string = open('C:\\programming\\test.txt','r+')
s = string.read().strip()
word = '' 
m = {}
k = s[0]
for k in s: 
    if k!=' ': 
        k = k.lower()
        word += k 
        continue
    elif word not in m : 
        m[word]=1 
    else : 
        m[word]+=1
    word=''
if word not in m : 
    m[word]=1 
    word = ''
else : 
    m[word]+=1
    word=''

max = 0 
for word in m.values() : 
    if word > max: 
        max = word 
string.write('\n')
for word,key  in m.items() : 
    if key == max: 
        string.write((word + ' ' + str(key))) 
        print(word, str(key))
        break 

