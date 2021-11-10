from fileparse import parse_csv

def leer_camion(nombre_archivo):
    '''
    Lee datos de lo que transporta un camión de un archivo de datos CSV con tres columnas.
    Devuelve una lista de diccionarios [{nombre: nombre, cajones: cantidad, precio: precio},...]
    '''
    with open(nombre_archivo, 'rt', encoding='utf-8') as f:
        return parse_csv(f, select = ['nombre', 'cajones', 'precio'], types=[str, int, float])


def leer_precios(nombre_archivo):
    '''
    Lee precios de un archivo de datos CSV con dos columnas.
    Devuelve un diccionario {nombre:precio, ...}
    '''
    with open(nombre_archivo, 'rt', encoding='utf-8') as f:
        return parse_csv(f, types=[str, float], has_headers=False)


def hacer_informe(camion, precios):
    '''
    Arma los datos para la impresión de una lista y diccionario
    Devuelve una lista de tuplas con el nombre del vegetal, su cantidad, el precio de venta 
    y la diferencia entre el precio de venta y compra
    '''    
    lista = []
    
    precios = dict(precios)
    for c in camion:
        nombre = c['nombre']
        datos = (nombre, c['cajones'], c['precio'], precios[nombre] - c['precio'])
        lista.append(datos)
    
    return lista


def imprimir_informe(informe):
    '''
    Imprime por pantalla una lista de tuplas con los vegetales, la cantidad de cajones que se compraron,
    el precio de venta y la diferencia entre la venta y la compra.
    '''
    cajones_tot = 0
    precio_tot = 0
    cambio_tot = 0
    
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    
    print(f'{headers[0]:^11s} {headers[1]:^11s} {headers[2]:^11s} {headers[3]:^11s}')
    print('----------- '*4)
    
    for nombre, cajones, precio, cambio in informe:
        cajones_tot += cajones
        precio_tot += precio
        cambio_tot += cambio
        print(f'{nombre:<10s} {cajones:>11d} {f"${precio:.2f}":>11s} {f"${cambio:.2f}":>11s}')
    
    print('=========== '*4)
    print(f'{"Total":<10s} {cajones_tot:>11d} {f"${precio_tot:.2f}":>11s} {f"${cambio_tot:.2f}":>11s}')


def informe_camion(nombre_archivo1, nombre_archivo2):
    '''
    Imprime el informe de los archivos que recibe como parámetro
    '''
    
    camion = leer_camion(nombre_archivo1)
    precios = leer_precios(nombre_archivo2)
    informe = hacer_informe(camion, precios)
    
    imprimir_informe(informe)
    
    
def f_principal(parametros):
    if len(parametros) != 3:
        raise SystemExit(f'Uso adecuado: {parametros[0]} ' 'archivo_camion archivo_precios')

    informe_camion(parametros[1], parametros[2])


if __name__ == '__main__':
    import sys
    f_principal(sys.argv)