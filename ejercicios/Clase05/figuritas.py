import random
import numpy as np
import matplotlib.pyplot as plt


def imprimir_titulo(titulo):    
    print()
    print('#'*len(titulo))
    print(titulo)
    print('#'*len(titulo))
    print()


# Ejercicio 5.10
def crear_album(figus_total):
    return np.zeros(figus_total, dtype=np.int64)


# Ejercicio 5.11
def album_incompleto(A):
    return 0 in A


# Ejercicio 5.12
def comprar_figu(figus_total):
    return random.randint(0, figus_total-1)


# Ejercicio 5.13
def cuantas_figus(figus_total):    
    album = crear_album(figus_total)
    
    while album_incompleto(album):        
        album[comprar_figu(figus_total)] += 1 
    
    return album.sum()


# Ejercicio 5.15
def experimento_figus(n_repeticiones, figus_total):
    lista = [cuantas_figus(figus_total) for i in range(n_repeticiones)]
    
    return int(np.mean(lista))


#Ejercicio 5.17
def comprar_paquete(figus_total, figus_paquete, sin_repeticion = False):
    if sin_repeticion:
        figus = [i for i in range(figus_total)]
        return random.sample(figus, k=figus_paquete)
    else:
        return [comprar_figu(figus_total) for i in range(figus_paquete)]
    


#Ejercicio 5.18
def cuantos_paquetes(figus_total, figus_paquete, sin_repeticion = False):
    cantidad_paquetes = 0
    album = crear_album(figus_total)

    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete, sin_repeticion)
        cantidad_paquetes += 1
        while(paquete):
            album[paquete.pop()] = 1            

    return cantidad_paquetes


# Ejercicio 5.19
def experimento_figus_paquetes(n_repeticiones, figus_total, figus_paquete):
    lista = [cuantos_paquetes(figus_total, figus_paquete) for i in range(n_repeticiones)]
    
    return int(np.mean(lista))


# Histograma
def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]

    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)

        while paquete:
            album[paquete.pop()] = 1

        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)

    return historia_figus_pegadas    


#Ejercicio 5.14
def ejercicio514():    
    figus_total = 6
    n_repeticiones = 1000

    lista = [cuantas_figus(figus_total) for i in range(n_repeticiones)]

    imprimir_titulo('### Ejercicio 5.14 ###')    
    print(f'Para completar un album de {figus_total} figuritas hay que comprar en promedio {np.mean(lista):.0f} figuritas')


# Ejercicio 5.15
def ejercicio515():
    figus_total = 670
    n_repeticiones = 100
    promedio = experimento_figus(n_repeticiones, figus_total)

    imprimir_titulo('### Ejercicio 5.15 ###')
    print(f'Para completar un album de {figus_total} figuritas hay que comprar en promedio {promedio} figuritas')    


# Ejercicio 5.19
def ejercicio519():
    figus_total = 670
    figus_paquete = 5
    n_repeticiones = 100
    promedio = experimento_figus_paquetes(n_repeticiones, figus_total, figus_paquete)

    imprimir_titulo('### Ejercicio 5.19 ###')
    print(f'Para completar un album de {figus_total} figuritas hay que comprar en promedio {promedio} paquetes de {figus_paquete} figuritas cada uno.')


# Histograma
def histograma():
    figus_total = 670
    figus_paquete = 5
    
    plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
    plt.xlabel("Cantidad de paquetes comprados.")
    plt.ylabel("Cantidad de figuritas pegadas.")
    plt.title("La curva de llenado se desacelera al final")
    plt.show()


# Ejercicio 5.20
def ejercicio520():
    figus_total = 670
    figus_paquete = 5
    n_repeticiones = 100

    lista = [cuantos_paquetes(figus_total, figus_paquete) for i in range(n_repeticiones)]

    n_paquetes_hasta_llenar = np.array(lista)

    prob = (n_paquetes_hasta_llenar <= 850).sum() / n_repeticiones

    imprimir_titulo('### Ejercicio 5.20 ###')
    print(f'La probabilidad de llenar el ambum con 850 paquetes o menos es del {prob*100:.2f}%')


# Ejercicio 5.21
def ejercicio521():
    figus_total = 670
    figus_paquete = 5
    n_repeticiones = 100

    paquetes = np.array([cuantos_paquetes(figus_total, figus_paquete) for i in range(n_repeticiones)])

    plt.hist(paquetes, bins=50)
    plt.show()


# Ejercicio 5.22
def ejercicio522():    
    figus_total = 670
    figus_paquete = 5
    n_repeticiones = 1000

    lista = [cuantos_paquetes(figus_total, figus_paquete) for i in range(n_repeticiones)]

    n_paquetes_hasta_llenar = np.array(lista)
    n_paquetes_hasta_llenar.sort()

    p90 = int(n_repeticiones * .9)
    
    imprimir_titulo('### Ejercicio 5.22 ###')
    print(f'La cantidad aproximada de paquetes que hay que comprar para tener un 90% de probabilidad de completar el album es de {n_paquetes_hasta_llenar[p90]}')


# Ejercicio 5.23
def ejercicio523():
    figus_total = 670
    figus_paquete = 5
    n_repeticiones = 100
    lista = [cuantos_paquetes(figus_total, figus_paquete, True) for i in range(n_repeticiones)]
    n_paquetes_hasta_llenar = np.array(lista)

    prob = (n_paquetes_hasta_llenar <= 850).sum() / n_repeticiones

    imprimir_titulo('### Ejercicio 5.23 ###')
    print(f'La probabilidad de llenar un album con 850 paquetes o menos (sin figuritas repetidas) es del {prob*100:.2f}%')


# Ejercicio 5.24
def albumes_incompletos(A):
    incompleto = False
    for a in A:
        incompleto = incompleto or 0 in a

    return incompleto


def cuantos_paquetes_album(album_total, figus_total, figus_paquete):    
    cantidad_paquetes = 0

    albumes = [crear_album(figus_total) for  i in range(album_total)]

    while albumes_incompletos(albumes):    
        paquete = comprar_paquete(figus_total, figus_paquete)
        cantidad_paquetes += 1
        while(paquete):
            figu = paquete.pop()
            for album in albumes:
                if album[figu] == 0:
                    album[figu] = 1
                    break;
    
    return cantidad_paquetes


def experimento_album_figus_paquetes(n_repeticiones, album_total, figus_total, figus_paquete):
    lista = [cuantos_paquetes_album(album_total, figus_total, figus_paquete) for i in range(n_repeticiones)]
    
    return int(np.mean(lista))


def ejercicio524():
    album_total = 5
    figus_total = 670
    figus_paquete = 5
    
    cantidad_paquetes = experimento_album_figus_paquetes(100, album_total, figus_total, figus_paquete)
    
    imprimir_titulo('### Ejercicio 5.24 ###')
    print(f'Para completar {album_total} álbum/es de {figus_total} figuritas hay que comprar en promedio {cantidad_paquetes} paquetes de {figus_paquete} figuritas cada uno.')    


def main():
    opcion = ''
    while opcion.lower() != 's':
        imprimir_titulo('### Menú ###')        
        print('1. Ejercicio 5.14', end='\t')
        print('4. Ejercicio Histograma', end='\t')
        print('7. Ejercicio 5.22')
        print('2. Ejercicio 5.15', end='\t')
        print('5. Ejercicio 5.20', end='\t')
        print('8. Ejercicio 5.23')
        print('3. Ejercicio 5.19', end='\t')
        print('6. Ejercicio 5.21', end='\t')
        print('9. Ejercicio 5.24')
        print('S. Salir')        

        opcion = input(': ')

        if opcion == '1':
            ejercicio514()
        elif opcion == '2':
            ejercicio515()
        elif opcion == '3':
            ejercicio519()
        elif opcion == '4':
            histograma()
        elif opcion == '5':
            ejercicio520()
        elif opcion == '6':
            ejercicio521()
        elif opcion == '7':
            ejercicio522()
        elif opcion == '8':
            ejercicio523()
        elif opcion == '9':
            ejercicio524()

        if opcion.lower() != 's':
            x = input("ENTER para continuar...")


if __name__ == '__main__':
    main()