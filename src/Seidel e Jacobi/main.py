import numpy as np
import Jacobi as jc


A2 = np.matrix([[5, -4, 1, 0], [-4, 6, -4, 1],
                [1, -4, 6, -4], [0, 1, -4, 5]], dtype=float)

B2 = np.array([-1, 2, 1, 3], dtype=float)

A = np.matrix([[10, 2, 1],
               [1, 5, 1],
               [2, 3, 10]], dtype=float)

B = np.array([7, -8, 6], dtype=float)


Vetor = np.zeros_like(B)
print('vetor inicial:\n', Vetor)

tol = 0.00000001

Vetor, boolean, it = jc.jacobi(A, B, Vetor, tol)

print('JACOBI:\n vetor:\n ', Vetor, '\n Matriz é diagonal dominante: \n',
      boolean, '\nNumero iteracoes:\n', it)
