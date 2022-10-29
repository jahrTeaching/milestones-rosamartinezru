import Resources.Temporal_Schemes  as ts
from numpy import meshgrid, array, zeros, size, absolute, sqrt

## Absolute Stability Region
def Stability_Region(x,y,Temporal_Scheme):
    N = size(x)
    Z = zeros([N,N],dtype=complex)

    for i in range(N):
        for j in range(N):
            Z[N-1-j,i] = complex(x[i],y[j])

    return absolute(array(Stability_Polinomial(Temporal_Scheme, Z)))



def Stability_Polinomial(Temporal_Scheme, w):
    if Temporal_Scheme == ts.Euler:
        r = 1 + w
    elif Temporal_Scheme == ts.Inverse_Euler:
        r = 1/(1-w)
    elif Temporal_Scheme == ts.Crank_Nicolson:
        r = (1+w/2)/(1-w/2)
    elif Temporal_Scheme == ts.Runge_Kutta_4:
        r = 1 + w + (w**2)/2 + (w**3)/6 + (w**4)/(4*3*2)
    elif Temporal_Scheme == ts.Leap_Frog:
        r = sqrt(1)

    return r

