from numpy import array # No importar de Math porque no es vectorial

# EJEMPLO DE FUNCIÓN IMPURA

counter = 0

def impure1(x):

    global counter # NO GLOBAL !! 

    counter += 1 # Es lo mismo que counter = counter +1

    return x + counter

print(impure1(10)) # Sale 11 de resultado

print(impure1(10)) # Sale 12 :(

# FUNCIÓN PURA -->  no tiene SIDE-EFFECTS, y siempre da el mismo resultado para los mismos argumentos de entrada
# Puede interaccionar con el "mundo exterior", hay algo que depende del estado de una de las variables

# NO MODIFICAR LOS ARGUMENTOS 

l = "k"

print(id(l))

def impure2(l):

    l += "c"

    print(id(l))

    return l

j = impure2(l)



t = "v"

print(id(t))

def impure3(t): # Esto NO es impura, no modifica el argumento

    t = t + "c"

    print(id(t))

    return t

v = impure2(t)

# FIBONACCI

def F(n): #Implementación recursiva
    if n ==1:
        return 1       
    if n == 2:
        return 1
    else:
        return F(n-1) + F(n-2) #Puedo llamar a la función dentro del return

print(F(10))

# EJEMPLO MAPPING

def f(x):

    return x**2

v = array([1, 2, 3])

#w = f(v) # Muy matemático, nos gusta más <3
#print(w) # Hace el cuadrado de cada una de las componentes

w = array(list(map(f,v))) #Map mapea f para todo v, tiene que crear una lista y luego un array, un poco rollo :(
print(w)






