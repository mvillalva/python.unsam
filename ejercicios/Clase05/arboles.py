import csv
import numpy as np
import matplotlib.pyplot as plt


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


def medidas_de_especies(especies, arboleda):
    medidas={especie: [(arbol['altura_tot'], arbol['diametro']) for arbol in arboleda if arbol['nombre_com'] == especie] for especie in especies}
    return medidas


def imprimir_titulo(titulo):    
    print()
    print('#'*len(titulo))
    print(titulo)
    print('#'*len(titulo))
    print()



# Ejercicio 5.25
def ejercicio525():
    archivo = '../Data/arbolado-en-espacios-verdes.csv'
    arboleda = leer_arboles(archivo)    

    altos = [arbol['altura_tot'] for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
    
    plt.hist(altos, bins=50)
    plt.show()


# Ejercicio 5.26

def scatter_hd(lista_de_pares):
    datos = np.array(lista_de_pares)
    N = datos.shape[0]
    colors = datos[:,1] * datos[:,0]
    area = (10 * np.random.rand(N))**2
    
    plt.scatter(datos[:,1], datos[:,0], s=area, c=colors, alpha=0.5)
    plt.xlim(0,150) 
    plt.ylim(0,40)
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")  
    plt.title("Relación diámetro-alto")
    plt.show()


def ejercicio526():
    archivo = '../Data/arbolado-en-espacios-verdes.csv'
    arboleda = leer_arboles(archivo)
    scatter_hd([(arbol['altura_tot'], arbol['diametro']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá'])
    #plt.show()
    


# Ejercicio 5.27
def ejercicio527():
    archivo = '../Data/arbolado-en-espacios-verdes.csv'
    arboleda = leer_arboles(archivo)
    especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    medidas = medidas_de_especies(especies, arboleda)
    
    for m in medidas:        
        scatter_hd(medidas[m])
    #plt.show()


def main():
    opcion = ''
    while opcion.lower() != 's':
        imprimir_titulo('### Menú ###')        
        print('1. Ejercicio 5.25')
        print('2. Ejercicio 5.26')
        print('3. Ejercicio 5.27')
        print('S. Salir')        

        opcion = input(': ')

        if opcion == '1':
            ejercicio525()
        elif opcion == '2':
            ejercicio526()
        elif opcion == '3':
            ejercicio527()
        
        if opcion.lower() != 's':
            _ = input("ENTER para continuar...")

    
if __name__ == '__main__':
    main()