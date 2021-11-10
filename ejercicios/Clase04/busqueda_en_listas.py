# Ejercicio 4.3
def buscar_u_elemento(lista, elemento):
    pos = -1
    for i, e in enumerate(lista):
        if e == elemento:
            pos = i
    
    return pos


def buscar_n_elemento(lista, elemento):
    cant = 0
    for i, e in enumerate(lista):
        if e == elemento:
            cant += 1
    
    return cant


# Ejercicio 4.4
def maximo(lista):    
    ''' Devuelve el máximo de una lista, 
        la lista debe ser no vacía y de números positivos.
    '''
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = lista[0] # Lo inicializo con el primer valor de la lista porque 
                 # si lo inicializo en 0 y me pasan solo números negativos el 0 siempre va a ser mayor
    for e in lista: # Recorro la lista y voy guardando el mayor    
        if e > m:
            m = e

    return m


def main():
    lista = [1,2,3,2,10,3,4]
    lista2 = [-5,-2,-9]
    elemento = 3
    
    print()
    print(f'La última posición del elemento {elemento} en la lista {lista} es: {buscar_u_elemento(lista, elemento)}', end ='\n\n')
    print(f'La cantidad de veces que aparece el elemento {elemento} en la lista {lista} es: {buscar_n_elemento(lista, elemento)}', end ='\n\n')
    print(f'El máximo valor de la lista {lista2} es: {maximo(lista2)}', end ='\n\n')


if __name__ == '__main__':
    main()