import numpy as np

my_array = np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])
# printa a matriz e o formato da matriz (i,j)
print(my_array, my_array.shape)

# preenche uma matriz do formato (i,j) dado em reshape com os numeros em ordem dada por arange(n) .
a = np.arange(16).reshape((4, 4))
print(a)

A = np.matrix([[6, 2, 4], [1, 1, 2], [4, 3, 2], [1, 1, 1]], dtype=float)
# diz o numero de linhas da matriz
n = np.shape(A)[0]
# diz o numero de colunas da matriz
m = np.shape(A)[1]

# preenche uma matriz identidade n x n
Identidade = np.eye(n)

print(A, n, m, Identidade)
