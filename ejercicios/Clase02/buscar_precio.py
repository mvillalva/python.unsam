# Ejercicio 2.7: Buscar precios
def buscar_precio(vegetal_a_buscar):        
    with open('../Data/precios.csv', 'rt', encoding='utf-8') as f:
        vegetales = f.read().split('\n')
    
    for vegetal in vegetales:
        elemento = vegetal.split(',')
        if elemento[0].lower() == vegetal_a_buscar.lower():
             return(f"El precio de un cajón de {vegetal_a_buscar} es ${elemento[1]}")
                
    return(f"{vegetal_a_buscar.capitalize()} no figura en el listado de precios.")


#### Programa Principal ####
print(buscar_precio('Frambuesa')) #El precio de la Frambuesa es de $34.35
print(buscar_precio('Kale')) #Kale no figura en el listado de precios.