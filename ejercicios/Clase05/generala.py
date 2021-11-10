import random
from collections import Counter


def tirar(n = 5):
    return [random.randint(1, 6) for i in range(n)]


def es_generala(tirada):
    return tirada.count(tirada[0]) == 5
    


def prob_generala(N, servida = False):
    if servida:        
        return sum([es_generala(tirar()) for j in range(3) for i in range(N)]) / N
    else :
        G = 0

        for j in range(N):
            cantidad = 5
            dados = []
            for i in range(3):
                tirada = tirar(cantidad)
                tirada += dados
                dados = []

                if (es_generala(tirada)):
                    G += 1
                    break;
                #obtengo el dado que más se repite para no tirarlo nuevamente
                (dado, cantidad) = Counter(tirada).most_common(1)[0]
                
                # Actualizo la cantidad de dados que tiro en la proxima jugada y me guardo los dados repetidos
                dados = [dado] * cantidad
                cantidad = 5 - cantidad
        
        return G/N



def main():
    tiradas = 100000
    G = prob_generala(tiradas)
    H = prob_generala(tiradas, True)
    
    probabilidad = G*100
    print(f'La probabilidad de que en {tiradas} juegos obtengamos generala es del {probabilidad:.2f}%')
    
    probabilidad = H*100
    print(f'La probabilidad de que en {tiradas} juegos obtengamos generala servida es del {probabilidad:.2f}%')


if __name__ == '__main__':
    main()