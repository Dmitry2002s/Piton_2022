string = input()
string = string.upper() 
count = float(0)  
lenght = 0 
for t in string : 
    if t == "G" or t == "C" : 
        count +=1
    lenght+=1

print(count*100/lenght)