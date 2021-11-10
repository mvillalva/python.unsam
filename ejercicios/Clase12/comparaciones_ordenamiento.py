import random
import numpy as np
import matplotlib.pyplot as plt

def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    # posición final del segmento a tratar
    n = len(lista) - 1
    comparaciones = 0

    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p = buscar_max(lista, 0, n)
        comparaciones += n
        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]        

        # reducir el segmento en 1
        n = n - 1

    return comparaciones


def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""

    pos_max = a    
    for i in range(a + 1, b + 1):        
        if lista[i] > lista[pos_max]:
            pos_max = i
    
    return pos_max


def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    comparaciones = 0
    
    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        comparaciones += 1
        if lista[i + 1] < lista[i]:
            comparaciones += reubicar(lista, i + 1)
            
    return comparaciones

def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""

    v = lista[p]

    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    comparacion = 1
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        comparacion += 1
        lista[j] = lista[j - 1]
        j -= 1

    lista[j] = v
    
    return comparacion
    

def ord_burbujeo(lista):    
    comparaciones = 0
    l = len(lista)-1
    hay_cambio = True
    i = 0
    
    while hay_cambio:
        hay_cambio = False
        for j in range(0,l-i):
            comparaciones +=1
            if(lista[j] > lista[j+1]):
                hay_cambio = True
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux        
        i += 1
    
    return comparaciones


def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    comparacion = 1
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq, comp_izq = merge_sort(lista[:medio])
        der, comp_der = merge_sort(lista[medio:])
        lista_nueva, comp_merge = merge(izq, der)        
        comparacion += comp_izq + comp_der + comp_merge
    
    return lista_nueva, comparacion


def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []
    
    comparacion = 1
    
    while(i < len(lista1) and j < len(lista2)):
        comparacion +=1
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado, comparacion


def generar_lista(N):
    return  [random.randint(1, 1000) for i in range(N)]


def experimento(N, k):
    promedio = [0.0] * 3
    for i in range(k):
        lista = generar_lista(N)
        promedio[0] += ord_seleccion(lista.copy())
        promedio[1] += ord_insercion(lista.copy())
        promedio[2] += ord_burbujeo(lista.copy())        
    
    promedio[0] = promedio[0] / k
    promedio[1] = promedio[1] / k
    promedio[2] = promedio[2] / k    
    
    return (promedio[0], promedio[1], promedio[2])


def experimento_vectores(Nmax):    
    comparaciones_seleccion = np.zeros(Nmax)
    comparaciones_insercion = np.zeros(Nmax)
    comparaciones_burbujeo  = np.zeros(Nmax)
    comparaciones_merge     = np.zeros(Nmax)
    
    for i in range(Nmax):
      lista = generar_lista(i)
      comparaciones_seleccion[i] = ord_seleccion(lista.copy())
      comparaciones_insercion[i] = ord_insercion(lista.copy())
      comparaciones_burbujeo[i]  = ord_burbujeo(lista.copy())
      comparaciones_merge[i]     = merge_sort(lista.copy())[1]
      
    return comparaciones_seleccion, comparaciones_insercion, comparaciones_burbujeo, comparaciones_merge

         

def graficar(Nmax, comparaciones_seleccion, comparaciones_insercion, comparaciones_burbujeo, comparaciones_merge):
    largos = np.arange(Nmax) + 1
    
    plt.plot(largos, comparaciones_burbujeo, label = 'Burbujeo', color='red')
    plt.plot(largos, comparaciones_seleccion, label = 'Selección', linestyle='dashed', color='green')
    plt.plot(largos, comparaciones_insercion, label = 'Insersión', color='orange')
    plt.plot(largos, comparaciones_merge, label = 'Merge Sort', color='blue')
    plt.xlabel("Largo de la lista")
    plt.ylabel("Cantidad de comparaciones")
    plt.title("Métodos de ordenamiento")
    plt.legend()
    plt.show()


if __name__ == '__main__':       
    print(experimento(10,2))
    Nmax = 256
    comparaciones_seleccion, comparaciones_insercion, comparaciones_burbujeo, comparaciones_merge = experimento_vectores(Nmax)
    graficar(Nmax, comparaciones_seleccion, comparaciones_insercion, comparaciones_burbujeo, comparaciones_merge)
    
    