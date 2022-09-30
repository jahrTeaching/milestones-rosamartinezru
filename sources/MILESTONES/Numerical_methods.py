# NEWTON-RAPHSON ALGORITHM : find roots of a real fucntion

from numpy import size, array, zeros, dot
from numpy.linalg import inv

def Jacobian(F, U):
    N = size(U)
    J= array(zeros([N,N]))
    err = 1.e-3
    for i in range(N):
        J[:,i] = (F(U + err) - F(U-err))/(2*err)
    return J  


def newton(func, U):
        U = U - dot(inv(Jacobian(func, U)),func(U))
    return 
