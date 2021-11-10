import csv
from collections import Counter

# Ejercicio 4.15
def leer_arboles(nombre_archivo):
    arboles = []

    with open(nombre_archivo, 'rt', encoding='utf-8') as f:    
        lineas = csv.reader(f)
        
        encabezados = next(lineas)

        tipos = [float, float, int, int, int, int, int, str, str, str, str, str, str, str, str, float, float]

        for i, linea in enumerate(lineas):
            try:
                record = dict(zip(encabezados, [parse(dato) for parse, dato in zip(tipos, linea)]))
                arboles.append(record)
            except ValueError:
                print(f'Ocurrió un error al leer la línea {i+2} del archivo "{nombre_archivo}"\n')

    return arboles


# Ejercicio 4.18
def medidas_de_especies(especies, arboleda):
    medidas={especie: [(arbol['altura_tot'], arbol['diametro']) for arbol in arboleda if arbol['nombre_com'] == especie] for especie in especies}
    return medidas


def main():
    archivo = '../Data/arbolado-en-espacios-verdes.csv'
    arboleda = leer_arboles(archivo)
    especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']

    # Ejercicio 4.16
    H=[arbol['altura_tot'] for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
    print(H)

    # Ejercicio 4.17
    T=[(arbol['altura_tot'], arbol['diametro']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
    print(T)

    # Ejercicio 4.18
    c = Counter()
    especie = medidas_de_especies(especies, arboleda)
    
    for e in especie:
        for t in especie[e]: 
            c[e] += 1
    print(c)

    
if __name__ == '__main__':
    main()