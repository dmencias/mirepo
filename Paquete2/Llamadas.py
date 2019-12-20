import math

x = float(input("Enter x: "))
y = math.sqrt(x)

print("La raiz cuadrada de", x, "es igual a", y)

list=[]
x = list[0]


try:
    print("1")
    x = 1/0
    print("2")
except:
    print("Algo salió mal")
    
print("3")

try:
    x = int(input("Ingrese un numero: "))
    y  = 1/x
    print(y)
    
except ZeroDivisionError:
    print("No puedes dividir para cero, lo siento")

except ValueError:
    print("Debe ingresar un valor entero")

except:
    print("Algo salió mal")

print("THE END")


try:
    y  = 1/0
except ArithmeticError:
    print("Problema aritmetico")
except ZeroDivisionError:
    print("division para cero")

    
print("EL FIN")

def badFun(n):
    try:
        return 1 /n
    except ArithmeticError:
        print("Problema Aritmetico")
    return None

badFun(0)
print("El Fin")


def badFun(n):
    return 1/n
try:
    badFun(0)
except ArithmeticError:
    print("Que ocurrio?. Una excepción se levantó")

print("EL FIN")






































