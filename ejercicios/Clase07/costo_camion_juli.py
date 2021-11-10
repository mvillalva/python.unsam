# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 16:38:42 2021

@author: JuliManu
"""

import csv
import informe_final
def costo_camion(nombre_archivo):
    camion = informe_final.leer_camion(nombre_archivo)
    costo_total = 0
    for fruta in camion:
        try:
            ncajones = fruta['cajones']
            precio = fruta['precio']
            costo_total += ncajones * precio
        except ValueError:
            print (f'hay un error en el archivo de lectura')
    return costo_total

def f_principal(parametros):
    if len(parametros) != 2:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'archivo_camion')
    archivo_camion = parametros[1]
    costo = costo_camion(archivo_camion)
    print('Costo total:', costo)
    
if __name__ == '__main__':
    import sys
    f_principal(sys.argv)