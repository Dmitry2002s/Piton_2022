def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
enc = {} 
a = input() 
b = input()
i = 0 
lenght = len(a)
while i < lenght:
    enc[a[i]] = b[i] 
    i+=1 
c = input() 
d = '' 
for m in c : 
    d += enc[m]
print(d)
c = input()
d = '' 
for m in c: 
    d += get_key(enc, m)
print(d) 
