# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 08:37:37 2019

@author: CEC
"""

def isPrime():
    while True:
        x=input("Ingrese el numero: ")
        if x == 'q' or x == 'quit':
            break
        else:
            isPrime1(int(x))
            break
            

isPrime()


def isPrime1(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

print (isPrime(int(n=input("Ingrese el numero:"))))


for i in range(1,100):
    if isPrime(i + 1):
        print(i + 1, end=" ")

print()
                
        
num = 123
lista = magic(num)

print(lista)     
   