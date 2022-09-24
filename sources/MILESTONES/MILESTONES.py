import numpy as np
import matplotlib.pyplot as plt


import Functions_Schemes as fs 


delta_t = 0.01
t_f = float(500)
N = int(t_f/delta_t) #Number of partitions

U_IC = np.zeros((4, N+1))

U_IC[:,0] = ([1., 0., 0., 1.]) #Initial conditions


#Explicit Euler Scheme
U_Euler = fs.Euler_Scheme(U_IC, delta_t, N)

plt.plot(U_Euler[0,:],U_Euler[1,:])
plt.show()

#Implicit Inverse Euler Scheme
U_IEuler = fs.Inverse_Euler(U_IC, delta_t, N)

plt.plot(U_IEuler[0,:],U_IEuler[1,:])
plt.show()

#Runge-Kutta Fourth Order Scheme
U_RK4 = fs.Runge_Kutta_4(U_IC, delta_t, N)

plt.plot(U_RK4[0,:],U_RK4[1,:])
plt.show()

#Crank-Nicolson Scheme
U_CN = fs.Crank_Nicolson(U_IC, delta_t, N)

plt.plot(U_CN[0,:],U_CN[1,:])
plt.show()
