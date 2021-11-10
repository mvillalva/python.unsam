class Canguro:
    
    def __init__(self, nombre, lista = []):
        self.nombre = nombre
        self.contenido_marsupio = lista.copy()
        
    
    def __str__(self):
        lista = [self.nombre + ' tiene: ']
        l = self.contenido_marsupio.copy()
        for c in l:            
            lista.append(object.__str__(c))
        
        return '\n\t'.join(lista)
    
    
    def __repr__(self):
        return f'Canguro ({self.nombre}, {self.contenido_marsupio})'
    
    
    def meter_en_marsupio(self, contenido):
        self.contenido_marsupio.append(contenido)
        
        
class CanguroMalo:
    """Un Canguro es un marsupial."""

    def __init__(self, nombre, contenido=[]):
        """Inicializar los contenidos del marsupio.

        nombre: string
        contenido: contenido inicial del marsupio, lista.
        """
        self.nombre = nombre
        self.contenido_marsupio = contenido.copy() #agregaria copy() 

    def __str__(self):
        """devuelve una representación como cadena de este Canguro.
        """
        t = [ self.nombre + ' tiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.

        item: objecto a ser agregado
        """
        self.contenido_marsupio.append(item)


if __name__ == '__main__':
    madre_canguro = Canguro('Madre')
    cangurito = Canguro('gurito')
    madre_canguro.meter_en_marsupio('billetera')
    madre_canguro.meter_en_marsupio('llaves del auto')
    madre_canguro.meter_en_marsupio(cangurito)
    
    print(madre_canguro)