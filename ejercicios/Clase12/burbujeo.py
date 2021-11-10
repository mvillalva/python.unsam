def ord_burbujeo(lista):    
    l = len(lista)-1
    hay_cambio = True
    i = 0
    
    while hay_cambio:
        hay_cambio = False
        for j in range(0,l-i):            
            if(lista[j] > lista[j+1]):
                hay_cambio = True
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux        
        i += 1
        
    return lista
        
def ord_burbujeo_r(lista):    
    if len(lista) == 1:
        return lista
    
    l = len(lista)-1
    for i in range(l):
        if lista[i] > lista[i+1]:
            aux = lista[i]
            lista[i] = lista[i+1]
            lista[i+1] = aux
    
    return ord_burbujeo(lista[:-1]) + lista[-1:]

    
if __name__ == '__main__':
    lista_1 = [1, 2, -3, 8, 1, 5]
    print(ord_burbujeo(lista_1))
    
    lista_2 = [1, 2, 3, 4, 5]
    print(ord_burbujeo(lista_2))

    lista_3 = [0, 9, 3, 8, 5, 3, 2, 4]
    print(ord_burbujeo(lista_3))

    lista_4 = [10, 8, 6, 2, -2, -5]
    print(ord_burbujeo(lista_4))

    lista_5 = [2, 5, 1, 0]
    print(ord_burbujeo(lista_5))