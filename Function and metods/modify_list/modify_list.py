
def modify_list(l):
    k = 0 
    lenght = len(l)
    while k < lenght:
        if l[k]%2==0 : 
            l[k]/=2 
            k+=1 
        else: 
            l.remove(l[k]) 
            lenght-=1 
        
lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst) 