import numpy as np

def medir_temp(n):
    # Ejercicio 5.8
    temperaturas = np.random.normal(37.5,.2, n)
    np.save('../Data/temperaturas', temperaturas)
    
    return temperaturas


def resumen_temp(n):
    mediciones = medir_temp(n)
    minima = min(mediciones)
    maxima = max(mediciones)
    promedio = sum(m for m in mediciones)/n
    mediana = 0.0

    mediciones.sort()
    l = len(mediciones)
    if l % 2 == 0:
        mediana = (mediciones[(l//2)-1] + mediciones[(l//2)]) / 2
    else:
        mediana = mediciones[(l//2)-1]    

    return maxima, minima, promedio, mediana


def main():
    print(resumen_temp(999))    


if __name__ == '__main__':
    main()