class Carta:
    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

#definicion de las pintas
PINTA_CORAZON = "Corazon"
PINTA_DIAMANTE = "Diamante"
PINTA_TREBOL = "Trebol"
PINTA_PICA = "Pica"

#ejemplo de uso
carta1 = Carta("As", PINTA_CORAZON)
carta2 = Carta("10", PINTA_DIAMANTE)

print("Carta 1:", carta1.valor, "de", carta1.pinta)
print("Carta 2:", carta2.valor, "de", carta2.pinta)
