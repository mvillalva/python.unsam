# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 08:20:45 2021

@author: MICHELL
"""

# =============================================================================
#Ejercicio 6.12: Un poco más allá
# =============================================================================

import csv
import informe_funciones

def costo_camion(nombre_archivo):
    'Calcula el precio pagado por los cajones cargados en el camión.'
    frutas = informe_funciones.leer_camion(nombre_archivo)
    costo_total=0  
    for fruta in frutas:
            ncajones = fruta['cajones']
            precio = fruta['precio']
            costo_total += ncajones * precio
    return costo_total
