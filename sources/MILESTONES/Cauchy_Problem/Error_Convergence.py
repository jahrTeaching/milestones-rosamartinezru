from Cauchy_Problem.Cauchy_Problem import Cauchy_Problem

from numpy import array, zeros, size, linspace, log10, round_
from numpy.linalg import norm

# RICHARDSON ERROR

def Error_Cauchy(F, t, U_0, Temporal_Scheme, order):

    N = size(t)
    E = zeros([N,size(U_0)])

    t1 = t
    t2 = linspace(0, t[N-1], N*2)

    U2N = Cauchy_Problem(F, t2, U_0, Temporal_Scheme)
    U1N = Cauchy_Problem(F, t1, U_0, Temporal_Scheme)

    for i in range(0,N):
        E[i,:] = (U2N[2*i,:] - U1N[i,:]) / (1 - 1 / (2**order))

    return E

# TEMPORAL CONVERGENCE

def Convergence_rate(F, t, U_0, Temporal_Scheme):

    N = size(t)

    t1 = t
    tf = t1[N-1]
    U1 = Cauchy_Problem(F, t1, U_0, Temporal_Scheme)

    k = 20

    log_E = zeros(k)
    log_N = zeros(k)

    for i in range(0,k):

        N = 2*N
        t2 = linspace(0, tf, N)

        U2 = Cauchy_Problem(F, t2, U_0, Temporal_Scheme)

        E = norm((U2[int(N-1),:] - U1[int(N/2-1),:]))

        log_E[i] = log10(E)
        log_N[i] = log10(N)

        t1 = t2
        U1 = U2

    return [log_N, log_E]

def lineal_Convergence_rate(log_E, log_N):

    k = size(log_E)


    for j in range(0,k):
         if (abs(log_E[j]) > 12):
             break
    j = min(j, k)
    reg = LinearRegression().fit(log_N[0:j+1].reshape((-1, 1)),log_E[0:j+1])
    order = round_(abs(reg.coef_),1)

    log_N_lineal = log_N[0:j+1]
    log_E_lineal = reg.predict(log_N[0:j+1].reshape((-1, 1)))
    

    log_E_total = log_E - log10(1 - 1 / (2**order))

    return [log_N_lineal, log_E_lineal, order, log_E_total]


