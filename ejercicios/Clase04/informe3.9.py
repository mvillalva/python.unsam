# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 16:46:32 2021

@author: JuliManu
"""

#informe.py
import csv
def leer_camion(nombre_archivo):
    f = open(nombre_archivo, 'rt')
    rows = csv.reader(f)
    headers = next(rows)
    camion = []
    for n_row,row in enumerate(rows, start=1):
        record = dict(zip(headers,row))
        #lote = (record['nombre'], int(record['cajones']), float(record['precio']))
        camion.append(record)
    return camion
contenido_camion = leer_camion('../Data/fecha_camion.csv')
#print(contenido)
def leer_precios(nombre_archivo):
    f = open(nombre_archivo, 'rt')
    rows = csv.reader(f)
    dic = {}
    for n_row,row in enumerate(rows, start=1):
        try:
            dic[row[0]]= float(row[1])
        except IndexError:
            print (f'Fila {n_row}: no pude interpretar: {row}')
    return dic
contenido_precios = leer_precios('../Data/precios.csv')
#from pprint import pprint
#pprint(contenido)
costo_camion = 0
precio_total = 0
for fila in contenido_camion:
    costo_camion += int(fila['cajones'])*float(fila['precio'])
    precio_total += int(fila['cajones'])* contenido_precios[fila['nombre']]
balance = precio_total - costo_camion
print('el costo camion es', ' $', costo_camion)

print('el precio total es', ' $', precio_total)

print('el balance es', ' $', balance)
