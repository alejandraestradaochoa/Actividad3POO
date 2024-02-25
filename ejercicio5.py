import math 

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio\
    
    def calcular_centro(self):
        return math.pi * self.radio**2
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.radio
    
    def punto_pertenece(self, punto):
        distancia_centro_punto = math.sqrt((punto[0] - self.centro[0])**2 + (punto[1] - self.centro[1])**2)
        return distancia_centro_punto <= self.radio
    
#ejemplo de uso   
circulo1 = Circulo((0, 0), 5)
print("El area del circulo es :", circulo1.calcular_area())
print("El perimetro del circulo es :", circulo1.calcular_perimetro())

punto1 = (3, 4)
print("El punto pertenece al circulo?", circulo1.punto_pertenece(punto1))

punto2 = (5, 6)
print("El punto pertenece al circulo?", circulo1.punto_pertenece(punto2))
