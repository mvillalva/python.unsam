import math
import numpy as np
import matplotlib.pyplot as plt

def cm2inch(value):
    return value/2.54


def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()


def distancia_caminata(caminatas, mas_alejada = True):
    '''Obtiene la posición de la caminata que más se aleja del origen
       o que menos se aleja según el parámetro mas_alejada.       
       
    Pre: Recibe una lista de caminatas y qué posición deberá devolver.
    Pos: Devuelve la posición de la caminata según el parametro mas_alejada.

    '''
    distancia = math.fabs(sum(caminatas[0]))
    pos = 0
    for i, caminata in enumerate(caminatas):
        distancia_total = math.fabs(sum(caminata))
        if mas_alejada and distancia_total > distancia:
            distancia = distancia_total
            pos = i
        elif not mas_alejada and distancia_total < distancia:
            distancia = distancia_total
            pos = i
            
    return pos

def f_principal():
    N = 100000
    caminatas = []
    
    lim_sup = 500
    lim_inf = -500
    
    fig = plt.figure(figsize=(cm2inch(30), cm2inch(15)))
    plt.subplot(2, 1, 1) 
    
    for i in range(12):
        caminatas.append(randomwalk(N))
        plt.plot(caminatas[i])
        
    plt.xticks([])
    plt.title("12 caminatas al azar")
    plt.xlabel("tiempo")
    plt.ylabel("distancia al origen")
    plt.ylim(lim_inf,lim_sup)
    
    mas_alejada = distancia_caminata(caminatas)
    if mas_alejada >= 0:
        plt.subplot(2, 2, 3) 
        plt.plot(caminatas[mas_alejada])
        plt.xticks([])
        plt.title("La caminata que más se aleja")
        plt.xlabel("tiempo")
        plt.ylabel("distancia al origen")
        plt.ylim(lim_inf,lim_sup)
    
    menos_alejada = distancia_caminata(caminatas, False)
    if menos_alejada >= 0:
        plt.subplot(2, 2, 4) 
        plt.plot(caminatas[menos_alejada])
        plt.xticks([]), plt.yticks([])
        plt.title("La caminata que menos se aleja")
        plt.xlabel("tiempo")
        plt.ylabel("distancia al origen")
        plt.ylim(lim_inf,lim_sup)
    
    plt.show()
    
if __name__ == '__main__':
    f_principal()