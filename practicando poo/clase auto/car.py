class Car:

    nro_autos = 0
    valor_nafta = 250

    def __init__(self, marca, modelo, km):
        self.marca = marca
        self.modelo = modelo
        self.km = km
        self.vida = 100

        Car.nro_autos += 1

    def conducir(self):
        print('Conduciendo...')

    def __str__(self):
        return f'Autito: {self.marca}, {self.modelo}, {self.km}'

    def get_vida(self):
        return self.vida

    def chocar(self):
        self.vida -= 10

    def chocar_a_otro(self, other_car):
        other_car.vida -= 15

    @classmethod
    def modif_valor_nafta(cls, valor):
        cls.valor_nafta = valor
