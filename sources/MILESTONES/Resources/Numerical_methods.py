# NEWTON-RAPHSON ALGORITHM : find roots of a real fucntion

from numpy import size, array, zeros, dot
from numpy.linalg import inv, norm

def Jacobian(F, U):
	N = size(U)
	J= array(zeros([N,N]))
	t = 1e-3

	for i in range(N):
		xj = array(zeros(N))
		xj[i] = t
		J[:,i] = (F(U + xj) - F(U - xj))/(2*t)
	return J  


def newton(func, U_0):
	N = size(U_0) 
	U = array(zeros(N))
	U1 = U_0
	error = 1
	stop = 1e-8
	iteration = 0

	while error > stop and iteration < 1000:
		U = U1 - dot(inv(Jacobian(func, U1)),func(U1))
		error = norm(U - U1)
		U1 = U
		iteration = iteration +1
	return U


