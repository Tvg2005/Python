def linha():
    print("-" * 75)


class Veiculo:
    def __init__(self, valor, modelo, quilometragem):
        self.valor = valor
        self.modelo = modelo
        self.quilometragem = quilometragem

    def get_valor(self):
        return self.valor

    def get_modelo(self):
        return self.modelo

    def get_quilometragem(self):
        return self.quilometragem

    def set_valor(self, novo_valor):
        self.valor = novo_valor

    def set_modelo(self, novo_modelo):
        self.modelo = novo_modelo

    def set_quilometragem(self, nova_quilometragem):
        self.quilometragem = nova_quilometragem

    def aumenta_valor(self, aumento):
        if aumento <= 0:
            print("Valor inválido")
            aumento = int(input("Insira outro valor: "))
            print("Valor aumentado!")
            self.valor = self.valor + aumento
        else:
            print("Valor aumentado!")
            self.valor = self.valor + aumento

    def aumenta_valor_pct(self, valor_pct):
        self.valor = self.valor + (self.valor * valor_pct / 100)


class Carro(Veiculo):
    def __init__(self, valor, modelo, quilometragem=1, qtd_portas=4):
        super().__init__(valor, modelo, quilometragem)
        self.qtd_portas = qtd_portas

    def __str__(self):
        return f"Modelo:{self.modelo}\nValor:{self.valor}\nKm:{self.quilometragem}\nPortas:{self.qtd_portas}"


class Moto(Veiculo):
    def __init__(self, valor, modelo, quilometragem, cilindradas=0):
        super().__init__(valor, modelo, quilometragem)
        self.cilindradas = cilindradas


if __name__ == '__main__':
    carro1 = Carro(10000, "Hyundai", 0, 4)
    carro2 = Carro(100000, "Ford", 100)
    carro3 = Carro(99, "Honda")
    linha()
    print(carro1)
    linha()
    moto1 = Moto(100000, "BMW", 50000, 600)
    moto2 = Moto(5000, "Yamaha", 0)
    print(vars(moto1))
    linha()
    print(moto2.__dict__)
    carro1.aumenta_valor(9999)
    linha()
    print(carro1)
    linha()
    carro2.aumenta_valor_pct(100)
    print(carro2)
    linha()
    carro3.aumenta_valor(0)
