# 4 .6 Propagacion


lista = [ 0, 1, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 1, 1, -1, 0]


def propaga(lista):
    
    propagan= []
    for p,v in enumerate(lista):
        if v == -1:
            v = p
            propagan.insert(1, p)
            
    return propagan

carbon = propaga(lista)

carbon.sort()



# hasta aca lo que se busca es identificar los "carbonizados",
#  de esta manera el objetivo es pasar a 1 los 0 de la lista,
#  sabiendo que solo y exclusivamente hay 0 antes de el primr -1, no van a sufir cambios. mismo analisis para el ultimo -1 de la lista. 



#quiero correr por la lista desde el primer elemento identificado hasta el ultimo

carbon.sort()

print(carbon)

z = len(carbon)

tupla = (carbon[0],carbon[z-1])
print(tupla)

# sin lograrlo, se intnto recorer la lista y modificar los 0 
def propagar(lista):
    e = 1
    propaga = []
    for a in range(lista[tupla[0]],lista[tupla[1]+1]):
        if a == 0:
            a = e
            propaga.insert(1, a)
    return propaga

original = propagar(lista)

print(original)



"""

a=["s","f","g","s","f","g","s","f","g"]


m=[i for i,x in enumerate(a) if x=='s']

print(m)


arr = [12, 23, 21, 66, 38, 49, 11, 38, 54]

n = [p  for p, v in enumerate(arr) if v == 38]

print(n)




def propaga2(lista):
    
    propagan= []
    for p,v in enumerate(lista):
        if v == 1:
            v = p
            propagan.insert(1, p)
            
    return propagan

encen = propaga2(lista)
print(encen)



def propaga(lista):
    
    propagan= []
    for p,v in enumerate(lista):
        if v == -1:
            v = p
            propagan.insert(1, p)
            
    return propagan

carbon = propaga(lista)
print(carbon)


p3 = carbon + encen

p3.sort()

print(p3)

if encen[0] < carbon[0]:
    n_original = []
    z=encen[0]
    i = 1
    while i < z:
        original[i]=1
        n_original = [original[i]]
    
    print(n_original)




"""