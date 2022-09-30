#MILESTONE-1

from numpy import array, linspace
import matplotlib.pyplot as plt

import Functions_Schemes as fs

N = 5000

U_0 = array([1, 0, 0, 1])

t = linspace(0, 50, N)

U = fs.Cauchy_Problem( fs.Kepler_F, t, U_0, fs.Inverse_Euler)
plt.plot(U[:,0], U[:,1])
plt.title("Kepler Orbit with dt = 0.001, Euler Temporal Scheme")
plt.xlabel("x")
plt.ylabel("y")
plt.show()






#U1 = fs.Cauchy_Problem( fs.Kepler_F, t, U_0, fs.Euler)
#U2 = fs.Cauchy_Problem( fs.Kepler_F, t, U_0, fs.Inverse_Euler)
#U3 = fs.Cauchy_Problem( fs.Kepler_F, t, U_0, fs.Runge_Kutta_4)
#U4 = fs.Cauchy_Problem( fs.Kepler_F, t, U_0, fs.Crank_Nicolson)
# plt.plot(t, fs.Specific_energy(U1,N)[0:N], "r", label = "Euler")
#plt.plot(t, fs.Specific_energy(U2,N)[0:N], "b", label = "Inverse Euler")
#plt.plot(t, fs.Specific_energy(U3,N)[0:N], "g", label = "Runge Kutta 4")
#plt.plot(t, fs.Specific_energy(U4,N)[0:N], "m", label = "Crank Nicolson")
#plt.title("Specific energy, N =50000")
#plt.xlabel("Time [s]")
#plt.ylabel("Energy [J/kg]")
#plt.legend(loc = "lower right")
#plt.show()

