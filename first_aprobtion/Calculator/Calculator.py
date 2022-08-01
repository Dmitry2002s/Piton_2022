A = float(input())
B = float(input())
operation = str(input()) 
if(operation == "*"):
    print(A * B)
elif(operation == "/"):
    if(B==0):
        print("Деление на 0!")
    else:
        print(A / B)
elif(operation == "-"):
    print(A - B)
elif(operation == "+"):
    print(A + B)
elif(operation == "pow"):
    print(A ** B)
elif(operation == "div"):
    if(B==0):
        print("Деление на 0!")
    else:
        print(A // B)
elif(operation == "mod"):
    if(B==0):
        print("Деление на 0!")
    else:
        print(A % B)