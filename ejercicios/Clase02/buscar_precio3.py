def buscar_precio(nombre_fruta):    

    with open('../Data/precios.csv', 'rt') as f:
        salida = ''
        
        for line in f:       
            row = line.split(',')
            if row[0] == nombre_fruta:            
                salida = f'El precio del cajón de {nombre_fruta} es: ${row[1]}'
                return salida
            
    salida = f'{nombre_fruta} no figura en el listado de precios'
    return salida
    
fruta = input('Ingrese fruta') 
a = buscar_precio(fruta)
print(a)