def geringoso(palabra):    
    capadepenapa = ''
    vocales = 'aeiou'
    conAcento = 'áéíóú'
    cerradas = 'iu'
    cerradasAcento = 'íú'
    abiertas = 'aeo'
    
    for i,c in enumerate(palabra):                    
        p = 'p'
        if c.isupper():
            p = 'P'
        capadepenapa += c
        cl = c.lower()
        if cl in vocales:            
            # i < len(palabra)-1 esto lo hago para que no entre a esta opción...
            # en la última letra
            if i < len(palabra)-1:
                if cl in cerradas and (palabra[i+1].lower() in vocales or palabra[i+1].lower() in conAcento):
                    # Verifico si hay diptongo: 
                    # si la letra es 'i' o 'u' y la siguiente es vocal...
                    # entonces hay diptongo, por lo tanto no tengo que convertir esta vocal.
                    pass
                elif cl in abiertas and (palabra[i+1].lower() in cerradas or palabra[i+1].lower() in cerradasAcento):
                    # Verifico si hay diptongo: 
                    # si la letra es 'a', 'e' u 'o' y la siguiente es 'i' o 'u'...
                    # entonces hay diptongo, por lo tanto no tengo que convertir esta vocal.
                    pass
                else:
                    capadepenapa += p + c
            else:
                capadepenapa += p + c
        elif cl in conAcento:
            # Si la vocal está acentuada...
            # su traducción tiene que tener el acento sólo en la pimera vocal
            indice = conAcento.index(cl)
            vocal = vocales[indice]             
            if c.isupper():
                vocal = vocal.upper()
            capadepenapa += p + vocal        
        
    return capadepenapa


def diccionario(palabras):
    dic = {}
    for palabra in palabras:
        dic[palabra] = geringoso(palabra)
    
    return dic
    

#### Programa Principal ####
print(diccionario(['banana','manzana','naranja']))
#{'banana': 'bapanapanapa', 'manzana': 'mapanzapanapa', 'naranja': 'naparapanjapa'}