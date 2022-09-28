
from numpy import array, zeros, linspace
from scipy.optimize import fsolve

#Kepler Function
def Kepler_F(U, t):
    r = U[:-2] #Position
    drdt = U[2:] #Velocity
    norm = (r[0]**2 + r[1]**2)**0.5 

    return array([ drdt[0], drdt[1], -r[0]/(norm**3), -r[1]/(norm**3)])


#Problema de Cauchy
def Cauchy_Problem(F, t, U_0, Temporal_Scheme):

    N = len(t) - 1
    N_0 = len(U_0)
    U = array(zeros([N+1, N_0]))

    U[0,:] = U_0

    for i in range(N):

        delta_t = t[i+1] - t[i]
        U[i+1, :] = Temporal_Scheme(U[i, :], delta_t, F, t[i])

    return U


#Explicit Euler Scheme
def Euler(U, delta_t, F, t):

    return U + delta_t*F(U,t)
    

#Implicit Inverse Euler Scheme
def Inverse_Euler(U, delta_t, F, t):
    def func_I(x):
        return x - U - F(x,t)*delta_t

    return fsolve(func_I, U)


#Runge-Kutta-4 Scheme

def Runge_Kutta_4(U, delta_t, F, t):

    k1 = F(U, t)
    k2 = F(U + delta_t*k1/2, t + delta_t/2)
    k3 = F(U + delta_t*k2/2, t + delta_t/2)
    k4 = F(U + delta_t*k3, t + delta_t)

    return U + delta_t*(k1 + 2*k2 + 2*k3 + k4)/6


#Crank Nicolson Scheme
def Crank_Nicolson(U, delta_t, F, t):
        def func_CN(x):
            return x - U - (F(x,t) + F(U,t))*delta_t/2

        return fsolve(func_CN, U)

    
   #Orbital specific energy
def Specific_energy(U,N):
    e = array(zeros(N+1))

    for i in range(0,N):

        mu = 3.986e14
        E_mec = (U[i,2]**2 + U[i,3]**2)/2
        E_pot = mu/((U[i,0]**2 + U[i,1]**2)**(1/2))
        e[i] = E_mec - E_pot

    return e

        
