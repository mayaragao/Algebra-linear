import numpy as np
import PowerMethod as pm

A = np.matrix([[1, 0.2, 0],
               [0.2, 1, 0.5],
               [0, 0.5, 1]], dtype=float)

A2 = np.matrix([[3, 2, 0], [2, 3, -1], [0, -1, 3]], dtype=float)

n = np.shape(A2)[0]
X0 = np.ones(n)
lambda0 = 1
tolerancia = 0.001

print('\n POWER METHOD:\n\n A:\n', A2)


lamb, X, iteracoes = pm.metodo_potencia(A2, X0, lambda0, tolerancia)


print('\nAutoVetor = ', X, '\nAutoValor =',
      lamb, '\nNº de iteracoes: ', iteracoes)
