import numpy as np
inicio = 1
fin = 19

vec = np.arange(inicio, fin+1, 2)
print([vec])

vec = np.linspace(inicio, fin, num=(inicio+fin)//2)
print([vec])