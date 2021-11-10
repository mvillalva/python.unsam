#IMPORTATE!!! Para correr el ejercicio debe copiarse el archivo dentro del directorio Clase02...
# y además la consola debe estar posicionada en ese directorio.
# Si no al no encontrar el archivo arrojaría el siguiente error:
# FileNotFoundError: [Errno 2] No such file or directory: '../Data/camion.csv'

#Ejercicio 2.18: Balances
import csv

def leer_camion(nombre_archivo):
    camion = []
    
    with open(nombre_archivo, 'rt') as f:    
        lineas = csv.reader(f)
        
        encabezados = next(lineas)
        
        for i, linea in enumerate(lineas):
            record = dict(zip(encabezados, linea))
            try:                
                record['cajones'] = int(record['cajones'])
                record['precio'] = float(record['precio'])
                camion.append(record)
            except ValueError:
                # muestro la línea i+2, ya que la primera corresponde al encabezado
                # de esta forma puedo saber que línea del archivo está el error.
                print(f'Ocurrió un error al leer la línea {i+2} del archivo "{nombre_archivo}"\n')

    return camion


def leer_precios(nombre_archivo):
    elementos = {}
    with open(nombre_archivo, 'rt', encoding='utf-8') as f:
        vegetales = csv.reader(f)
    
        for i, vegetal in enumerate(vegetales):
            try:
                elementos[vegetal[0]] = float(vegetal[1])
            except:            
                print(f'Ocurrió un error al leer la línea {i+2} del archivo "{nombre_archivo}"\n')
            
    return elementos


def hacer_informe(camion, precios):
    lista = []
    for c in camion:
        nombre = c['nombre']
        datos = (nombre, c['cajones'], c['precio'], precios[nombre] - c['precio'])
        lista.append(datos)
    
    return lista


#### Programa Principal ####
cajones_tot = 0
precio_tot = 0
cambio_tot = 0

camion = leer_camion('../Data/camion.csv')
precios = leer_precios('../Data/precios.csv')
informe = hacer_informe(camion, precios)

headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')

print(f'{headers[0]:^11s} {headers[1]:^11s} {headers[2]:^11s} {headers[3]:^11s}')
print('----------- '*4)

for nombre, cajones, precio, cambio in informe:
    cajones_tot += cajones
    precio_tot += precio
    cambio_tot += cambio
    print(f'{nombre:<10s} {cajones:>11d} {"$"+str(round(precio,2)):>11s} {cambio:>11.2f}')

print('=========== '*4)
print(f'{"Total":<10s} {cajones_tot:>11d} {"$"+str(round(precio_tot,2)):>11s} {cambio_tot:>11.2f}')


# Salida por pantalla:
    
#   Nombre      Cajones     Precio      Cambio   
# ----------- ----------- ----------- ----------- 
# Lima               100       $32.2        8.02
# Naranja             50       $91.1       15.18
# Caqui              150     $103.44        2.02
# Mandarina          200      $51.23       29.66
# Durazno             95      $40.37       33.11
# Mandarina           50       $65.1       15.79
# Naranja            100      $70.44       35.84
# =========== =========== =========== =========== 
# Total              745     $453.88      139.62
