class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        

    def __str__(self):
        return f'({self.x}, {self.y})'

    
    def __repr__(self):
        return f'Punto({self.x}, {self.y})'
    
    
    def __add__(self, b):
      return Punto(self.x + b.x, self.y + b.y)