def donde_insertar(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada    
    Devuelve p tal que lista[p] == x, si x está en lista
    Devuelve p donde insertar si no esta en lista
    '''
    if verbose:
        print('[DEBUG] izq |der |medio |pos')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:5d} |{pos:3d}')
        if lista[medio] == x:
            pos = medio
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda    
            
    # si no ecnotró, verifico desde donde quedó el medio y pregunto para la derecha o izquierda    
    if pos == -1: 
        if lista[medio] > x: # si el valor de la lista es mayor a x entonces 
            pos = medio      # tengo que devolver esa posicion
        else:                # si el valor de la lista es menor a x entonces 
            pos = medio + 1  # tengo que devolver esa posicion + 1
            
    return pos


def insertar(lista, x):
    if x in lista:
        pos = lista.index(x)
    else:
        pos = donde_insertar(lista, x)
        if pos < len(lista):
            lista.insert(pos, x)
        else:
            lista.append(x)
    
    return pos


if __name__ == '__main__':
    lista = [1,2,6,8,9,13,16,20,56]
    x = 19
    pos= insertar(lista, x)
    print(pos, lista)
    
    for i in range(21):
        pos= insertar(lista, i)
        print(pos, lista)
    
