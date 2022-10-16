from numpy import array, product # No importar de Math porque no es vectorial

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

# EJEMPLO DE FILTRADO

y = array([1,2,3,4,5])
y1 = y[y<=3] # Coge los elementos menores o iguales a 3, muy compacto

def f(x):
    return x<=3

y1 = array(list(filter(f,y))) # Filter devuelve un objeto que hay que pasar a un array (primero a una lista), demasiado largo

# EJEMPLO REDUCE

y = array([1,2,3,4])
print(product(y)) # sum, product, norm, all, any, max, find ..... 

###########################################################################################################

# OVERLOADING - SOBRECARGA

# Sobrecarga de operadores
class dual_number: # Una clase tiene un constructor y las funciones u operaciones

    def __init__(self, x, y): # El constructor
        self.x = x
        self.i = y

    def __add__(self, z):
        
        return dual_number(self.x + z.x, self.y + z.y)

z1 = dual_number(1,1) #Se instancia un elemento de la clase
z2 = dual_number(2,2)

z3 = z1 + z2 #Sintactic sugar, escribir las cosas de manera "amigable"

# Sobrecargar el problema de Cauchy con variable compleja, se usa en la región de estabilidad, U vector columna de complejos













