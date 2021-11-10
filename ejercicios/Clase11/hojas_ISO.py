#%%
def medidas_hoja_A(N):
    
    def calcular_medida(N, A = 0, ancho = 841, largo = 1189):        
        if N == A:
            return ancho, largo
        else:
            A += 1
            if A % 2 == 0:
                ancho = ancho // 2            
            else:
                largo = largo // 2
            ancho, largo = calcular_medida(N, A, ancho, largo)
        return ancho, largo
    
    ancho, largo = calcular_medida(N)
    
    if N % 2 == 0:
        return ancho, largo
    else:
        return largo, ancho
    
#%%
def medidas_hoja_A(N):
    if N == 0:
        return 841, 1189
    
        
    ancho_ant, largo_ant = medidas_hoja_A(N-1)
    
    ancho = largo_ant // 2
    largo = ancho_ant
    
    return ancho, largo

#%%
def main():
    hojas = 10
    print(f"MEDIDAS DESDE A0 HASTA A{hojas}")    
    print("--------------------------")
    for N in range(hojas+1):
        ancho, largo = medidas_hoja_A(N)
        medida = f"{ancho}x{largo}mm"        
        print(f"{f'A{N}:':<5s}{medida}")


if __name__ == '__main__':
    main()