def tabla_multiplicar():    
    print(' ' * 4, end ='')
    line = '-' * 4
    
    for h in range(10):
        print(f'{h:>4d}', end='')
        line += '-' * 4
    
    print('\n'+line)
    
    for i in range(10):
        print(f'{i:>2}:', end=' ')
        suma = 0
        for j in range(10):
            print(f'{suma:>4d}', end='')
            suma += i
        print('')


tabla_multiplicar()