# N-body problem resolution
import Resources.Temporal_Schemes  as ts
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

from Resources.Cauchy_Problem import Cauchy_Problem
from Resources.ODE_problems.N_body import F_N_body

from numpy import array, linspace, reshape


N = 10000

U_0 = array([1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0]) 

t = linspace(0, 10, N)

U = Cauchy_Problem( F_N_body, t, U_0, ts.Runge_Kutta_4)

plt.plot(U[:,0], U[:,1], "b")
plt.plot(U[:,6], U[:,7], "r")
plt.show()

fig = plt.figure()
ax1 = fig.add_subplot(111,projection='3d')
ax1.plot_wireframe(U[:,0].reshape((-1, 1)), U[:,1].reshape((-1, 1)), U[:,2].reshape((-1, 1)), color= "red")
ax1.plot_wireframe(U[:,6].reshape((-1, 1)), U[:,7].reshape((-1, 1)), U[:,8].reshape((-1, 1)), color= "blue")
plt.title("N-body problem")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()