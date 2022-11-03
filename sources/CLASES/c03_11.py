## WRAPPERS AND DECORATORS
from time import perf_counter
import tracemalloc

def simple_decorator(f):
    
    def wrapped_function(x):

        print("Function name:", f.__name__) # Saca el nombre de la función

        print("Output =", f(x)) # Saca el resultado de la función 

        return f(x)

    return wrapped_function



## Debugging
# Para una función de la cual no se el número de argumentos, ni el tipo

def debugging(f):

    def debug_f(*args, **kwargs): # * = Puntero a una tupla de argumentos, ** = parejas key-word

        print("Input arguments of function: " + f.__name__)

        for i in range(len(args)):
            print("i = ", i, "value = ", args[i] )

        for key, value in kwargs.items():
            print(key, "=", value)

        r = f(*args, **kwargs)

        print("Return value = ", r)

        return r

    return debug_f


            


## Profiling


def profiling(f): # Necesito importar la biblioteca

    def profiling_f(*args, **kwargs): # * = Puntero a una tupla de argumentos, ** = parejas key-word

        tracemalloc.start()
        start_time = perf_counter()
        r = f(*args, **kwargs)
        finish_time = perf_counter()
        current, peak = tracemalloc.get_traced_memory()

        print("Memory = ", current/(10**6), "MB")
        print("CPU time = ", finish_time - start_time, "seconds")
        
        tracemalloc.stop()
       
        return r

    return profiling_f


## Exception

def exceptions(f):

    def exceptions_f(*args, **kwargs):

        try:
            return f(*args, **kwargs)

        except:
            print("WARNING")
            exit

    return exceptions_f


## Ejemplo

@exceptions
@simple_decorator # Decoro la función con todos los decorators que quiera apilados
@debugging
@profiling
def f(x):

    return x**2

y = f(2) # ó y = f(x = 2)

