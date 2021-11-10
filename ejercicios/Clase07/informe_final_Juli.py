# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 11:16:15 2021

@author: julid
"""


import csv
import fileparse


def leer_camion(file):
    camion = fileparse.parse_csv(file, types = [str, int, float])
    return camion

def leer_precios(file):
    precios = fileparse.parse_csv(file, types = [str, float], has_headers = False)
    return precios

def hacer_informe(archivo_camion, archivo_precios):
    contenido_camion = leer_camion(archivo_camion)
    contenido_precios = dict(leer_precios(archivo_precios))
    lista = []
    for n in contenido_camion:
        n = (n['nombre'], n['cajones'], n['precio'], contenido_precios[n['nombre']]-n['precio'])
        lista.append(n)
    return lista
def imprimir_informe(informe):
    for nombre, cajones, precio, cambio in informe:
        precio_nuevo = '$' + str(precio)
        print(f'{nombre:>10s} {cajones:>10d} {precio_nuevo:>10s} {cambio:>10.2f}')
def informe_camion(archivo_camion, archivo_precios):
    informe = hacer_informe(archivo_camion, archivo_precios)
    imprimir_informe(informe)
    
    
    
def f_principal(parametros):
    if len(parametros) != 3:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'archivo_camion archivo_precios')
    archivo_camion = parametros[1]
    archivo_precios = parametros[2]
    informe = hacer_informe(archivo_camion, archivo_precios)
    imprimir_informe(informe)
    
    
if __name__ == '__main__':
    import sys
    f_principal(sys.argv)
#informe_camion('../Data/camion.csv', '../Data/precios.csv')


#%%
