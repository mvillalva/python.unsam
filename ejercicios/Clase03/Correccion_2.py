"""
Este programa funciona si estas ubicado en "..\Ejercicio\Clase03\"

@author:  Hugo César Galván


"""
#informe.py
"""
Realiza el balance de las operaciones en frutería en base a los
precios y el valor de cada fruta por cajón

Usa técnica para elegir las columnas a partir de sus encabezados.
"""
import csv
# Armamos un diccionario con cada tipo de 
def leer_camion(nombre_archivo):
    f = open(nombre_archivo)
    rows = csv.reader(f)
    encabezados = next(rows)
    camion = []
    lote = {}
    for n_fila, fila in enumerate(rows, start=1):
        record = dict(zip(encabezados, fila))
        lote ['nombre'] = record['nombre']
        lote ['cajones'] = int(record['cajones'])
        lote ['precio'] = float(record['precio'])
        camion.append(lote)      
        lote = {}
    f.close()
    return camion


def leer_precios(nombre_archivo):
    dic_precio = {}
    f = open(nombre_archivo, 'r')
    rows = csv.reader(f)
    for row in rows:
        if len(row)>1:
            dic_precio[row[0]] = float(row[1])
        else:
            continue
    return dic_precio
    f.close()   


def hacer_informe(camion, precios):
    camion = leer_camion(camion)
    precios = leer_precios(precios)
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    frutavta = []
    for s in camion:
        for k, v in precios.items():
            if (s['nombre'])== k:
                fruta1 = ( s['nombre'], s['cajones'], s['precio'], float(v)-float(s['precio']) )
                frutavta.append(fruta1)
    
    
    print('%10s %10s %10s %10s' % headers) #print(fruta)
    print('---------- ---------- ---------- ----------')
    for r in frutavta:
        print('%10s %10d %10.2f %10.2f' % r) #print(fruta)
    return 
    
#%%
informes = hacer_informe('../Data/camion.csv', '../Data/precios.csv')
#print(informes[0])
