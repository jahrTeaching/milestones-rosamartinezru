# NUMERICAL ERROR

from numpy import array, linspace
import matplotlib.pyplot as plt

import Resources.Temporal_Schemes  as ts
import Resources.Kepler_Problem as kp
import Resources.Cauchy_Problem as cp


N = 10

U_0 = array([1, 0, 0, 1]) 

t = linspace(0, 50, N)

#error = cp.Error_Cauchy(kp.Kepler_F, t, U_0, ts.Euler)


#plt.plot(t, error[:,0],"r", label = "X position")
#plt.plot(t, error[:,1],"b", label = "Y position")
#plt.title("Numerical error, Crank-Nicolson TS, dt = 0.01")
#plt.xlabel("t")
#plt.ylabel("Error")
#plt.legend(loc = "lower left")
#plt.show()

[log_N1, log_E1, order, N_lineal, E_lineal] = cp.Convergence_rate(kp.Kepler_F, t, U_0, ts.Euler)


plt.plot(log_N1, log_E1, color = "r", label = "Euler")
plt.plot(N_lineal, E_lineal, "--", color = "b", label = "Linear Regression")
plt.title("Convergence rate for Euler, order =" +str(order))
plt.xlabel("log(N)")
plt.ylabel("log(|U2-U1|)")
plt.legend(loc = "lower left")
plt.grid()
plt.show()
