#costo_camion.py

#Ejercicio 2.9: Funciones de la biblioteca
import csv

def costo_camion(nombre_archivo):
    costo = 0
    with open(nombre_archivo, 'rt') as f:    
        lineas = csv.reader(f)
        
        encabezados = next(lineas)
        for i, linea in enumerate(lineas):
            record = dict(zip(encabezados, linea))            
            try:
                costo += (int(record['cajones']) * float(record['precio']))
            except ValueError:
                # muestro la línea i+2, ya que la primera corresponde al encabezado
                # de esta forma puedo saber que línea del archivo está el error.
                print(f'Ocurrió un error al leer la línea {i+2} del archivo')
    return costo


#### Programa Principal ####
costo = costo_camion('../Data/fecha_camion.csv')
print('Costo total:', costo) # Costo total: 47671.15
