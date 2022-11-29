
# LAGRANGE POINTS AND THEIR STABILITY

import Temporal_Schemes.Simple_TS as ts
import Temporal_Schemes.Adaptative_Stepsize  as eRK
import ODE_problems.Body3_Restricted as br
from Cauchy_Problem.Cauchy_Problem import Cauchy_Problem

from numpy import array, linspace, zeros, around
from random import random

import matplotlib.pyplot as plt

# CR3BP SOLUTION

N = 20000

t = linspace(0, 100, N)

#mu = 3.0039e-7 #Earth-Sun
mu = 1.2151e-2 #Earth-Moon


def F(U,t):

   return br.CR3BP(U, t, mu)

# LAGRANGE POINTS

NL = 5
U_0L = zeros([NL,4])

U_0L[0,:] = array([0.8, 0.6, 0, 0])
U_0L[1,:] = array([0.8, -0.6, 0, 0])
U_0L[2,:] = array([-0.1, 0, 0, 0])
U_0L[3,:] = array([0.1, 0, 0, 0])
U_0L[4,:] = array([1.01, 0, 0, 0])


x_p = br.Lagrange_points(U_0L, NL, mu)

# ORBITS AROUND LAGRANGE POINTS
U_0LP = zeros(4)
U_0SLP = zeros(4)

eps = 1e-3*random()
sel_LG = 1

U_0LP[0:2] = x_p[sel_LG-1,:] + eps
U_0LP[2:4] = eps

U_0SLP[0:2] = x_p[sel_LG-1,:] 
U_0SLP[2:4] = 0

# STABILITY OF LAGRANGE POINTS

U_LP = Cauchy_Problem(F, t, U_0LP, eRK.Embedded_RK)

eingvalues = br.Stability_LP(U_0SLP, mu)
print(around(eingvalues.real,8))

# PAINT THE ORBIT

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(U_LP[:,0], U_LP[:,1],'-',color = "r")
ax1.plot(-mu, 0, 'o', color = "g")
ax1.plot(1-mu, 0, 'o', color = "b")
for i in range(NL):
    ax1.plot(x_p[i,0], x_p[i,1] , 'o', color = "k")

ax2.plot(U_LP[:,0], U_LP[:,1],'-',color = "r")
ax2.plot(x_p[sel_LG-1,0], x_p[sel_LG-1,1] , 'o', color = "k")

ax1.set_xlim(-2,2)
ax1.set_ylim(-2,2)
ax1.set_title("Orbital system view")
ax2.set_title("Lagrange point view")
ax2.set_xlim(x_p[sel_LG-1,0]-0.5,x_p[sel_LG-1,0]+0.5)
ax2.set_ylim(x_p[sel_LG-1,1]-0.5,x_p[sel_LG-1,1]+0.5)
fig.suptitle("Earth-Sun - CR3BP (Inverse Euler TS) - Orbit around the L2 point with t = " + str(t[N-1]))
for ax in fig.get_axes():
    ax.set(xlabel='x', ylabel='y')
    ax.grid()

plt.show()

