#Ejercicio 2.3: Precio de la naranja
#%% v1.0
busqueda = 'naranja'
art = ''
encontro = False
precion = 0

with open('..\Data\precios.csv', 'rt', encoding='utf-8') as f:
    vegetales = f.read().split('\n')    

for vegetal in vegetales:
    elemento = vegetal.split(',')
    if elemento[0].lower() == busqueda:
        encontro = True
        precio = elemento[1]
        art = 'l'
        if busqueda[-1] == 'a':
            art = ' la'
            
if encontro:
    print(f"El precio de{art} {busqueda} es de ${precio}")
else:
    print(f"{busqueda.capitalize()} no figura en el listado de precios.")
    
#El precio de la Naranja es de $106.28

#%% V2.0
busqueda = 'naranja'
with open('..\Data\precios.csv', 'rt', encoding='utf-8') as f:
    vegetales = f.read().split('\n')    

art = ''
indice = 0
precio = 0
encontro = False
cantidad = len(vegetales)

while indice < cantidad and not encontro:    
    elemento = vegetales[indice].split(',')
    if elemento[0].lower() == busqueda:
        precio = elemento[1]
        art = 'l'
        if busqueda[-1] == 'a':
            art = ' la'
        encontro = True
    indice += 1

if encontro:
    print(f"El precio de{art} {busqueda} es de ${precio}")
else:
    print(f"{busqueda.capitalize()} no figura en el listado de precios.")

#El precio de la Naranja es de $106.28