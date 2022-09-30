# NEWTON-RAPHSON ALGORITHM : find roots of a real fucntion

from numpy import size, array, zeros, dot
from numpy.linalg import inv, norm

def Jacobian(F, U):
    N = size(U)
    J= array(zeros([N,N]))
    err = 1.e-3

    for i in range(N):
        J[:,i] = (F(U + err) - F(U - err))/(2*err)

    return J  


def newton(func, U_0):
    N = size(U_0) 
    U = array(zeros(N))
    U1 = U_0
    err = 1

    while err < 1e-8:
        U = U1 - dot(inv(Jacobian(func, U1)),func(U1))
        err = norm(U-U1)
        U1 = U

    return U


