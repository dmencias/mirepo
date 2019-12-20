# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 08:11:07 2019

@author: CEC
"""
rango_inferior = -10
rango_superior = 10


def control(valor_ingresado,rango_inferior,rango_superior):
    try:
        valor_ingresado = input("ingrese un valor entre -10 y 10:" )
        if int(valor_ingresado) < rango_superior and int(valor_ingresado) > rango_inferior:
            print(valor_ingresado) 
        else:
            print("El valor ingresado esta fuera del rango especificado")
    
    except ValueError:
        print("Debe ingresar un valor entero")



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
    
    
    
  
  y = list(range(1,10,1))
  
   x = list(range(1,10))

len(y)


        