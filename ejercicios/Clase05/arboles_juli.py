# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 17:29:54 2021

@author: JuliManu
"""
#%%
import csv
def leer_parque(nombre_archivo, parque):
    f = open(nombre_archivo, 'rt', encoding='utf8') 
    filas = csv.reader(f)
    headers = next(filas)
    lista = []
    for fila in filas:
        record = dict(zip(headers, fila))
        if record['espacio_ve'] == parque:
            lista.append(record)
        else:
            pass
    return lista
lista1 = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')
from pprint import pprint
#pprint(lista1)
lista2 = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'ANDES, LOS')
lista3 = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'CENTENARIO')

#%%
def especies(lista_arboles):
    primero = []
    for arbol in lista_arboles:
        primero.append(arbol['nombre_com'])
    conjunto = set(primero)
    return conjunto
conjunto = especies(lista1)
#pprint(conjunto)

#%%
from collections import Counter
def especies(lista_arboles):
    esp = Counter()
    for arbol in lista_arboles:
        esp[arbol['nombre_com']]+=1
    return esp
especies1 = especies(lista1)
#pprint(especies1)
especies2 = especies(lista2)
#pprint(especies2)    
especies3 = especies(lista3)
#pprint(especies3)
gral_paz = especies1.most_common(5)
los_andes = especies2.most_common(5)
cente = especies3.most_common(5)
#print('ESPECIES MÁS COMUNES EN EL PARQUE GENERAL PAZ')
#pprint (gral_paz)
#print('ESPECIES MÁS COMUNES EN EL PARQUE LOS ANDES')
#pprint (los_andes)
#print('ESPECIES MÁS COMUNES EN EL PARQUE CENTENARIO')
#pprint (cente)        

#%%
def obtener_alturas(lista_arboles, especie):
    especies = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            altura_float = float(arbol['altura_tot'])
            especies.append(altura_float)
        else:
            pass
    return especies
alturas1 = obtener_alturas(lista1, 'Jacarandá')
alturas2 = obtener_alturas(lista2, 'Jacarandá')
alturas3 = obtener_alturas(lista3, 'Jacarandá')
max_gralpaz = max(alturas1)
prom_gralpaz = sum(alturas1)/len(alturas1)
max_losandes = max(alturas2)
prom_losandes = sum(alturas2)/len(alturas2)
max_cente = max(alturas3)
prom_cente = sum(alturas3)/len(alturas3)
#print (f'el máximo de altura en un Jacarandá en el parque General Paz es {max_gralpaz:.2f}, y el promedio es {prom_gralpaz:.2f}')
#print (f'el máximo de altura en un Jacarandá en el parque Los Andes es {max_losandes:.2f}, y el promedio es {prom_losandes:.2f}')
#print (f'el máximo de altura en un Jacarandá en el parque Centenario es {max_cente:.2f}, y el promedio es {prom_cente:.2f}')

#%%
def obtener_inclinaciones(lista_arboles, especie):
    inclinaciones = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            inclinacion_int = int(arbol['inclinacio'])
            inclinaciones.append(inclinacion_int)
        else:
            pass
    return inclinaciones
inclinaciones1 = obtener_inclinaciones(lista1, 'Jacarandá')
#print(inclinaciones1)

#%%
def especimen_mas_inclinado(lista_arboles):
    inclinaciones = []
    for arbol in lista_arboles:
        inclinacion_int = int(arbol['inclinacio'])
        inclinaciones.append(inclinacion_int)
    conjunto = set(inclinaciones)
    max_incli = max(conjunto)
    arbol_mas_incli = ''
    for arbol in lista_arboles:
        if max_incli == int(arbol ['inclinacio']):
            arbol_mas_incli = arbol ['nombre_com']
        else:
            pass
    return [max_incli,arbol_mas_incli]
mas_incli_gralpaz = especimen_mas_inclinado(lista1)
#print(f'el árbol con más inclinación en el parque General Paz es un {mas_incli_gralpaz[1]:s} con una inclinación de {mas_incli_gralpaz[0]:d} grados') 
mas_incli_losandes = especimen_mas_inclinado(lista2)
#print(f'el árbol con más inclinación en el parque Los Andes es un {mas_incli_losandes[1]:s} con una inclinación de {mas_incli_losandes[0]:d} grados') 
mas_incli_cente = especimen_mas_inclinado(lista3)
#print(f'el árbol con más inclinación en el parque Centenario es un {mas_incli_cente[1]:s} con una inclinación de {mas_incli_cente[0]:d} grados')    

#%%
def especie_promedio_mas_inclinada(lista_arboles):
    incli = Counter()
    esp = Counter()
    for arbol in lista_arboles:
        incli[arbol['nombre_com']] += int(arbol['inclinacio'])
        esp[arbol['nombre_com']] += 1
    lista_prom = []
    for arbol in lista_arboles:
        promedio = float(incli[arbol['nombre_com']]/esp[arbol['nombre_com']])
        lista_prom.append(promedio)
    max_prom = max(lista_prom)
    for arbol in lista_arboles:
        if float(incli[arbol['nombre_com']]/esp[arbol['nombre_com']]) == max_prom:
            arbol_max_prom = arbol['nombre_com']
        else:
            pass
    return [arbol_max_prom,max_prom]
mas_inclinada_losandes = especie_promedio_mas_inclinada(lista2)
print(f'la especie más inclinada en promedio en el parque Los Andes es un {mas_inclinada_losandes[0]:s} con un promedio de {mas_inclinada_losandes[1]:.2f} grados')

#%% Ejercicio 4.15, 4.16, 4,17 y 4.18
import csv
def leer_arboles(nombre_archivo):
    f = open(nombre_archivo, 'rt', encoding='utf8') 
    filas = csv.reader(f)
    headers = next(filas)
    tipos = [float, float, int, int, int, int, int, str, str, str, str, str, str, str, str, float, float]
    arboleda = []
    for fila in filas:
        convertida = [func(val) for func, val in zip(tipos, fila)]
        d = dict(zip(headers, convertida))
        arboleda.append(d)
    return arboleda


arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
   
H = [jacaranda['altura_tot'] for jacaranda in arboleda if jacaranda['nombre_com'] == 'Jacarandá']

lista_de_pares = [(jacaranda['altura_tot'],jacaranda['diametro']) for jacaranda in arboleda if jacaranda['nombre_com'] == 'Jacarandá']


def medidas_de_especies(especies,arboleda):

    dic = {especie: [(info['altura_tot'],info['diametro']) for info in arboleda if info['nombre_com'] == especie] for especie in especies}
    return dic

def main():
    #print(arboleda)
    #print(H)
    #print(HyD)
    especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    medidas_esp = medidas_de_especies(especies, arboleda)
    print(medidas_esp)
if __name__ == '__main__':
    main()

#%% Clase05
import numpy as np
import os
import matplotlib.pyplot as plt
import random
def histograma_altos_jacarandas(nombre_archivo):
    os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
    arboleda = leer_arboles(nombre_archivo)
    altos = [jacaranda['altura_tot'] for jacaranda in arboleda if jacaranda['nombre_com'] == 'Jacarandá']
    plt.hist(altos,bins=100)
    
#def main():
 #   histograma_altos_jacarandas('../Data/arbolado-en-espacios-verdes.csv')
#if __name__ == '__main__':
 #   main()
    
def scatter_hd(lista_de_pares):
    array = np.array(lista_de_pares)
    N = 50
    colors = np.random.rand(N)
    area = (30 * np.random.rand(N))**2  # 0 to 15 point radii
    
    plt.scatter(array[0], array[1], s=area, c=colors, alpha=0.5)
    plt.show()
    
def main():
    scatter_hd(lista_de_pares)
if __name__ == '__main__':
    main()