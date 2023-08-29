lista = []
def linha():
    print("-" * 75)


def mostra_dados(self):
    global ct
    linha()
    ct += 1
    print(f"Carro {ct}:")
    print(f"Modelo: {self.modelo}")
    print(f"Ano: {self.ano}")
    print(f"Valor: {self.valor}")


def set_qtd():
    lista.append(carro1)
    lista.append(carro2)
    lista.append(carro3)
    lista.append(carro4)
    lista.append(carro5)


class Veiculo:
    def __init__(self, modelo, ano, valor):
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def get_ano(self):
        return self.get_ano()

    def get_valor(self):
        return self.get_valor()

    def get_modelo(self):
        return self.get_modelo()

    def set_ano(self, novo_ano):
        self.ano = novo_ano

    def set_valor(self, novo_valor):
        if novo_valor <= 0:
            self.valor = float(input("Insira um valor válido: "))
        else:
            self.valor = novo_valor

    def set_modelo(self, novo_modelo):
        self.modelo = novo_modelo

    def aumenta_valor(self):
        aumento = int(input("Insira um valor para aumentar no carro: "))
        self.valor = aumento + self.valor
        print(f"Valor novo: {self.valor}")

    def get_qtd(self):
        return len(lista)


if __name__ == '__main__':
    carro1 = Veiculo("Audi A4", 2017, 100000)
    carro2 = Veiculo("Lamborghini Huracan", 2022, 2000000)

    valor_carro = int(input("Insira um novo valor para o carro 1: "))
    carro1.set_valor(valor_carro)
    ct = 0
    mostra_dados(carro1)
    mostra_dados(carro2)
    linha()
    escolha_carro = int(input("Insira o carro que deseja aumentar o valor [1][2]: "))
    linha()
    if escolha_carro == 1:
        carro1.aumenta_valor()
    elif escolha_carro == 2:
        carro2.aumenta_valor()
    else:
        print("Carro inválido!")
    linha()
    modelo_carro_novo = input("Insira o modelo do carro novo: ")
    linha()
    ano_carro_novo = int(input("Insira o ano do carro novo: "))
    carro3 = Veiculo(modelo_carro_novo, ano_carro_novo, 0)
    mostra_dados(carro3)

    carro4 = Veiculo("Siena", 0, 0)
    mostra_dados(carro4)
    carro5 = Veiculo("McLaren", 0, 60000000)
    mostra_dados(carro5)
    linha()
    set_qtd()
    print(f"Quantidade carros: {carro1.get_qtd()}")
