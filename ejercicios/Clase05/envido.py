# Ejercicio 5.4: Envido
# Teniendo en cuenta las reglas del Truco, estimá la probabilidad de obtener 
# 31, 32 o 33 puntos de envido en una mano. ¿Son iguales estas tres probabilidades? ¿Por qué?
import random
from collections import Counter
from tqdm import tqdm


def calcular_envido(mano, numero):
    #cacula solo el envido de dos o tres cartas del mismo palo
    
    # si la carta es mayor a 7 cambio el valor a 10
    # si no, le sumo 10 al valor, para luego calcular el envido
    cartas = [[10 if m[0] > 7 else m[0]+10, m[1]] for m in mano]
    
    # Guardo los valores de las cartas para elegir los dos mas altos de un mismo palo en caso de que tenga flor
    valores = [10 if m[0] > 7 else m[0]+10 for m in mano]
    
    # Lo uso para saber cuantas cartas de un mismo palo hay
    c = Counter(m[1] for m in cartas)    
    
    # Sumo los ennvidos 
    # Si tengo 2 cartas iguales sumo su valor 
    # Si son 3 iguales (flor) sumo los dos mas altos
    envido = sum(m[0] if c[m[1]] == 2 else m[0] if c[m[1]] == 3 and m[0] != min(valores) else 0 for m in cartas)
    
    return envido == numero    


def main():
    valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    palos = ['oro', 'copa', 'espada', 'basto']
    naipes = [[valor,palo] for valor in valores for palo in palos]
    casos = 10000

    casos31 = sum(calcular_envido(random.sample(naipes, 3), 31) for i in tqdm(range(casos)))
    casos32 = sum(calcular_envido(random.sample(naipes, 3), 32) for i in tqdm(range(casos)))
    casos33 = sum(calcular_envido(random.sample(naipes, 3), 33) for i in tqdm(range(casos)))

    print()
    print(f"La probabilidad de sacar 31 puntos de envido en 1 mano es del {casos31/casos*100:.2f}%")
    print(f"La probabilidad de sacar 32 puntos de envido en 1 mano es del {casos32/casos*100:.2f}%")
    print(f"La probabilidad de sacar 33 puntos de envido en 1 mano es del {casos33/casos*100:.2f}%")
    print()
    print("Cuanto mayor sea el puntaje a obtener, hay menos combinaciones de n�meros para obtener ese envido.\nPor lo tanto, la probabilidad disminuye.")
    print()


if __name__ == '__main__':
    main()

