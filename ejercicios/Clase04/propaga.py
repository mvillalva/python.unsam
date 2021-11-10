def propagar(lista):    
    sigue = True

    while sigue: # Miestras que haya fósforos apagados al lado de uno encendido hago la búsqueda
        sigue = False
        for i, e in enumerate(lista):            
            if e == 1: # Si esta encendido analizo la izquierda y la derecha                
                if i < len(lista)-1 and lista[i+1] == 0: # Si no es el último fósforo y el de la derecha esta apagado...
                    lista[i+1] = 1                       # enciendo el fósforo de la derecha
                    sigue = True

                if i != 0 and lista[i-1] == 0: # Si no es el primer fósforo y el de la izquierda está apagado...
                    lista[i-1] = 1             # enciendo el fósforo de la izquierda
                    sigue = True

    return lista

def propagar_mejorada(lista):
    long = len(lista)-1 #esto lo uso luego para recorrer la lista
    
    for i, e in enumerate(lista):        
        if i < long and e == 1 and lista[i+1] == 0: 
            lista[i+1] = 1                
    
    for i, e in enumerate(reversed(lista)):                
        if i < long and e == 1 and lista[long-i-1] == 0:
            lista[long-i-1] = 1       

    return lista


def main():
    # lista = [ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]
    # lista2 = [ 0, 0, 0, 1, 0, 0]

    # print(f'La lista {lista} propagada quedó así: {propagar_mejorada(lista)}')
    # print(f'La lista {lista2} propagada quedó así: {propagar_mejorada(lista2)}')
    print(propagar([ 0, 0, 0, 1, 0, 0]))
    print(propagar([ 0, 0, 0, 0, 0, -1]))
    print(propagar([ 0, 0, 0, 0, 0, 1]))
    print(propagar([]))
    print(propagar([ 0 for _ in range(1000) ] + [1]))
    print(propagar([1] + [ 0 for _ in range(1000) ]))
    print(propagar([ (i% 6)//2-1 for i in range(200) ]))
    print(propagar([ -1*((i% 6)//2-1) for i in range(60) ]))


if __name__ == '__main__':
    main()