def buscar_precio(nombre_fruta):
  
  with open('../Data/precios.csv', 'rt') as f:
    salida = ''

    for line in f:
      row = line.split(',')
      if row[0] == nombre_fruta:
        salida = f'El precio del cajón de {nombre_fruta} es: ${row[1]}'
        return salida
        #Poniendo return estás haciendo que la función no siga ejecutandose,
        # por lo tanto, todo lo que esté después de ese return no se va a ejecutar,
        # entonces, no es necesario poner un else o elif si no se cumple la condición.

        #Si luego de leer el archivo nunca entro a if row[0] == nombre_fruta:
        # quiere decir que no existe lo que estas buscando, entonces la función 
        # va a llegar hasta la línea que esta aca abajo, porque no ejecutó el return del if
    
  salida = f'{nombre_fruta} no figura en el listado de precios'    
  return salida


fruta = input('Ingrese la fruta: ')
print(buscar_precio(fruta))