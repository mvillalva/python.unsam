# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 19:14:37 2021

@author: nahue
"""

def propagar(lista):
    propagada=[]    #lista propagada
    encendido=0     #variable que indica si el último fósforo está encendido
    apagados=[]     #Lista de los últimos fósforos apagados al recorrer la lista
    for e in lista:      #recorro la lista
        if e==0:                            #Si el fósforo esta apagado y...
            if encendido:                   # ...el anterior encendido...
                propagada.append(1)         #...agrego fósforo encendido.
            else:
                apagados.append(0) #si el fósforo apagado y el anterior no está encendido agregos este fósforo a la lista apagados
        elif e==1:                            #Si el fósforo está encendido...
            propagada+=[1 for el in apagados]    #...enciendo la lista "apagados" y la agrego a la lista "propagada"
            apagados=[]                          #vacío la lista de apagados
            encendido=1     #indico que el fósforo está encendido.
            propagada.append(1)              #Agrego el fósforo encendido.
        elif e==-1:                          #Si el fósforo está quemado...   
            propagada+=apagados                #...agrego la lista "apagados" a la lista "propagada"
            apagados=[]                        #vacío la lista de apagados
            propagada.append(-1)         #Agrego el fósforo quemado.
            encendido=0    # indico que el fósforo no está encendido       
    propagada+=apagados  #si quedaron fósforos apagados los agrego
    return propagada
    
# print(propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]))
# print(propagar([ 0, 0, 0, 1, 0, 0]))
# print(propagar([]))

print(propagar([ 0, 0, 0, 1, 0, 0]))
print(propagar([ 0, 0, 0, 0, 0, -1]))
print(propagar([ 0, 0, 0, 0, 0, 1]))
print(propagar([]))
print(propagar([ 0 for _ in range(1000) ] + [1]))
print(propagar([1] + [ 0 for _ in range(1000) ]))
print(propagar([ (i% 6)//2-1 for i in range(200) ]))
print(propagar([ -1*((i% 6)//2-1) for i in range(60) ]))