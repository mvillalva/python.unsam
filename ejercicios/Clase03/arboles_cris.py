
import csv
from pprint import pprint
from collections import Counter


# Ejercicio 3.18
def leer_parque (filename,parque='GENERAL PAZ'):
    data_trees = []
    # parque = parque.upper()
    # especie_parque = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for i,row in enumerate(rows):
            record = dict(zip(headers,row))
            data_trees.append(record)
    especie_parque = []
    for especie in data_trees:
        if especie["espacio_ve"] in parque:
            especie_parque.append(especie)
    # print(especie_parque) 
    return especie_parque


# Ejercicio 3.19
def especies(arbolado):
    especies = []    
    for especie in arbolado:
        especies.append(especie["nombre_com"])
    especies = set(especies)
    return especies


# Ejercicio 3.20
def leer_parque_data (filename):
    data_trees = []
    # parque = parque.upper()
    # especie_parque = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for i,row in enumerate(rows):
            record = dict(zip(headers,row))
            record = dict(espacio_ve = record['espacio_ve'],\
                          nombre_com = record['nombre_com'],\
                          altura_tot = int(record['altura_tot']),\
                          inclinacio = int(record['inclinacio']),\
                          long       = float(record['long']),\
                          lat        = float(record['lat']))
            data_trees.append(record)
    return data_trees


def contar_ejemplares(tree_list,park):
    try:
        park = [park[0].upper(),park[1].upper(),park[2].upper()]
        trees_park1 = Counter()
        trees_park2 = Counter()
        trees_park3 = Counter()
        for tree in tree_list:
            if tree['espacio_ve'] == park[0]:
                trees_park1[tree['nombre_com']] += 1
            elif tree['espacio_ve'] == park[1]:
                trees_park2[tree['nombre_com']] += 1
            elif tree['espacio_ve'] == park[2]:
                trees_park3[tree['nombre_com']] += 1
        list = trees_park1.most_common(5)
        list += trees_park2.most_common(5)
        list += trees_park3.most_common(5)
        print(f'\n\n{park[0]:28s} {park[1]:28s} {park[2]:28s}')
        print(f'{("~"*16+" "*13)*3}')
        for i in range(5):
            especie, cant = list[i]
            especie1, cant1 = list[i+5]
            especie2, cant2 = list[i+10]
            str1 = especie +': '+str(cant)
            str2 = especie1 +': '+str(cant1)
            str3 = especie2 +': '+str(cant2)
            print(f'{str1:<28s} {str2:<28s} {str3:<28s}')
        print('\n\n')
    except IndexError:
        print('Error, ha ingresado menos de 3 parques')


def main():
    filename = '../Data/arbolado-en-espacios-verdes.csv'
    tree_list = leer_parque_data(filename)
    parque   = ['GENERAL PAZ','ANDES, LOS','CENTENARIO']
    
    print('\n\n','#'*10,' ', 'Ejercicio 3.18',' ','#'*10)
    print('Lectura de los arboles de un Parque (General Paz)','\n\n')
    pprint(leer_parque(filename))

    print('\n\n','#'*10,' ', 'Ejercicio 3.19',' ','#'*10)
    print('Determinar las especies del parque anterior','\n\n')

    pprint(especies(leer_parque(filename)))

    print('\n\n','#'*10,' ', 'Ejercicio 3.20',' ','#'*10)
    print('Contar ejemplares por especie en los parques:\nGeneral Paz, Los Andes, Centenario','\n\n')

    contar_ejemplares(tree_list,parque)


if __name__ == '__main__':
    main()
    




# def contar_ejemplares(tree_list,parque):
# def contar_ejemplares(tree_list):
#     pprint(tree_list)
#     total_trees = Counter()
#     tree_l = []
#     for t in tree_list:
#         total_trees[t['nombre_com']] += 1
#     tt = total_trees.most_common(5)
#     for t in tt:
#         # tl = (t[0],t[1],parque.upper())
#         tl = (t[0],t[1])
#         tree_l.append(tl)
#     return tree_l


# def mostrar_contados(pq1,pq2,pq3):
# def mostrar_contados(pq1):
    # pq1.extend(pq2)
    # pq1.extend(pq3)
    # print(f'{pq1[0][2]:<30s} {pq1[5][2]:<30s} {pq1[10][2]:<30s}')
    # print((('~'*25)+'      ') *3)
    # for i in range(5):
    #     print(f'{str(pq1[i][0]):<20s}:{str(pq1[i][1]):<10s}{str(pq1[i+5][0]):<20s}:{str(pq1[i+5][1]):<10s}{str(pq1[i+10][0]):<20s}:{str(pq1[i+10][1]):<10s}')