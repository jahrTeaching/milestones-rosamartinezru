from numpy.linalg import norm
from numpy import array, zeros, sqrt
from Resources.System_equations import newton



# CIRCULAR RESTRICTED 3 BODY PROBLEM

def CR3BP(U, t, mu):
    r = U[0:2] #Position
    drdt = U[2:4] #Velocity

    p1 = sqrt((r[0] +mu)**2 + r[1]**2)
    p2 = sqrt((r[0] -1 +mu)**2 + r[1]**2)

    dvdt_1 = -(1-mu)*(r[0]+mu)/(p1**3) - mu*(r[0] -1 +mu)/(p2**3)
    dvdt_2 = -(1-mu)*r[1]/p1**3 - mu*r[1]/p2**3

    return array([ drdt[0], drdt[1], 2*drdt[1] + r[0] + dvdt_1, -2*drdt[0] + r[1] + dvdt_2])

def Lagrange_points(U_0, NL, mu):

    LP = zeros([5,2])

    def F(Y):
        X = zeros(4)
        X[0:2] = Y
        X[2:4] = 0
        FX = CR3BP(X, 0 , mu)
        return FX[2:4]
   
    for i in range(NL):
        LP[i,:] = newton(F, U_0[i,0:2])

    return LP

