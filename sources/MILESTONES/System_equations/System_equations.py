# NEWTON-RAPHSON ALGORITHM : find roots of a real function

from numpy import size, zeros, matmul, array, dot
from numpy.linalg import inv, norm
from System_equations.Algebra import Jacobian, factorization_LU
from numpy import float64


def solve_LU(M,b):

	N=size(b)
	y=zeros(N)
	x=zeros(N)

	A,L,U = factorization_LU(M)
	y[0] = b[0]

	for i in range(0,N):
		y[i] = b[i] - matmul(A[i,0:i], y[0:i])
		

	x[N-1] = y[N-1]/A[N-1,N-1]

	for i in range(N-2,-1,-1):
		x[i] = (y[i] - matmul(A[i, i+1:N+1], x[i+1:N+1])) / A[i,i]
		
	return x


def Inverse(A):

	N = size(A,1)

	B = zeros([N,N])

	for i in range(0,N):
		one = zeros(N)
		one[i] = 1

		B[:,i] = solve_LU(A, one)

	return B


def newton(func, U_0):
	N = size(U_0) 
	U = zeros(N)
	U1 = U_0
	error = 1
	stop = 1e-10
	iteration = 0

	while error > stop and iteration < 10000:
		U = U1 - dot(Inverse(Jacobian(func, U1)),func(U1))
		error = norm(U - U1)
		U1 = U
		iteration = iteration +1
	return U

