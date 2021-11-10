def sumar_enteros(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    resultado = 0

    if desde and hasta and hasta > desde:
        for i in range(desde, hasta+1):
            resultado += i

    return resultado


def sumar_enteros_2(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    resultado = 0

    if desde and hasta and hasta > desde:
        n_desde = ((desde-1)*(desde)) / 2
        n_hasta = (hasta*(hasta+1)) / 2
        resultado = n_hasta - n_desde

    return resultado


print(sumar_enteros(10,20))
print(sumar_enteros_2(10,20))