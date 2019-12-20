# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 09:44:03 2019

@author: CEC
"""

file=open("devices.txt","a")
while True:
    newItem = input("Ingrese un nuevo item: ")
    if newItem == 'exit':
        print("todo Listo!!")
        break
    else:
        file.write(newItem + "\n") 
file.close()

file=open("devices.txt","r")
for item in file:
    item=item.strip()
    print(item)

file.close()

