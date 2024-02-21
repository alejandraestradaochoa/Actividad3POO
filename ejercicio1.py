class Vehiculo:
    def __init__(self, velocidad_maxima, kilometraje):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje

#ejemplo de uso 
mi_carro = Vehiculo(200, 150000)
print("velocidad_maxima :", mi_carro.velocidad_maxima)
print("kilometraje:", mi_carro.kilometraje)
