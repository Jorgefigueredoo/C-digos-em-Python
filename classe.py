class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 10
        print(f"{self.modelo} acelerou para {self.velocidade} km/h")

    def frear(self):
        self.velocidade = max(0, self.velocidade - 10)
        print(f"{self.modelo} desacelerou para {self.velocidade} km/h")

meu_carro = Carro("Toyota", "Corolla", 2020)

meu_carro.acelerar()
meu_carro.acelerar()
meu_carro.frear()
