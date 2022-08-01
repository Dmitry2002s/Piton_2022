def square (A,B,C) : 
    p = (A+B+C)/2 
    return (p*(p-A)*(p-B)*(p-C))**0.5 


Operation = {
    "Прямоугольник" : lambda A,B: A*B, 
    "Круг " : lambda A : 3.14*(A**2), 
    "Треугольник" : lambda A ,B ,C : square(A,B,C) 
    }
X = input() 
A = int(input())
print(operation[X](A) ) 
