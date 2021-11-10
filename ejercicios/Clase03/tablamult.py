def header():    
    header = ' ' * 4
    line = '-' * 4
    for i in range(0,10):
        header += f'{i:>4d}'
        line += '-' * 4
    print(header)
    print(line)


def row(pos):
    fila = f'{pos:>2}: '
    for j in range(0,10):
        suma = 0
        for h in range(0,pos):
            suma += j
        fila += f'{suma:>4d}'
    
    return fila


def tabla_multiplicar():
    header()    
    for i in range(0,10):        
        print(row(i))


tabla_multiplicar()
