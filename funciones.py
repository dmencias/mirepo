# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 20:13:17 2019

@author: CEC
"""
def hi(name):
    print("hola,", name)

hi(input("Ingrese su nombre:"))

def holatodos(nombre1, nombre2):
    print("Hola,", nombre2)
    print("Hola,", nombre1)

holatodos("Sebastian","Carlos")

def adress(street,city, postalCode):
    print("Su dirección es: ",street, "St.,", city,postalCode)

s = input("Calle: ")
pC = input("Codigo Postal:")
c = input("ciudad:")

adress(s, c, pC)

#Ex. 1

def subtra(a,b):
    print(a - b)

subtra(5, 2)
subtra(2, 5)

#Ex.2

def subtra(a,b):
    print(a - b)

subtra(a=5, b=2)
subtra(b=2, a=5)

def multiplicacion(a, b):
    return a * b

print(multiplicacion(3,4))

def  deseos():
    return "Feliz cumpleaños"

var = deseos()

print(var)


#Uso de listas en funciones con paso de parametros

def holatodomundo(myList):
    for name in myList:
        print("Hola,", name)

holatodomundo(["Adam","Jhon","Lucy"])


def createList(n):
    myList=[]
    for i in range(n):
        myList.append(i)
    return myList

print(createList(5))


#Funciones Lambda

def a(x, y):
    return x + y

b = lambda x, y: x + y

print(b(1,5))


def a(x):
    return "Hola Mundo",x

print(a(2))


revertir = lambda cadena: cadena[::-1]

print(revertir("DavidMencias"))

#Para determinar si un numero es par o impar

impar = lambda num: num%2 != 0

print(impar(6))

#Duplicar un numero

doblar = lambda num: num*2

print(doblar(100))

seq = ['data','salt','dairy','cat','dog']

print[list(filter(lambda word: word[0]=='d',seq))]



















