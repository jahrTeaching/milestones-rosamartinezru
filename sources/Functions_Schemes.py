import numpy as np
from scipy.optimize import fsolve

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
        def func_I(x):
            return [x[0] - U1[0] - x[2]*delta_t,
                    x[1] - U1[1] - x[3]*delta_t,
                    x[2] - U1[2] + x[0]/(np.linalg.norm(x[:-2])**3)*delta_t,
                    x[3] - U1[3] + x[1]/(np.linalg.norm(x[:-2])**3)*delta_t]
        U[:,i+1] = fsolve(func_I, [U[0,i], U[1,i], U[2,i], U[3,i]])
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
        def func_CN(x):
            return [x[0] - U1[0] - (x[2] + Kepler_F(U1)[0])*delta_t/2,
                    x[1] - U1[1] - (x[3] + Kepler_F(U1)[1])*delta_t/2,
                    x[2] - U1[2] - (-x[0]/(np.linalg.norm(x[:-2])**3) + Kepler_F(U1)[2])*delta_t/2,
                    x[3] - U1[3] - (-x[1]/(np.linalg.norm(x[:-2])**3) + Kepler_F(U1)[3])*delta_t/2]
        U[:,i+1] = fsolve(func_CN, [U[0,i], U[1,i], U[2,i], U[3,i]])
    return(U)

        

