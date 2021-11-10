def incrementar(s):
    carry = 1
    l = len(s)

    for i in range(l-1,-1,-1):
        if (s[i] == 1 and carry == 1):
            s[i] = 0
            carry = 1
        else:
            s[i] = s[i] + carry
            carry = 0        
    return s


def listar_secuencias(n):
    lista = [0]*n
    print(lista)
    for i in range(2**n):
        lista = incrementar(lista)
        print(lista)    


if __name__ == '__main__':
    listar_secuencias(20)