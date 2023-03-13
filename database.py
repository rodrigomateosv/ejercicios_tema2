import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def _str_(self):
        return "({0},{1})".format(self.x, self.y)
    
    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return 1
        elif self.x < 0 and self.y > 0:
            return 2
        elif self.x < 0 and self.y < 0:
            return 3
        elif self.x > 0 and self.y < 0:
            return 4
        else:
            return 0
        
    def vector(self, p):
        print("El vector entre {} y {} es ({} , {})").format(self,p,p.x-self.x,p.y-self.y)
              
    def distancia(self, p):
       d= math.sqrt( (p.x-self.x)**2 + (p.y-self.y )**2)
       print("La distancia entre {} y {} es {}").format(self,p,d) 

        