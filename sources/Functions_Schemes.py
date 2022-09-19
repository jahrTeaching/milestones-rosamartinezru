import numpy as np
from sympy import solve

#Kepler Function
def Kepler_F(U):
    r = U[:-2] #Position
    drdt = U[2:] #Velocity
    F =  np.concatenate(( drdt, - r / (np.linalg.norm(r)**3)), axis = None) 
    return F

#Explicit Euler Scheme
def Euler_Scheme(U, delta_t, N):
    for i in range(0,N):
        U[:,i+1] = U[:,i] + delta_t*Kepler_F(U[:,i])
    return(U)
    

#Implicit Inverse Euler Scheme
def Inverse_Euler(U, delta_t, N):
    for i in range(0,N):
        U1 = U[:,i]
        U[:,i+1] = np.nsolve(U2 - U1 - Kepler_F(U2)*delta_t, U2)
    return(U)


#Runge-Kutta-4 Scheme
def Runge_Kutta_4(U, delta_t, N):
    for i in range(0,N):
        k1 = Kepler_F(U[:,i])
        k2 = Kepler_F(U[:,i] + delta_t*k1/2)
        k3 = Kepler_F(U[:,i] + delta_t*k2/2)
        k4 = Kepler_F(U[:,i] + delta_t*k3)

        U[:,i+1] = U[:,i] + delta_t*(k1 + 2*k2 + 2*k3 + k4)/6
    return(U)


#Crank Nicolson Scheme
def Crank_Nicolson(U, delta_t, N):
    for i in range(0,N):
        U1 = U[:,i]
        U[:,i+1] = np.nsolve(U2 - U1 - (Kepler_F(U2)+ Kepler_F(U1))*delta_t/2, U2)
    return(U)

        

