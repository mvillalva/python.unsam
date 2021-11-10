import os


def archivos_png(nombre_archivo):
    lista = []

    for raiz, dirs, archivos in os.walk(nombre_archivo):
        for archivo in archivos:
            if archivo.endswith('.png'):
                lista.append(archivo)
    
    return lista    


def f_principal(parametros):
    if len(parametros) != 2:
        raise SystemExit(f'Uso adecuado: {parametros[0]} ' 'nombre_archivo')

    print(archivos_png(parametros[1]))


if __name__ == '__main__':    
    import sys
    f_principal(sys.argv)