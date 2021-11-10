#Ejercicio 2.10: Ejecución desde la línea de comandos con parámetros
import csv
import sys

def costo_camion(nombre_archivo):
    costo = 0
    try:
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
    except:
        print("Ocurrió un error al leer el archivo, verifique que exista.")
        return -1


#### Programa Principal ####
nombre_archivo = '../Data/camion.csv'

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]

costo = costo_camion(nombre_archivo)
if costo != -1:
    print('Costo total:', costo) 

#camion.csv: Costo total: 47671.15
#missing.csv: Ocurrió un error al leer la línea 5 del archivo
#             Ocurrió un error al leer la línea 8 del archivo
#             Costo total: 30381.15
