# CAUCHY PROBLEM
from numpy import array, zeros

def Cauchy_Problem(F, t, U_0, Temporal_Scheme):

    N = len(t) - 1
    N_0 = len(U_0)
    U = array(zeros([N+1, N_0]))

    U[0,:] = U_0

    for i in range(N):

        delta_t = t[i+1] - t[i]
        U[i+1, :] = Temporal_Scheme(U[i, :], delta_t, F, t[i])

    return U




