class CuentaBancaria:
    def __init__ (self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, cantidad):
        if cantidad > 0:
            self.balance += cantidad
            print(f"Se depositaron {cantidad} unidades en la cuenta.")
        else:
            print("La cantidad a depositar debe ser mayor que cero.")
    
    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.balance:
            self.balance -= cantidad
            print(f"Se ha retirado {cantidad} de la cuenta.")
        else:
            print("la cantidad a retirar debe ser mayor que cero y menor o igual al balance disponible.")

#Ejemplo de uso
cuenta = CuentaBancaria("1234567890",  ["Juan", "Maria"], 1000)
print("Balance inicial:", cuenta.balance)
cuenta.retirar(500)
print("Nuevo Balance:", cuenta.balance)