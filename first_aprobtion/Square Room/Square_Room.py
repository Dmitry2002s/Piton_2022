A = input() 
if(A=="прямоугольник"): 
    a = int(input())
    b = int(input())
    print(a*b)
elif(A == "круг"):
    r = int(input())
    print(3.14*r**2)
elif(A == "треугольник"):
    a = float(input())
    b = float(input())
    c = float(input())
    p = float((a+b+c)/2) 
    result = ((p*(p-a)*(p-b)*(p-c))**0.5)  
    print(result)
