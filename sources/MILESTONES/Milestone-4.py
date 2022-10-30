## Integration of the linear oscillator
import Resources.Temporal_Schemes  as ts
import matplotlib.pyplot as plt
import Resources.Stability_Regions as sr

from Resources.Cauchy_Problem import Cauchy_Problem
from Resources.Harmonic_Oscillator import F_oscillator 

from numpy import array, linspace, cos, sin 


N = 100

U_0 = array([1,0]) 

t = linspace(0, 10, N)

U = Cauchy_Problem( F_oscillator, t, U_0, ts.Leap_Frog)

plt.plot(t, U[:,0],"r", label = "Approximate solution")
plt.plot(t, cos(t),"--",color = "r", label = "Analitic solution")
plt.plot(t, U[:,1], "b", label = "Appr. velocity")
plt.plot(t, -sin(t),"--", color = "b", label = "Analit. velocity")
plt.title("Harmonic Oscillator dt = 0.1, Leap-Frog Temporal Scheme")
plt.xlabel("t")
plt.ylabel("y(t)/dy(t)")
plt.legend(loc = "lower left")
plt.grid()
plt.show()


x = linspace(-5, 5, num=100);
y = linspace(-5, 5, num=100);

dt = array([0.01, 0.1, 1])

stab_region = sr.Stability_Region(x,y,ts.Runge_Kutta_4)

CSF = plt.contourf(x, y, stab_region, levels = [0, 1],  colors=['#C0C0C0'] ) #levels = [0.5, 1, 1.5]
CS = plt.contour(x, y, stab_region, levels = [0.5, 1, 1.5] ) 
for t in range(3):
    plt.plot([0,0],[1*dt[t],-1*dt[t]], 'o', label = "Harmonic Oscillator Roots with dt = " +str(dt[t]))
plt.clabel(CS, inline=1, fontsize=10)
plt.title('Absolute Stability Region for Leap Frog TS')
plt.xlabel("Re(|r|)")
plt.ylabel("Im(|r|)")
plt.legend(loc = "lower left")
plt.grid()
plt.show()
