## TEMPORAL SCHEMES
from System_equations.System_equations import newton
from Cauchy_Problem.Cauchy_Problem import Cauchy_Problem
#from scipy.optimize import newton, fsolve
from numpy import size, linspace

# Explicit Euler Scheme
def Euler(U, delta_t, F, t):

    return U + delta_t*F(U,t)
    

# Implicit Inverse Euler Scheme
def Inverse_Euler(U, delta_t, F, t):
    def func_I(x):
        return x - U - F(x,t)*delta_t

    return newton(func_I, U)


# Runge-Kutta-4 Scheme
def Runge_Kutta_4(U, delta_t, F, t):

    k1 = F(U, t)
    k2 = F(U + delta_t*k1/2, t + delta_t/2)
    k3 = F(U + delta_t*k2/2, t + delta_t/2)
    k4 = F(U + delta_t*k3, t + delta_t)

    return U + delta_t*(k1 + 2*k2 + 2*k3 + k4)/6


# Crank Nicolson Scheme
def Crank_Nicolson(U, delta_t, F, t):
        def func_CN(x):
            return x - U - (F(x,t) + F(U,t))*delta_t/2

        return newton(func_CN, U)


#Leap-frog Scheme
def Leap_Frog(U2, U1, delta_t, F, t):

    return U1 + 2*delta_t*F(U2,t)