# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 16:20:42 2021

@author: JuliManu
"""
#%% EJ 5.3 COCUMPLEAÑOS
import random
from collections import Counter

def cumpleaños():
    cumples = []
    for i in range(30):
        cumples.append(random.randint(1,365))
    repite = Counter()
    for cumple in cumples:
        repite[cumple] += 1
    return repite

def mismo_dia(cumples):
    hay_mismo_dia = False
    for cumple in cumples: 
        if cumples[cumple]>1:
            hay_mismo_dia = True
    
    return hay_mismo_dia       

print(cumpleaños())
N=100000
G = sum([mismo_dia(cumpleaños()) for i in range(N)])
prob = G/N
print(prob)