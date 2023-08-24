def linha():
    print("-" * 75)


class Carro:
    def __init__(self, marca, ano, modelo):
        self.marca = marca
        self. ano = ano
        self.modelo = modelo

    def get_marca(self):
        return self.marca

    def get_ano(self):
        return self.ano

    def get_modelo(self):
        return self.modelo

    def set_marca(self, nova_marca):
        self.marca = nova_marca

    def set_ano(self, novo_ano):
        self.ano = novo_ano

    def set_modelo(self, novo_modelo):
        self.modelo = novo_modelo


if __name__ == '__main__':
    carro1 = Carro("Gol", 2010, "Sedan")
    carro2 = Carro("Fiat", 2020, "SUV")
    carro3 = Carro("Tesla", 2022, "Sedan")
    print(f"Carro1:\nMarca: {carro1.get_marca()}\nAno: {carro1.get_ano()}\nModelo: {carro1.get_modelo()}")
    linha()
    print(f"Carro2:\nMarca: {carro2.get_marca()}\nAno: {carro2.get_ano()}\nModelo: {carro2.get_modelo()}")
    linha()
    print(f"Carro3:\nMarca: {carro3.get_marca()}\nAno: {carro3.get_ano()}\nModelo: {carro3.get_modelo()}")
    linha()
    carro1.set_marca("Lamborghini")
    carro1.set_ano(2015)
    carro1.set_modelo("SUV")
    print("Carro 1 modificado!")
    linha()
    print(f"Carro1:\nMarca: {carro1.get_marca()}\nAno: {carro1.get_ano()}\nModelo: {carro1.get_modelo()}")