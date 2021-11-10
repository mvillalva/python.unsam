import informe_funciones

def costo_camion(nombre_Archivo):
    filas = informe_funciones.leer_camion(nombre_Archivo)
    costo_total = sum([f['cajones']*f['precio'] for f in filas])    
    return costo_total
    # Esto de abajo no iría
    # with open( nombre_Archivo) as f:
    #     filas=csv.reader(f)
    #     encabezados=next(filas)
    #     fila=next(filas)
    #     costo_total=0
    #     for n_fila,fila in enumerate(filas,start=1):
    #         record=dict(zip(encabezados,fila))
    #         try:
    #             ncajones=int(record['cajones'])
    #             precio=float(record['precio'])
    #             costo_total += ncajones*precio
                
    #         except ValueError:
    #             print(f'Fila{n_fila}:No puede intepretar:{fila}')
        
    #     return costo_total
        

# camion=informe_funciones.leer_camion ('C:/Users/User2021/Documents/python/unsam/archivos/Data/missing.csv')

# print(camion)

if __name__ == '__main__':
    costo = costo_camion('../Data/fecha_camion.csv')
    print('Costo total:', costo) # Costo total: 47671.15