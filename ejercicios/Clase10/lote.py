class Lote:
    
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio
        
    
    def __repr__(self):
        return f"Lote('{self.nombre}', {self.cajones}, {self.precio})"
        
    
    def costo(self):
        return self.precio * self.cajones
    
    
    def vender(self, cantidad):
        self.cajones -= cantidad

        
        
class MiLote(Lote):
    
    def __init__(self, nombre, cajones, precio, factor):
        super().__init__(nombre, cajones, precio)
        self.factor = factor
    
    def rematar(self):
        self.vender(self.cajones)
        
    def costo(self):
        costo_orig = super().costo()
        return self.factor * costo_orig
    