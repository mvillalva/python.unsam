#costo_camion.py

#Ejercicio 2.9: Funciones de la biblioteca
import csv

def costo_camion(nombre_archivo):
    costo = 0
    with open(nombre_archivo, 'rt') as f:    
        lineas = csv.reader(f)
        
        next(lineas)
        for i, linea in enumerate(lineas):
            try:
                costo += (int(linea[1]) * float(linea[2]))
            except ValueError:
                # muestro la línea i+2, ya que la primera corresponde al encabezado
                # de esta forma puedo saber que línea del archivo está el error.
                print(f'Ocurrió un error al leer la línea {i+2} del archivo')
    return costo


#### Programa Principal ####
costo = costo_camion('../Data/camion.csv')
print('Costo total:', costo) # Costo total: 47671.15
