
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
def Euler_Scheme(U, delta_t, F, t):

    return U + delta_t*F(U,t)
    

#Implicit Inverse Euler Scheme
#def Inverse_Euler(U, delta_t, N):
#    for i in range(0,N):
#        U1 = U[:,i]
#        def func_I(x):
#            return [x[0] - U1[0] - x[2]*delta_t,
#                    x[1] - U1[1] - x[3]*delta_t,
#                    x[2] - U1[2] + x[0]/(np.linalg.norm(x[:-2])**3)*delta_t,
#                    x[3] - U1[3] + x[1]/(np.linalg.norm(x[:-2])**3)*delta_t]
#        U[:,i+1] = fsolve(func_I, [U[0,i], U[1,i], U[2,i], U[3,i]])
#    return(U)

def Inverse_Euler(U, delta_t, F, t):
 
    def func_I():
        return [x - U - F(x,t)*delta_t]

    return array([fsolve(func_I, U)])


#Runge-Kutta-4 Scheme
#def Runge_Kutta_4(U, delta_t, N):
#    for i in range(0,N):
#        k1 = Kepler_F(U[:,i])
#        k2 = Kepler_F(U[:,i] + delta_t*k1/2)
#        k3 = Kepler_F(U[:,i] + delta_t*k2/2)
#        k4 = Kepler_F(U[:,i] + delta_t*k3)

#        U[:,i+1] = U[:,i] + delta_t*(k1 + 2*k2 + 2*k3 + k4)/6
#    return(U)

def Runge_Kutta_4(U, delta_t, F, t):

    k1 = F(U, t)
    k2 = F(U + delta_t*k1/2, t + delta_t/2)
    k3 = F(U + delta_t*k2/2, t + delta_t/2)
    k4 = F(U + delta_t*k3, t + delta_t)

    return U + delta_t*(k1 + 2*k2 + 2*k3 + k4)/6


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
