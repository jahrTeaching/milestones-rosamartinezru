## TEMPORAL SCHEMES
from Resources.System_equations import newton
from scipy.optimize import newton, fsolve


# Explicit Euler Scheme
def Euler(U, delta_t, F, t):

    return U + delta_t*F(U,t)
    

# Implicit Inverse Euler Scheme
def Inverse_Euler(U, delta_t, F, t):
    def func_I(x):
        return x - U - F(x,t)*delta_t

    return fsolve(func_I, U)


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

        return fsolve(func_CN, U)

