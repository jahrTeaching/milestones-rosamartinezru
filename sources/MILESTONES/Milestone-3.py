# NUMERICAL ERROR

from numpy import array, linspace, zeros, size
from numpy.linalg import norm
import matplotlib.pyplot as plt

import Resources.Temporal_Schemes  as ts
import Resources.ODE_problems.Kepler_Problem as kp
import Resources.Cauchy_Problem as cp
from Resources.ODE_problems.Harmonic_Oscillator import F_oscillator 

N = 50000

U_0 = array([1, 0, 0, 1]) 

t = linspace(0, 50, N)

error = cp.Error_Cauchy(kp.Kepler_F, t, U_0, ts.Leap_Frog, 2)
module = zeros(size(error[:,0]))
for i in range(0,size(error[:,0])):
    module[i] = (error[i,0]**2 + error[i,1]**2)**(1/2)

plt.plot(t, error[:,0], 'o', color =  "red", label = "X position")
plt.plot(t, error[:,1], 'o', color = "blue", label = "Y position")
plt.plot(t, module,  'o',color =  "green", label = "Error module")
plt.title("Numerical error, Leap-Frog TS, dt = 0.01")
plt.xlabel("t")
plt.ylabel("Error")
plt.legend(loc = "lower left")
plt.grid()
plt.show()

#plt.plot(t, error[:,0],"r", 'o',  label = "X position")
#plt.title("Numerical error, Leap-Frog TS, dt = 0.01")
#plt.xlabel("t")
#plt.ylabel("Error")
#plt.legend(loc = "lower left")
#plt.grid()
#plt.show()

#error_Euler = cp.Error_Cauchy(kp.Kepler_F, t, U_0, ts.Euler, 1)
#module_Euler = zeros(size(error_Euler[:,0]))
#for i in range(0,size(error_Euler[:,0])):
#     module_Euler[i] = (error_Euler[i,0]**2 + error_Euler[i,1]**2)**(1/2)

#error_InvE = cp.Error_Cauchy(kp.Kepler_F, t, U_0, ts.Inverse_Euler, 1)
#module_InvE = zeros(size(error_Euler[:,0]))
#for i in range(0,size(error_InvE[:,0])):
#     module_InvE[i] = (error_InvE[i,0]**2 + error_InvE[i,1]**2)**(1/2)

#error_CN = cp.Error_Cauchy(kp.Kepler_F, t, U_0, ts.Crank_Nicolson, 2)
#module_CN = zeros(size(error_Euler[:,0]))
#for i in range(0,size(error_CN[:,0])):
#     module_CN[i] = (error_CN[i,0]**2 + error_CN[i,1]**2)**(1/2)

#error_RK4 = cp.Error_Cauchy(kp.Kepler_F, t, U_0, ts.Runge_Kutta_4, 4)
#module_RK4 = zeros(size(error_Euler[:,0]))
#for i in range(0,size(error_RK4 [:,0])):
#     module_RK4[i] = (error_RK4 [i,0]**2 + error_RK4 [i,1]**2)**(1/2)


#plt.plot(t, module_Euler,"r", label = "Euler error module")
#plt.plot(t, module_InvE,"b", label = "Inverse Euler error module")
#plt.plot(t, module_CN,"g", label = "Crank-Nicolson error module")
#plt.plot(t, module_RK4,"m", label = "Runge-Kutta-4 error module")
#plt.title("Numerical error module for different TS")
#plt.xlabel("t")
#plt.ylabel("Position error module")
#plt.legend(loc = "upper left")
#plt.grid()
#plt.show()


#[log_N1, log_E1] = cp.Convergence_rate(F_oscillator, t, U_0, ts.Leap_Frog)
#[N_lineal, E_lineal, order, log_E_total] = cp.lineal_Convergence_rate(log_E1, log_N1)

#plt.plot(log_N1, log_E1, color = "r", label = "log(|U2-U1|)")
#plt.plot(log_N1,log_E_total, color = "g", label = "log(|E|)")
#plt.title("Numerical error of Euler")
#plt.xlabel("log(N)")
#plt.ylabel("error")
#plt.grid()
#plt.show()

#plt.plot(log_N1, log_E1, color = "r", label = "Leap-Frog")
#plt.plot(N_lineal, E_lineal, "--", color = "b", label = "Linear Regression")
#plt.title("Convergence rate for Leap Frog, order =" +str(order))
#plt.xlabel("log(N)")
#plt.ylabel("log(|U2-U1|)")
#plt.legend(loc = "lower left")
#plt.grid()
#plt.show()
