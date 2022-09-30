# KEPLER ORBIT PROBLEM
from numpy import array, zeros, linspace


#Kepler Function
def Kepler_F(U, t):
    r = U[:-2] #Position
    drdt = U[2:] #Velocity
    norm = (r[0]**2 + r[1]**2)**0.5 

    return array([ drdt[0], drdt[1], -r[0]/(norm**3), -r[1]/(norm**3)])

 
   #Orbital specific energy
def Specific_energy(U,N):
    e = array(zeros(N+1))

    for i in range(0,N):

        mu = 3.986e14
        E_mec = (U[i,2]**2 + U[i,3]**2)/2
        E_pot = mu/((U[i,0]**2 + U[i,1]**2)**(1/2))
        e[i] = E_mec - E_pot

    return e

        
