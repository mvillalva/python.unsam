# Ejercicio 4.5
def invertir_lista(lista):
    invertida = []
    for e in lista: # Recorro la lista        
        invertida = [e] + invertida #agrego el elemento al principio de la lista invertida

    return invertida


def invertir_lista_v2(lista): #sin usar insert
    indice = len(lista)

    invertida = [None] * indice
    for e in lista: # Recorro la lista
        indice -= 1
        invertida[indice]= e

    return invertida


def main():
    lista = [1, 2, 3, 4, 5]
    lista2 = ['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']
    print(f'La lista {lista} invertida quedó así: {invertir_lista(lista)}')
    print(f'La lista {lista2} invertida quedó así: {invertir_lista(lista2)}')


if __name__ == '__main__':
    main()