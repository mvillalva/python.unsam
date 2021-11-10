def bbinaria_rec(lista, e):
    if len(lista) == 0:
        res = False
    elif len(lista) == 1:
        res = lista[0] == e
    else:
        medio = len(lista)//2
        
        res = lista[medio] == e
        
        if not res:
            if lista[medio] < e:
                res = bbinaria_rec(lista[medio:], e)
            else:
                res = bbinaria_rec(lista[:medio], e)

    return res


if __name__ == '__main__':
    lista = [1,2,3,4,5,6,7,8,9,10,21,22,23,44,55,56,57,80]
    print(bbinaria_rec(lista, 0))