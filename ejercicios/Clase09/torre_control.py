class TorreDeControl:
    
    def __init__(self):        
        self.aviones_a = []
        self.aviones_d = []
        
    
    def nuevo_arribo(self, vuelo):
        self.aviones_a.append(vuelo)
        
    
    def nueva_partida(self, vuelo):
        self.aviones_d.append(vuelo)
        
        
    def hay_aviones(self, aviones):
        return len(aviones) != 0 
    

    def asignar_pista(self):
        if self.hay_aviones(self.aviones_a):
            avion = self.aviones_a.pop(0)
            msg = f'El vuelo {avion} aterrizó con éxito'            
        elif self.hay_aviones(self.aviones_d):
            avion = self.aviones_d.pop(0)
            msg = f'El vuelo {avion} partió con éxito'
        else:
            msg = 'No hay vuelos en espera.'
            
        print(msg)
        
    
    def ver_estado(self):
        if self.hay_aviones(self.aviones_a):
            print('Vuelos esperando para aterrizar: '+ ', '.join(self.aviones_a))
        else:
            print('No hay vuelos esperando para aterrizar')
            
        if self.hay_aviones(self.aviones_d):
            print('Vuelos esperando para despegar: '+ ', '.join(self.aviones_d))
        else:
            print('No hay vuelos esperando para despegar')
            

if __name__ == '__main__':
    torre = TorreDeControl()
    torre.nuevo_arribo('AR156')
    torre.nueva_partida('KLM1267')
    torre.nuevo_arribo('AR32')
    torre.ver_estado()    
    torre.asignar_pista()
    torre.asignar_pista()    
    torre.asignar_pista()    
    torre.asignar_pista()
    
        