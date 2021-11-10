class Camion:    
    def __init__(self, lotes):
        self.lotes = lotes


    def __iter__(self):
        return self.lotes.__iter__()
    
    
    def __contains__(self, nombre):
        return any(lote.nombre == nombre for lote in self.lotes)
    
    
    def __len__(self):
        return len(self.lotes)
    
    
    def __getitem__(self, key):
        return self.lotes[key]
    
    
    def __str__(self):
        s = f'Camión con {len(self.lotes)} lotes: \n'
        for lote in self.lotes:            
            s += f"Lote de {lote.cajones} cajones de '{lote.nombre}', pagados a ${lote.precio} cada uno.\n"
        return s
    
    
    def __repr__(self):
        return f'Camion({self.lotes})'


    def precio_total(self):
        return sum(l.costo() for l in self.lotes)


    def contar_cajones(self):
        from collections import Counter
        cantidad_total = Counter()
        for l in self.lotes:
            cantidad_total[l.nombre] += l.cajones
        return cantidad_total
    
    
if __name__ == '__main__':
    from informe_final import leer_camion
    camion = leer_camion('../Data/camion.csv')
    if 'Naranja' in camion:
        print('A la naranja barata !!')