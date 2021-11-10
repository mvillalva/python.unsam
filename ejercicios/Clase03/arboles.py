import csv
from collections import Counter
from pprint import pprint

# Ejercicio 3.18
def leer_parque(nombre_archivo, parque=''):
    arboles = []
    
    with open(nombre_archivo, 'rt', encoding='utf-8') as f:    
        lineas = csv.reader(f)
        
        encabezados = next(lineas)
        
        for i, linea in enumerate(lineas):
            record = dict(zip(encabezados, linea))
            try:
                if not parque or record['espacio_ve'].upper() == parque.upper():
                    record['altura_tot'] = float(record['altura_tot'])
                    record['inclinacio'] = int(record['inclinacio'])
                    arboles.append(record)
            except ValueError:
                print(f'Ocurrió un error al leer la línea {i+2} del archivo "{nombre_archivo}"\n')

    return arboles


# Ejercicio 3.19
def especies(lista_arboles):
    especie = []
    for arbol in lista_arboles:
        especie.append(arbol['nombre_com'])    
    return set(especie)


# Ejercicio 3.20
def contar_ejemplares(lista_arboles):
    ejemplares = Counter()
    for arbol in lista_arboles:
        ejemplares[arbol['nombre_com']] += 1
    
    return ejemplares

    
def ejemplares_mas_comunes(lista_arboles, cantidad):
    ejemplares = contar_ejemplares(lista_arboles)
    
    return ejemplares.most_common(cantidad)

        
def imprimir_top_ejemplares(parques, cantidad):
    header = ''
    rows = {}
    primero = True
    titulo = f'\nTOP {cantidad} DE EJEMPLARES'
    print(titulo)
    print('-'*len(titulo), end='\n\n')
    
    for parque in parques:
        arboles = leer_parque('../Data/arbolado-en-espacios-verdes.csv', parque)    
        ejemplares = ejemplares_mas_comunes(arboles, cantidad)
        
        header += f'{parque:<28s}'        
        row = ''        
        for i, ejemplar in enumerate(ejemplares):
            row = f'{ejemplar[0]}: {ejemplar[1]}'
            if primero:
                rows[i] = f'{row:<28s}'
            else:
                rows[i] += f'{row:<28s}'
        
        primero = False

    print(header)
    print('-'*len(header))
    for r in rows:
        print(rows[r])
    

# Ejercicio 3.21
def obtener_alturas(lista_arboles, especie):
    alturas = []
    for arbol in lista_arboles:        
        if arbol['nombre_com'].lower() == especie.lower():            
            alturas.append(arbol['altura_tot']) 
    
    return alturas


def imprimir_alturas(parques, especie):    
    header = f'{"Medida":<15s}'
    rows = {}
    primero = True
    titulo = f'\nALTURAS DEL ARBOL {especie}'
    print(titulo)
    print('-'*len(titulo), end='\n\n')
    
    for parque in parques:
        arboles = leer_parque('../Data/arbolado-en-espacios-verdes.csv', parque)        
        alturas = obtener_alturas(arboles, especie)
        
        maxima = max(alturas)
        promedio = sum(alturas) / len(alturas)
        header += f'{parque:<15s}'
        
        if primero:
            rows[1] = f'{"max":<15s}{maxima:<15.2f}'
            rows[2] = f'{"prom":<15s}{promedio:<15.2f}'
            primero = False
        else:
            rows[1] += f'{maxima:<15.2f}'
            rows[2] += f'{promedio:<15.2f}'        

    print(header)
    print('-'*len(header))
    for r in rows:
        print(rows[r])
        

#Ejercicio 3.22
def obtener_inclinaciones(lista_arboles, especie):
    inclinaciones = []
    for arbol in lista_arboles:        
        if arbol['nombre_com'].lower() == especie.lower():            
            inclinaciones.append(arbol['inclinacio']) 

    return inclinaciones


def imprimir_inclinaciones(parques, especie):
    titulo = f'\nINCLINACIONES DEL ARBOL {especie}'
    row = ''
    
    print(titulo)
    print('-'*len(titulo), end='\n\n')
    
    for parque in parques:
        arboles = leer_parque('../Data/arbolado-en-espacios-verdes.csv', parque)        
        inclinaciones = obtener_inclinaciones(arboles, 'Jacarandá')
                
        print(parque)
        
        for i, inclinacion in enumerate(inclinaciones):
            row += f'{inclinacion:>3d},'

        print(row, end='\n\n')
        

# Ejercicio 3.23
def especimen_mas_inclinado(lista_arboles):    
    maximas_inclianciones = {}
    
    lista_especies = especies(lista_arboles)
    for especie in lista_especies:
        inclinaciones = obtener_inclinaciones(lista_arboles, especie)
        maxima = max(inclinaciones)
        maximas_inclianciones[especie] =  maxima
        
    return maximas_inclianciones
            

def imprimir_max_inclinaciones(parques):
    titulo = '\nMÁXIMAS INCLINACIONES POR PARQUES Y ESPECIMEN'    
    
    print(titulo)
    print('-'*len(titulo), end='\n\n')
    
    for parque in parques:
        arboles = leer_parque('../Data/arbolado-en-espacios-verdes.csv', parque)        
        inclinaciones = especimen_mas_inclinado(arboles)        
        
        print(parque)
        print('-'*len(parque))
        
        for inc in sorted(inclinaciones):
            print(f'{inc}: {inclinaciones[inc]}')
        
        print('', end='\n\n')
    

# Ejercicio 3.24
def especie_promedio_mas_inclinada(lista_arboles):
    prom_max_inclianciones = {}
    
    lista_especies = especies(lista_arboles)
    for especie in lista_especies:
        inclinaciones = obtener_inclinaciones(lista_arboles, especie)
        prom = sum(inclinaciones)/len(inclinaciones)
        prom_max_inclianciones[especie] =  prom
    
    maxima = max(prom_max_inclianciones, key = prom_max_inclianciones.get)
    
    return (maxima, prom_max_inclianciones[maxima])


# Ejercicio 3.24 y Extra
def imprimir_prom_max_inclinaciones(parques=''):
    if (parques):
        titulo = '\nPROMEDIO MÁXIMO DE INCLINACION POR PARQUE'
    else:
        titulo = '\nPROMEDIO MÁXIMO DE INCLINACION EN LA CIUDAD'
    
    print(titulo)
    print('-'*len(titulo), end='\n\n')
    
    if parques:
        for parque in parques:
            arboles = leer_parque('../Data/arbolado-en-espacios-verdes.csv', parque)        
            especie, promedio = especie_promedio_mas_inclinada(arboles)
                    
            print(f'{especie} del parque {parque} tiene un promedio de inclinación de {promedio} grados')
            print('', end='\n\n')
    else:
        arboles = leer_parque('../Data/arbolado-en-espacios-verdes.csv')
        especie, promedio = especie_promedio_mas_inclinada(arboles)
        print(f'{especie} es la especie con mayor promedio de inclinación en la Ciudad: {promedio} grados')
        print('', end='\n\n')
                

        
# Programa Princiapl
def main():
    parques = ['GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO']
    
    print(f'\nLISTADO DE ARBOLES DEL PARQUE {parques[0]}')
    print('-'*18, end = '\n\n')
    arboles = leer_parque('../Data/arbolado-en-espacios-verdes.csv', parques[0])
    pprint(arboles)
    
    print('\nESPECIES')
    print('-'*8, end = '\n\n')
    pprint(especies(arboles))
    
    print('\nCONTADOR')
    print('-'*8, end = '\n\n')
    pprint(contar_ejemplares(arboles))
    
    imprimir_top_ejemplares(parques, 5)
    imprimir_alturas(parques, 'Jacarandá')
    imprimir_inclinaciones(parques, 'Jacarandá')
    imprimir_max_inclinaciones(parques)
    
    # Máximia inclinación por parque
    imprimir_prom_max_inclinaciones(parques)
    
    # Máximia inclinación en toda la Ciudad
    imprimir_prom_max_inclinaciones()
    
if __name__ == '__main__':
    main()