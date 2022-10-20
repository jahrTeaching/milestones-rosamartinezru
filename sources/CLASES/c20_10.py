# Ejercicio de swap entre filas de matrices
from numpy import array, reshape

U = array([1,2,3,4])
U = reshape(U,(2,2))

(U[:,0],U[:,1]) = (U[:,1].copy(), U[:,0].copy())
# ó
#U[:,[0,1]]=U[:,[1,0]]

print("U = ", U)


