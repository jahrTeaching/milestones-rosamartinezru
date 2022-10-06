# NEWTON-RAPHSON ALGORITHM : find roots of a real function

from numpy import size, zeros, dot
from numpy.linalg import inv, norm
from Resources.Algebra import Jacobian



def newton(func, U_0):
	N = size(U_0) 
	U = zeros(N)
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


