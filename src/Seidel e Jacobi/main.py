import numpy as np
import Jacobi as jc
import Seidel as sd

A2 = np.matrix([[5, -4, 1, 0], [-4, 6, -4, 1],
                [1, -4, 6, -4], [0, 1, -4, 5]], dtype=float)

B2 = np.array([-1, 2, 1, 3], dtype=float)

A = np.matrix([[10, 2, 1],
               [1, 5, 1],
               [2, 3, 10]], dtype=float)

B = np.array([7, -8, 6], dtype=float)


Vetor = np.zeros_like(B)

Vetor2 = np.zeros_like(B2)

print('vetor inicial:\n', Vetor)

tol = 0.00001

V_jacobi, boolean, it = jc.jacobi(A, B, Vetor, tol)

print('JACOBI:\n vetor:\n ', V_jacobi, '\n Matriz é diagonal dominante: \n',
      boolean, '\nNumero iteracoes:\n', it)


V_seidel, boolean, it = sd.seidel(A, B, Vetor, tol)

print('SEIDEL:\n vetor:\n ', V_seidel, '\n Matriz é diagonal dominante: \n',
      boolean, '\nNumero iteracoes:\n', it)
