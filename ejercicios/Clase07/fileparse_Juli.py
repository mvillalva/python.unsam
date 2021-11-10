# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 12:17:25 2021

@author: julid
"""

import csv

def parse_csv(file, select = None, types = None, has_headers = True, silence_errors = False):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    if select!=None and has_headers == False:
        raise RuntimeError('Para seleccionar, necesito encabezados.')
        

    filas = csv.reader(file)
    if has_headers:
        # Lee los encabezados del archivo
        encabezados = next(filas)
    
        # Si se indicó un selector de columnas,
        #    buscar los índices de las columnas especificadas.
        # Y en ese caso achicar el conjunto de encabezados para diccionarios
    
        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []
    
        registros = []
        for i,fila in enumerate(filas):
            if not fila:    # Saltear filas vacías
                continue
        # Filtrar la fila si se especificaron columnas
            if indices:
                fila = [fila[index] for index in indices]
            if types:
                try:
                    fila = [func(val) for func, val in zip(types, fila) ]
                except ValueError as e:
                    if silence_errors == False:
                        print('Fila',i+1,':', ' No pude convertir', fila)
                        print('Motivo:', e)
            # Armar el diccionario
            registro = dict(zip(encabezados, fila))
            registros.append(registro)
    else:
        registros = []
        for i,fila in enumerate(filas):
            if not fila:
                continue
            if types:
                try:
                    fila = [func(val) for func, val in zip(types, fila) ]
                except ValueError as e:
                    if silence_errors == False:
                        print('Fila',i,':', ' No pude convertir', fila)
                        print('Motivo:', e)
            registro = tuple(fila)
            registros.append(registro)
       
            
    return registros