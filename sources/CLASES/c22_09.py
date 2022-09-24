#Factorial de n, programación imperativa (How to do it)
n = 6
f = 1

for i in range(1,n+1): #no llega hasta N si pongo range(1,n)
    f = f * i #Es una asignación, no una igualdad 

print("Factorial de n = ", f)

#Factorial de n, programación declarativa o funcional (What to do)
#n! = n*(n-1)!
#1! = 1

def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

print("Factorial de n = ", factorial(n))


#Scope
x = 1 #Variable entera global

def f1(y):
    global x #Le doy el carácter global o si no dará error , mejor no usarlo ¡NO!
    x = x + y #Se crea otra variable local que se llama x
    return x

print(id(x)) #Me da un identificador de x

def f2(y):
    x=3 #Aquí se crea una local x, por lo que sí da return , ¡NO local!
    x=x + y
    return x

print("f1 = ", f1(1))
print("f2 = ", f2(1))

#Para importar módulos:
#import numpy
#import numpy as np
#from numpy import array, zeros, linspace, sqrt <-- las matemáticas importarlas así


