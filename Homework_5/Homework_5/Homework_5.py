from array import array
from lib2to3.pgen2.token import EQUAL
from symtable import Symbol

import sympy 
from sympy import simplify,integrate , sin, cos, ln ,Matrix,MatrixSymbol, zeros 
from sympy.abc import x 
def function(f,y):# Значение функции в точке x:
    return f.evalf(subs = {x : y})
def f_diff(f,n):
    while(n!=0):
        f = f.diff(x)
        n-=1 
    return f 

def MAX_f(f ,a,b): 
    h = 1/100
    i = 0
    result = -10000000
    while(a+i*h<b):
        if(function(f,(a+i*h))>result):
            result = function(f,a+i*h)
        i+=1 
    return result 

def SKF_Simpson(f,a ,b ):
    F = simplify(f*p) 
    m = 100 
    h = (b-a)/(m)
    result = 0
    for j in range(0,m): 
        result += function(F,a+j*h) + 4*function(F, a+(j+1/2)*h) + function(F,a+(j+1)*h)
    result *= h/6
    return result 

def moments(p,a: float ,b : float ,n : int ):
    result = [] 
    for i in range(0,n) : 
        result.append(SKF_Simpson(p*x**i,a,b))
    return result 
def nodes(a,b , n ) : 
    result = [] 
    h = abs(b-a)/(n-1)
    for i in range(0,n ): 
        result.append(a+i*h) 
    return result 



choise = 0
f = x 
p = x 
a = 1 
b = 2 
while(True): 
    print('f(x) = ' + str(f) )
    print('p(x) = ' + str(p) )
    print('a = ' + str(a) ) 
    print('b = ' + str(b) ) 
    print('\n1 - изменить функцию \n2 - изменить вес\n3 - изменить пределы интегрирования' )
    print('4 - меню интегрирования ')
    print('0 - выход')
    choise = int(input('Введите число \n')) 
    if choise == 1 : 
        f = simplify(input('Введите функцию') )  
    elif choise == 2 : 
        p = input('Введите вес') 
    elif choise == 3 : 
        a = float(input('Введите левую границу'))
        b = float(input('Введите правую границу'))
    elif choise == 4 :
        while(True): 
            print('1 - получить точное значение ') 
            print('0 - вернуться в главное меню')
            choise = int(input('Введите номер действия'))
            if choise == 1 : 
                print(f"'Точное значение  интеграла на [{a},{b}] \n f(x) = {str(f)} \n Интеграл = {str(SKF_Simpson(f*p,a,b,) )}  ")
            elif choise == 2 : 
                print(f"Умные вычисления")
                n = int(input('Введите количество узлов'))
                MOMENTS = moments(p,a,b,n)
                print('\n полученные моменты весовой функции')
                for i in range(0,len(MOMENTS)) : 
                    print(i,MOMENTS[i]) 
                NODES = nodes(a,b,n) 
                print('Узлы функции', NODES) 
                line = []
                MATRIX_nodes = zeros(n,1) 
                j = 0 
                for i in NODES : 

                    MATRIX_nodes[j] = i 
                    j+=1 
                A = zeros(n,n) 
                for k in range(0,n): 
                    for i in range(0,n):
                        A[k,i] = NODES[k]**i 

                print('Матрица для решения \n' , A)
                m = MatrixSymbol('s', n,1).as_explicit()
                print(m)
                print('Матрица узлов' , MATRIX_nodes) 
                ##EQUAL(A*m = )
                


            elif choise == 0 : 
                break 
            else : 
                print('Ввод некорректен, повторите')
    elif choise == 0 : 
        break 
    else : 
        print('НЕВЕРНЫЙ ВВОД, повторите')