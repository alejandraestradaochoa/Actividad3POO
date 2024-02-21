class Punto:
    def __init__(self, x, y) :
        self.x = x
        self.y = y

    def mostrar(self) :
        print(f"({self.x}, {self.y})")

#ejemplo de uso
punto1 = Punto(2, 3)
punto1.mostrar()   # salida: (3, 4)

punto2 = Punto(-1, 2)
punto2.mostrar()   # salida: (-1, 2)
       