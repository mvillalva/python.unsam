# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 11:45:47 2021

@author: JuliManu
"""
#propagar.py
def propagar(lista):   

    for i,e in enumerate(lista):
        if e == 1:
            if i==0 and lista[1]==0:
                lista[1]=1    
            elif i==len(lista) and lista[-2]==0:
                lista[-2]=1                
            elif i>0 and lista[i-1]==0 and lista[+1]==0:
                lista[i-1]=1
                lista[i+1]=1                
            elif i>0 and lista[i-1]==0:
                lista[i-1]=1                
            elif i>0 and i<len(lista)-1 and lista[i+1]==0:
                lista[i+1]=1
                
    return lista


def main():
    lista = [ 0, 1, 0,-1, 1, -1, 0, 0,-1, 0, 1, 0, 0]
    print(lista)

    print(propagar(lista))


if __name__ == '__main__':
    main()


            