class Vehiculo:

    def __init__(self, color, tipo, cilindrada):
        self.color = color
        self.tipo = tipo
        self.cilindrada = cilindrada

    def acelerar(self):
        print("Vehiculo", self.tipo, "acelerando")

    def frenar(self):
        print("Vehiculo", self.tipo, "frenando")

    def doblar(self):
        print("Vehiculo", self.tipo, "doblando")
