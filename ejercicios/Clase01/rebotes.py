# rebotes.py
altura = 100
for i in range(10):
    altura = altura * (3/5)
    print(round(altura,4))
#%%
from random import shuffle, randint     # Números pseudoaleatorios
from itertools import product           # Producto cartesiano

def laberinto(m, n):
    def vecinos(i, j):                  # Conjunto de celdas aledañas a (i, j)
        if 0 < i: yield i - 1, j
        if i < m - 1: yield i + 1, j
        if 0 < j: yield i, j - 1
        if j < n - 1: yield i, j + 1

    def visitar(i, j):                  # Alg. de recorrido en profundidad:
        X.add((i, j))                   # Marcar celda actual como visitada
        N = list(vecinos(i, j)); shuffle(N)  # Desordenar celdas vecinas
        for h, k in N:                  # Para cada celda vecina
            if (h, k) in X: continue    # ...que no haya sido visitada:
            A[i + h + 1][j + k + 1] = ' '  # Tumbar el muro que las separa
            visitar(h, k)               # Visitar vecina recursivamente

    A = [['█']*(2*n + 1) for i in range(2*m + 1)]  # Tablero
    for i, j in product(range(1, 2*m + 1, 2), range(1, 2*n + 1, 2)):
        A[i][j] = ' '                   # Poner celdas blancas
    X = set()                           # Conjunto de celdas visitadas
    visitar(randint(0, m - 1), randint(0, n - 1))  # Inicio en celda aleatoria
    return('\n'.join(''.join(fila) for fila in A))  # Unir símbolos en un str

print(laberinto(11, 39))    
# %%
