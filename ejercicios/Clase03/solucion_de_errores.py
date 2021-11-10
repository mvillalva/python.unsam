#%% Ejercicio 3.1: Semántica
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        else:
            return False
        i += 1

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')

# El error esta en if expresion[i] == 'a': 
# El primer caso devuelve False porque al no encontrar como primera letra una "a" devuelve false 
# y sale de la función, ademas no contempla la mayúsculas o acentos
# El segundo caso devuelve True porque la primera letra de la cadeana es "a"
# El último caso devuelve False porque la pimera letra es distina de "a" 

#%% Ejercicio 3.1: Semántica (SOLUCION)
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i].lower() in ('a','á'):
            return True        
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')
tiene_a('Ese oso es enorme')
tiene_a('Está bien')
tiene_a('Á')

#%% Ejercicio 3.2: Sintaxis
def tiene_a(expresion)
    n = len(expresion)
    i = 0
    while i<n
        if expresion[i] = 'a'
            return True
        i += 1
    return Falso

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')

# Faltan los ":" para cerrar las instrucciones
# El if tiene un solo "="
# No contempla Mayúsculas o acentos
# el último return devuelve "Falso" y no es reocnocido

#%% Ejercicio 3.2: Sintaxis (SOLUCION)
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i].lower() in ('a', 'á'):
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')


#%% Ejercicio 3.3: Tipos
def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)

#El problema está en la última llamada a la función "tiene_uno(1984)", porque está pasando un
# numero y la función luego quiere obtener la longitud del dato que se le pasa y al ser numérico da
# error porque "len" se utiliza en cadenas.

#%% Ejercicio 3.3: Tipos (SOLUCION)
def tiene_uno(expresion):
    str_expresion = str(expresion)
    n = len(str_expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if str_expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)

# Convertí expresión a cadena, y utilizo esa conversión para averiguar el tamaño y usarla
# en el condicional.

#%% Ejercicio 3.4: Alcances
def suma(a,b):
    c = a + b

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

# la función "suma" no esta retornando un valor

#%% Ejercicio 3.4: Alcances (SOLUCION)
def suma(a,b):
    return a + b

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")
# Cambie dentro de la función "suma" "c= a + b" por "return a + b"


#%% Ejercicio 3.5: Pisando memoria
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)

# El problema es el scope de la variable "registro", ya que es global a la función, por lo tanto,
# cuando itera las filas, esta modificando el dato de registro ya que accede por la misma clave 
# en cada iteración. Al hacer el append de "registro" en "camion" está haciendo que ese item apunte a la pos
# de memoria de "registro" entonces cada vez que canmbio el dato en registro se modifica en todos los
# items de camión.


#%% Ejercicio 3.5: Pisando memoria (SOLUCION)
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]    
    
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:  
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            
            camion.append(registro)
            
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)

# cambie el lugar de creación de "registro", poniendila dentro del "for"

