def neutro(palabra):
    if len(palabra) > 1:
        if palabra[-1] == 'o':
            palabraNueva = palabra[:-1] + 'e'
        elif palabra[-2] == 'o':
            palabraNueva = palabra[:-2] + 'e' + palabra[-1]
        else:
            palabraNueva = palabra
    else:
        palabraNueva = palabra
    
    return palabraNueva

#%%
frase = '¿Y qué me contas del otro día cuando fuimos al parque o cuando volvimos?'
frase_t = ''
palabras = frase.split()

palabrasNuevas = []

for palabra in palabras:
    palabraNueva = neutro(palabra)
    palabrasNuevas.append(palabraNueva)    
        
frase_t = ' '.join(palabrasNuevas)

print(frase_t)
#'todes somes programadores'
