# N-body problem resolution
import Resources.Temporal_Schemes  as ts
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

from Resources.Cauchy_Problem import Cauchy_Problem
from Resources.ODE_problems.N_body import F_N_body

from numpy import array, linspace, reshape


N = 10000

U_0 = array([2,0,2,0,1,-1,3,1,1,-1,0,-2, 1,0,2,-1,1,-1]) 

t = linspace(0, 10, N)

U = Cauchy_Problem( F_N_body, t, U_0, ts.Runge_Kutta_4)

fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(U[:,0], U[:,2], "b")
plt.plot(U[:,6], U[:,8], "r")
plt.plot(U[:,12], U[:,14], "g")
#plt.plot(U[:,18], U[:,20], "y")
plt.plot([U_0[0],U_0[6]],[U_0[2],U_0[8]], 'o')
ax.set_aspect('equal', adjustable='box')
plt.title("4-body problem, x-y projection, dt = 0.001 ")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()

fig = plt.figure()
ax1 = fig.add_subplot(111,projection='3d')
ax1.plot_wireframe(U[:,0].reshape((-1, 1)), U[:,2].reshape((-1, 1)), U[:,4].reshape((-1, 1)), color= "red")
ax1.plot_wireframe(U[:,6].reshape((-1, 1)), U[:,8].reshape((-1, 1)), U[:,10].reshape((-1, 1)), color= "blue")
ax1.plot_wireframe(U[:,12].reshape((-1, 1)), U[:,14].reshape((-1, 1)), U[:,16].reshape((-1, 1)), color= "green")
ax1.plot_wireframe(U[:,18].reshape((-1, 1)), U[:,20].reshape((-1, 1)), U[:,22].reshape((-1, 1)), color= "yellow")
ax1.plot([U_0[0],U_0[6],U_0[12], U_0[18]],[U_0[2],U_0[8],U_0[14], U_0[20]],[U_0[4],U_0[10],U_0[16],U_0[22]], 'o')
plt.title("4-body problem, dt = 0.001, Runge-Kutta-4")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()