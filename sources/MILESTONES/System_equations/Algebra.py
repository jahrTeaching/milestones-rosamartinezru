# Matricial operators

from numpy import zeros, size, array, matmul

# Jacobian Matrix

def Jacobian(F, U):
	N = size(U)
	J= zeros([N,N])
	t = 1e-10

	for i in range(N):
		xj = zeros(N)
		xj[i] = t
		J[:,i] = (F(U + xj) - F(U - xj))/(2*t)
	return J  


# LU factorization

def factorization_LU(A):

	N = size(A,1)
	U = zeros([N,N])
	L = zeros([N,N])

	U[0,:] = A[0,:]
	for k in range(0,N):
		L[k,k] = 1

	L[1:N,0] = A[1:N,0]/U[0,0]


	for k in range(1,N):

		for j in range(k,N):
			U[k,j] = A[k,j] - matmul(L[k,0:k], U[0:k,j])

		for i in range(k+1,N):
			L[i,k] =(A[i,k] - matmul(U[0:k,k], L[i,0:k])) / (U[k,k])

	return L@U, L, U



