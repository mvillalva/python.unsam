from informe_funciones import leer_camion

def costo_camion(nombre_archivo):    
    camion = leer_camion(nombre_archivo)
    costo = sum([c['cajones']*c['precio'] for c in camion])    
    return costo


if __name__ == '__main__':
    costo = costo_camion('../Data/fecha_camion.csv')
    print('Costo total:', costo) # Costo total: 47671.15
