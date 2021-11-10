import random


def generar_punto():
    x = random.random()
    y = random.random()
    return x,y


def main():
    # M = puntos dentro del ciculo
    # N = cantidad de puntos a generar

    N = 100000
    M = sum(1 for v in [generar_punto() for i in range(N)] if v[0]**2 + v[1]**2 < 1)

    print(f'pi = {4*M/N}')
    

if __name__ == '__main__':
    main()