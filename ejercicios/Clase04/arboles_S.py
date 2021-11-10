#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 17:35:47 2021

@author: Stefania Orozco Gil
"""
# arboles.py
# Ejercicio de aplicación de conocimientos a una base de datos 
# sobre árboles en parques de la Ciudad de Buenos Aires
from collections import Counter
from pprint import pprint
import csv

#%% Ejercicio 3.18: Lectura de los árboles de un parque

# Definí una función leer_parque(nombre_archivo, parque) 
# que abra el archivo indicado y devuelva una lista de 
# diccionarios con la información del parque especificado. 
# La función debe devolver, en una lista un diccionario 
# con todos los datos por cada árbol del parque elegido 
# (recordá que cada fila del csv es un árbol).

# ------Función leer_parque(nombre_archivo, parque)-----

def leer_parque(nombre_archivo, parque):
    archivo = []
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        encabezados = next(rows)
        for row in rows:
            registro = dict(zip(encabezados, row))
            if parque == registro['espacio_ve']:
                archivo.append(registro)
            else:
                pass
    return archivo

# #%%
# centenario = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'CENTENARIO')

# #%%
# gral_paz = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')

# #%%
# los_andes = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'ANDES, LOS')

#%% Ejercicio 3.19: Determinar las especies en un parque

def especies(lista_arboles):
    a = []
    for arbol in lista_arboles:
        uno = arbol['nombre_com']
        a.append(uno)
    unicos = set(a)
    return unicos

# #%%
# arb_centenario = especies(centenario)

# #%%
# arb_geral_paz = especies(gral_paz)

#%% Ejercicio 3.20: Contar ejemplares por especie

# Usando contadores como en el Ejercicio 3.11, escribí una 
# función contar_ejemplares(lista_arboles) que, dada una 
# lista como la que generada con leer_parque(), devuelva 
# un diccionario en el que las especies (recordá, es la 
# columna 'nombre_com' del archivo) sean las claves y 
# tengan como valores asociados la cantidad de ejemplares
# en esa especie en la lista dada

# lista = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'CENTENARIO')

# from collections import Counter
# def contar_ejemplares(lista_arboles):
#     especies = Counter()
#     for arbol in lista_arboles:
#         especies[arbol['nombre_com']] += round(int(arbol['id_especie'])/int(arbol['id_especie']))
#     return especies

# a = contar_ejemplares(lista)
# pprint(a)

#%% Ejercicio 3.20: Contar ejemplares por especie_solución Manu 

def contar_ejemplares(lista_arboles):
    d = Counter()
    for arbol in lista_arboles:
        d[arbol['nombre_com']] += 1
    return d

# #%%
# ejemplares_centenario = contar_ejemplares(centenario)
# pprint(ejemplares_centenario)

# #%%
# ejemplares_gral_paz = contar_ejemplares(gral_paz)
# pprint(ejemplares_gral_paz)

# #%%
# ejemplares_los_andes = contar_ejemplares(los_andes)
# pprint(ejemplares_los_andes)

#%% Ejercicio 3.21: Alturas de una especie en una lista

#%% Ejercicio 3.23: Especie con el ejemplar más inclinado

#%% Ejercicio 4.15: Lectura de todos los árboles

# Basándote en la función leer_parque(nombre_archivo, parque) 
# del Ejercicio 3.18, escribí otra leer_arboles(nombre_archivo) 
# que lea el archivo indicado y devuelva una lista de diccionarios 
# con la información de todos los árboles en el archivo. 
# La función debe devolver una lista conteniendo un diccionario 
# por cada árbol con todos los datos.

# Vamos a llamar arboleda a esta lista.

def leer_arboles(nombre_archivo):    
    with open (nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)        
        types = [float,float,int,int,int,int,int,str,str,str,str,str,str,str,str,float,float]        
        lista = [dict(zip(headers,[func(val) for func, val in zip(types, row)])) for row in rows]

    return lista


#%% Ejercicio 4.16: Lista de altos de Jacarandá

# Usando comprensión de listas y la variable arboleda podés 
# por ejemplo armar la lista de la altura de los árboles.

arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
H = [arbol['altura_tot'] for arbol in arboleda]

# Usá los filtros (recordá la Sección 4.3) para armar la lista 
# de alturas de los Jacarandás solamente.

jacaranda = [jac['altura_tot'] for jac in arboleda if jac['nombre_com'] == 'Jacarandá']
print(jacaranda)







