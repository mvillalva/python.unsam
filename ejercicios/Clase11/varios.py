def es_potencia(n, b):
    if n == 1 or b in (0,1):
        return True
    elif n % b == 0:
        return es_potencia(n//b, b)
    else:
        return False
    
    
def replicar(lista, n):
    pass
    
    
if __name__ == '__main__':
    print(es_potencia(8,2))
    print(es_potencia(64,4))
    print(es_potencia(70,10))
    print(es_potencia(1,2))
    print(replicar([1,3,3,7], 2))
    