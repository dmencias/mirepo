# -*- coding: utf-8 -*-
"""
@author:  Fausto Paredes, Victor Vimos
@country: Quito-Ecuador
"""

def fun(x,a,b):
    y=list(range(a,b,1))  

    for i in range(0,len(y)):
         r=y[i]
         if r==x: 
             a=1;
             break
         else:
             a=0;
    return a         

try:
    x=int(input("Ingrese el numero a buscar: "))
    a=int(input("Ingrese el limite inferior: "))
    b=int(input("Ingrese el limite superior: "))
    f=fun(x,a,b)
    if f==1:
        print("the value is: ",x)
    else:
        print("the value is not within permitted range ")
except ValueError:
    print("wrong input ")




            
