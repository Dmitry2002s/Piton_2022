number = int(input())
A = number%1000
B = int(number/1000)
a1 = int(A/100)
a2 = int(A%100/10)
a3 = int(A%10)
b1 = int(B/100)
b2 = int(B%100/10)
b3 = int(B%10)
if(a1+a2+a3 == b1 +b2 + b3): 
    print("Счастливый")
else:
    print("Обычный")
