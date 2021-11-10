import os
from datetime import datetime


def procesar_nombre(fname):
    nombre = os.path.basename(fname)
    fecha = datetime.strptime(nombre[-12:-4], '%Y%m%d')
    nombre = nombre[:-13] + '.png'
    return nombre, fecha
    

def procesar(fname, destino = ''):
    '''
    Copia el archivo pasado en fname en el directorio destino, si no se especifica el destino
    solo renombra el archivo del directorio origen

    Pre: recibe la ruta relativa con el archivo a reemplazar y opcional el destino donde se 
    moverá
    Pos: Si el destino es vacío reemplaza el archivo actual
    '''
    fn_destino = ''    
    
    fn_origen = os.path.realpath(fname) # obtengo la ruta completa del archivo
    
    nombre, fecha = procesar_nombre(fname)
    
    if destino:
        destino = os.path.realpath(destino) # obtengo la ruta completa del directorio
        fn_destino = os.path.join(destino, nombre) # adjunto el nuevo nombre de archivo
    else:
        fn_destino = os.path.dirname(fn_origen)
        fn_destino = os.path.join(fn_destino, nombre)
        
    os.rename(fn_origen, fn_destino)
    
    fecha_acceso = datetime(year = fecha.year , month = fecha.month, day = fecha.day, hour = fecha.hour, minute = fecha.minute, second = fecha.second)
    fecha_modifi = datetime(year = fecha.year , month = fecha.month, day = fecha.day, hour = fecha.hour, minute = fecha.minute, second = fecha.second)
    
    ts_acceso = fecha_acceso.timestamp()
    ts_modifi = fecha_modifi.timestamp()
    os.utime(fn_destino, (ts_acceso, ts_modifi))    
    
    
def borrar_directorios(raices):
    for raiz in reversed(raices):
        try:
            os.rmdir(raiz)
        except Exception as e:
            print(e)
            

def main(parametros):
    if len(parametros) != 3:
        raise SystemExit(f'Uso adecuado: {parametros[0]} ' 'directorio_origen directorio_destino')
    
    destino = parametros[2]
    
    if not os.path.exists(destino): #si no existe el directorio lo creo
            os.mkdir(destino)
    
    raices  = []
    
    for raiz, dirs, archivos in os.walk(parametros[1]):
        raices.append(raiz)
        for archivo in archivos:
            if archivo.endswith('.png'):
                procesar(os.path.join(raiz, archivo), destino)
    
    borrar_directorios(raices)
    
    

if __name__ == '__main__':
    import sys    
    main(sys.argv)
