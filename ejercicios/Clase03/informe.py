#IMPORTATE!!! Para correr el ejercicio debe copiarse el archivo dentro del directorio Clase02...
# y además la consola debe estar posicionada en ese directorio.
# Si no al no encontrar el archivo arrojaría el siguiente error:
# FileNotFoundError: [Errno 2] No such file or directory: '../Data/camion.csv'

#Ejercicio 3.9: Balances
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


#### Programa Principal ####
precio_c_tot = 0
precio_v_tot = 0

camiones = leer_camion('../Data/camion.csv')
vegetales = leer_precios('../Data/precios.csv')

print('Producto    Camion($)   Venta($)   Ganancia($)')
print('========    =========   ========   ===========')

for camion in camiones:
    try:        
        nombre = camion['nombre']        
        precio_c = camion['precio'] * camion['cajones']
        precio_v = vegetales[nombre] * camion['cajones']
        ganancia = precio_v - precio_c
        precio_c_tot += precio_c
        precio_v_tot += precio_v
        print(nombre.ljust(12) + f'{precio_c:.2f}'.rjust(9) + f'{precio_v:.2f}'.rjust(11) + f'{ganancia:.2f}'.rjust(14))
    except:
        pass

ganancia_tot = precio_v_tot - precio_c_tot

print('========    =========   ========   ===========')
print('Total:'.ljust(12) + f'{precio_c_tot:.2f}'.rjust(9) + f'{precio_v_tot:.2f}'.rjust(11) + f'{ganancia_tot:.2f}'.rjust(14))


# Salida por pantalla:
    
# Producto    Camion($)   Venta($)   Ganancia($)
# ========    =========   ========   ===========
# Lima          3220.00    4022.00        802.00
# Naranja       4555.00    5314.00        759.00
# Caqui        15516.00   15819.00        303.00
# Mandarina    10246.00   16178.00       5932.00
# Durazno       3835.15    6980.60       3145.45
# Mandarina     3255.00    4044.50        789.50
# Naranja       7044.00   10628.00       3584.00
# ========    =========   ========   ===========
# Total:       47671.15   62986.10      15314.95
