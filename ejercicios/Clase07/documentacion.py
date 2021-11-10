def valor_absoluto(n):
    '''Calcula el valor absoluto de un número.
    Si n >= 0 devulve el número, si no, le cambia el signo

    Pre: n es un número
    Pos: Se devuelve el valor absoluto de n

    '''
    if n >= 0:
        return n
    else:
        return -n


def suma_pares(l):
    '''Calcula la suma de números pares de una lista.    
    
    Pre: l es una lista de números enteros.
    Pos: Devuelve el valor de sumar todos los pares de la lista.
         Si la lista esta vaciá entonces devuelve cero.
    '''
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0

    return res
    #res es una invariante, ya que si la lista es vacía devuelve 0


def veces(a, b):
    '''Calcula la suma de a, b veces

    Pre: a y b son número.
    Pos: Devuelve el valor de sumar a, b veces. Si b es igual a cero devuelve 0
    '''
    res = 0
    nb = b
    #Si b es negativo se produce un deadlock
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res
    #res es una invariante, ya que si b es 0 devuelve 0


def collatz(n):
    '''Calcula la Conjetura de Collatz.
    Si el número es par, se divide entre 2.
    Si el número es impar, se multiplica por 3 y se suma 1.

    Pre: n es un número natural
    Pos: Devuelve la cantidad de secuencias hasta el n se convierte en 1
    '''
    res = 1

    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1

    return res
    # res es una invariante, porque si n es 1 devuelve ese valor.