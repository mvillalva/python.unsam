def pascal(n, k):
    if k == 0 or n == k:
        return 1        
    else:
        return pascal(n-1, k-1) + pascal(n-1, k)


if __name__ == '__main__':
    n = 1
    k = 2
    try:
        print(f'El valor de la {k}º posición del nivel {n} en un Triángulo de Pacal es: {pascal(n, k)}')
    except:
        print('Te excediste!!')