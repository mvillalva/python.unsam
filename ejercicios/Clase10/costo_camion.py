from informe_final import leer_camion

def costo_camion(nombre_archivo):    
    '''
    Calcula el costo del camión dado un archivo
    '''

    camion = leer_camion(nombre_archivo)
    return camion.precio_total()


def f_principal(parametros):
    if len(parametros) != 2:
        raise SystemExit(f'Uso adecuado: {parametros[0]} ' 'archivo_camion')
    
    costo = costo_camion(parametros[1])
    print('Costo total:', costo) # Costo total: 47671.15


if __name__ == '__main__':
    import sys
    f_principal(sys.argv)
