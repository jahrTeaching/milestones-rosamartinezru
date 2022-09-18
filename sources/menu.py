#MILESTONE-1

import numpy as np

N = 10000 #Number of partitions
t_f = 12 * np.pi

t = np.linspace(0,t_f, N) 
U = np.zeros((4,N+1))
F = np.zeros(4)

U[:,0] = ([1., 0., 0., 1.]) #Initial conditions

#Explicit Euler Method
delta_t = t[1]-t[0]

for i in range(0,N):
    r = U[:-2,i]
    drdt = U[2:,i]
    F =  np.concatenate(( drdt, - r / (np.linalg.norm(r)**3)), axis = None) 
    U[:,i+1] = U[:,i] + delta_t*F
