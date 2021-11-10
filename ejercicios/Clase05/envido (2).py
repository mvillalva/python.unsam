#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 12:01:51 2020

@author: mcerdeiro
"""

# envido.py
# ejercicio 4.8

import random
#from tqdm import tqdm

#%%

valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [(valor,palo) for valor in valores for palo in palos]
#%%

def dar_mano():
    return random.sample(naipes,3)

def tengo_31(mano):
    ten = False
    for palo in palos:
        if (4, palo) in mano and (7, palo) in mano:
            ten = True
        if (5, palo) in mano and (6, palo) in mano:
            ten = True
    return ten

def tengo_32(mano):
    ten = False
    for palo in palos:
        if (5, palo) in mano and (7, palo) in mano:
            ten = True
    return ten

def tengo_33(mano):
    ten = False
    for palo in palos:
        if (6, palo) in mano and (7, palo) in mano:
            ten = True
    return ten
#%%
from tqdm import tqdm

N = 10000
G31 = 0
G32 = 0
G33 = 0
for i in tqdm(range(N)):
    mano = dar_mano()
    if tengo_33(mano):
        G33 += 1
    elif tengo_32(mano):
        G32 += 1
    elif tengo_31(mano):
        G31 += 1

print(f'Repartí {N} veces, de las cuales {G31} saqué 31 de envido, {G32} saqué 32 de envido y {G33} saqué 33 de envido.')
print(f'Podemos estimar la probabilidad de tener 31, 32 o 33 mediante {G31/N:.6f}, {G32/N:.6f} y {G33/N:.6f} respectivamente.')   
#%%


