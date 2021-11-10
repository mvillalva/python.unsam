# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 10:43:36 2021

@author: Jony
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 18:15:05 2021

@author: Jony
"""
import csv 

def leer_camion(nombre_archivo):    
    # Devuelve un dictionary con keys fijas( nombre, cajones, precio) y saca las values desde un archivo csv.
    camion = []
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            lote = (row[0], int(row[1]), float(row[2]))
            camion.append(lote)
        dcamion = [dict(zip(headers, l)) for l in camion]
    return dcamion


def leer_precios(nombre_archivo):
    # Lee la lista de precios de un archivo csv, devuelve un dictionary con el nombre de la fruta como key y el precio como value
    precios = {}
    with open(nombre_archivo, 'r') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                precios[row[0]] = float(row[1]) ### Falto convertir a float ###
            except IndexError:
                break
        return precios
    

def hacer_informe(camion,precios):
     listado=[]
     for compra in camion:
            artic=compra['nombre'] ### USAR NOMBRE EN LUGAR DE INDICES  ###
            cant=compra['cajones']
            p_costo=compra['precio']
            p_venta=precios[artic]
            listado.append((artic,cant,p_costo,(p_venta-p_costo)))            
     return(listado)
 
    
camion = leer_camion('../Data/camion.csv') # Lee el archivo camion.csv como dict
### Al usar ChainMap solo esta devolviendo el ultimo dato del diccionario ###
precios = leer_precios('../Data/precios.csv') # Lee el archivo precios.csv   
informe = hacer_informe(camion, precios)


headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')

print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
print('---------- '*4)

for nombre, cajones, precio, cambio in informe:
    print(f'{nombre:>10s} {cajones:>10d} {f"${precio:.2f}":>10s} {cambio:>10.2f}')