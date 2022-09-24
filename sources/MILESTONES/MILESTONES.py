from numpy import array, linspace
import matplotlib.pyplot as plt

import Functions_Schemes as fs

N = 1000

U_0 = array([1, 0, 0, 1])

t = linspace(0, 30, N)

U = fs.Cauchy_Problem( fs.Kepler_F, t, U_0, fs.Crank_Nicolson)
plt.plot(U[:,0], U[:,1])
plt.show()



