
from numpy import array, zeros, size, linspace, log10, round_
from numpy.linalg import norm
from sklearn.linear_model import LinearRegression
import Temporal_Schemes.Simple_TS  as ts

# CAUCHY PROBLEM

def Cauchy_Problem(F, t, U_0, Temporal_Scheme):

    N = len(t) - 1
    N_0 = len(U_0)
    U = array(zeros([N+1, N_0]), dtype=type(U_0))
    
    delta_t = t[2] - t[1]

    U[0,:] = U_0

    if Temporal_Scheme == ts.Leap_Frog:
        U[1,:] = U[0,:] + delta_t*F(U[0,:], t[0])

        for i in range(1,N):
            U1 = U[i-1, :]
            U2 = U[i, :]
            U[i+1, :] = Temporal_Scheme(U2, U1, delta_t, F, t[i])

    else:
        for i in range(N):
            U[i+1, :] = Temporal_Scheme(U[i, :], delta_t, F, t[i])

    return U
