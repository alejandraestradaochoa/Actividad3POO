class Rectangulo:
    def __init__(self, esquina1, esquina2):
    
        self.esquina1 = esquina1
        self.esquina2 = esquina2

    def calcular_perimetro(self):
        lado1 = abs(self.esquina1[0] - self.esquina2[0])
        lado2 = abs(self.esquina1[1] - self.esquina2[1])
        return 2 * (lado1 + lado2)
    
    def calcular_area(self):
        lado1 = abs(self.esquina1[0] - self.esquina2[0])
        lado2 = abs(self.esquina1[1] - self.esquina2[1])
        return lado1 * lado2
    
    def es_cuadrado(self):
        lado1 = abs(self.esquina1[0] - self.esquina2[0])
        lado2 = abs(self.esquina1[1] - self.esquina2[1])
        return lado1 == lado2
    
#ejemplo de uso
esquina_superior_izquierda = (1, 4)
esquina_inferior_derecha = (4, 1)

rectangulo1 = Rectangulo(esquina_superior_izquierda, esquina_inferior_derecha)
print("Perímetro del rectangulo:", rectangulo1.calcular_perimetro())
print("Área del rectangulo:", rectangulo1.calcular_area())
print("El rectangulo es cuadrado?", rectangulo1.es_cuadrado())
        
    