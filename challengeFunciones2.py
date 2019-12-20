# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 08:37:37 2019

@author: CEC
"""



def isYearLeap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
    
    
def daysInMonth(year, month):
    if year < 1500 or month < 1 or month >12:
        return None
    days=[31,28,30,31,30,31,30,31,30,31,30,31]
    res = days[month-1]
    if month == 2 and isYearLeap(year):
        res = 29
    return res
 
def dayOfYear(year, month, day):
    meses = [2,4,6,9,11]
    if year < 1500 or month <1 or month > 12 or day <1 or day > 31:
        return "Fecha erronea"
    elif not isYearLeap(year) and month == 2 and day > 28:
        return "Fecha erronea"
    elif month in meses and day > 30 :
        return "Fecha erronea"
    days = 0
    for i in range (1,12+1):
        days += daysInMonth(year,i)
        #print (i, daysInMonth(year,i))
    return days


print(dayOfYear(2017,1,30))
