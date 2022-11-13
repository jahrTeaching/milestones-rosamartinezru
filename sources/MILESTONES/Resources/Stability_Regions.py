from Resources.Temporal_Schemes  import *
from Resources.System_equations import newton
from numpy import zeros, size, float64, sqrt

## Absolute Stability Region
def Stability_Region(x, y, Temporal_Scheme):
    N = size(x)
    rho = zeros([N,N], dtype=float64)

    for i in range(N):
        for j in range(N):

            Z = complex(x[i],y[j])
            if Temporal_Scheme == Leap_Frog:
                r = Z + sqrt(Z**2+1)
            else:
                r = Temporal_Scheme(1., 1., lambda u, t: Z*u, 0.)

            rho[i,j] = abs(r)

    return rho

