from fileparse import parse_csv

def leer_camion(nombre_archivo):
    '''
    Lee datos de lo que transporta un camión de un archivo de datos CSV con tres columnas.    

    Parameters
    ----------
    nombre_archivo : str
    La primera columna debe contener un nombre, la segunda una cantidad y la tercera un precio.

    Returns
    -------
    camion : list
    Devuelve una lista de diccionarios [{nombre: nombre, cajones: cantidad, precio: precio},...]
    '''
    return parse_csv(nombre_archivo, select = ['nombre', 'cajones', 'precio'], types=[str, int, float])


def leer_precios(nombre_archivo):
    '''
    Lee precios de un archivo de datos CSV con dos columnas.

    Parameters
    ----------
    nombre_archivo : str
    La primera columna debe contener un nombre y la segunda un precio.

    Returns
    -------
    elementos : dict
    Devuelve un diccionario {nombre:precio, ...}
    '''
    return parse_csv(nombre_archivo, types=[str, float], has_headers=False)


def hacer_informe(camion, precios):
    '''
    Arma los datos para la impresión.

    Parameters
    ----------
    camion : list
        Lista con los nombre, cantidades y precios de cada cajón de vegetales
    precios : dict
        Diccionario con los precios de los vegetales

    Returns
    -------
    lista : list
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
    Imprime por pantalla un resumen con los vegetales, la cantidad de cajones que se compraron,
    el precio de venta y la diferencia entre la venta y la compra.
    
    Parameters
    ----------
    informe : list
        lista de tuplas con el nombre del vegetal, su cantidad, el precio de venta 
        y la diferencia entre el precio de venta y compra
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

    Parameters
    ----------
    nombre_archivo1 : str
        Nombre del archivo que contiene los datos del camión
    nombre_archivo2 : str
        Nombre del archivo que contiene los datos de los precios de venta de cada vegetal.
    '''
    
    camion = leer_camion(nombre_archivo1)
    precios = leer_precios(nombre_archivo2)
    informe = hacer_informe(camion, precios)
    
    imprimir_informe(informe)
    
    
def main():
    informe_camion('../Data/camion2.csv', '../Data/precios.csv')
    
    files = ['../Data/camion.csv', '../Data/camion2.csv']
    for name in files:
        print(f'{name:-^43s}')
        informe_camion(name, '../Data/precios.csv')
        print()


if __name__ == '__main__':
    main()