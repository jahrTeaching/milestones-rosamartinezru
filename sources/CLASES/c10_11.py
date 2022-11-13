from copy import deepcopy

# En una lista de listas no funciona el deep copy 
A = [[1,2], [3,4]]

B = A
C = A.copy()
D = deepcopy(A)

A[1][1] = 0
print("B = ", B) # Sale el cero en las dos, solo debería salir en B
print("C = ", C)
print("D = ", D) # Ahora si que sale sin el cero

A = [[1,2], [3,4]]
N, M = len(A), len(A[0])
E = [[A[i][j] for i in range(N)] for j in range(M)]
A[1][1] = 0

print("E = ", E)

