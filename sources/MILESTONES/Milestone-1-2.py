# MILESTONE 1 and 2

from numpy import array, linspace
import matplotlib.pyplot as plt

import Resources.Temporal_Schemes  as ts
import Resources.Kepler_Problem as kp
import Resources.Cauchy_Problem as cp

N = 50000

U_0 = array([1, 0, 0, 1]) 

t = linspace(0, 50, N)

U = cp.Cauchy_Problem( kp.Kepler_F, t, U_0, ts.Crank_Nicolson)

plt.plot(U[:,0], U[:,1])
plt.title("Kepler Orbit with dt = 0.001, Crank Nicolson Temporal Scheme")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

#PAINT THE ENERGY
#U1 = cp.Cauchy_Problem( kp.Kepler_F, t, U_0, ts.Euler)
#U2 = cp.Cauchy_Problem( kp.Kepler_F, t, U_0, ts.Inverse_Euler)
#U3 = cp.Cauchy_Problem( kp.Kepler_F, t, U_0, ts.Runge_Kutta_4)
#U4 = cp.Cauchy_Problem( kp.Kepler_F, t, U_0, ts.Crank_Nicolson)
# plt.plot(t, kp.Specific_energy(U1,N)[0:N], "r", label = "Euler")
#plt.plot(t, kp.Specific_energy(U2,N)[0:N], "b", label = "Inverse Euler")
#plt.plot(t, kp.Specific_energy(U3,N)[0:N], "g", label = "Runge Kutta 4")
#plt.plot(t, kp.Specific_energy(U4,N)[0:N], "m", label = "Crank Nicolson")
#plt.title("Specific energy, N =50000")
#plt.xlabel("Time [s]")
#plt.ylabel("Energy [J/kg]")
#plt.legend(loc = "lower right")
#plt.show()


