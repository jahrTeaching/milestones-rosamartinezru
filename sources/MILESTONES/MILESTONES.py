from numpy import array, linspace
import matplotlib.pyplot as plt

import Functions_Schemes as fs

N = 5000

U_0 = array([1, 0, 0, 1])

t = linspace(0, 50, N)

U = fs.Cauchy_Problem( fs.Kepler_F, t, U_0, fs.Runge_Kutta_4)
plt.plot(U[:,0], U[:,1])
plt.title("Kepler Orbit with dt = 0.01, RK-4 Temporal Scheme")
plt.xlabel("x")
plt.ylabel("y")
plt.show()



