import math

class Punto :
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostrar(self):
        print(f"({self.x}, {self.y})")

    def mover(self, nuevo_x, nuevo_y):
        self.x = nuevo_x
        self.y = nuevo_y

    def calcular_distancia(self, otro_punto):
        distancia = math.sqrt((self.x - otro_punto.x)**2 + (self.y - otro_punto.y)**2)
        return distancia
    
#ejemplo de uso
punto1 = Punto (3, 4)
punto1.mostrar()

punto2 = Punto (2, 5)
punto2.mostrar()

punto1.mover(5, 6)
punto1.mostrar()

distancia = punto1.calcular_distancia(punto2)
print("distancia entre punto1 y punto2 es:", distancia)
        