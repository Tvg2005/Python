def linha():
    print("-" * 75)


class Garrafa:
    def __init__(self, marca, cor="branca", tamanho=500):
        self.marca = marca
        self.cor = cor
        self.tamanho = tamanho

    def set_marca(self, nova_marca):
        print("Marca da garrafa alterada com sucesso!")
        self.marca = nova_marca

    def set_cor(self, nova_cor):
        print("Cor da garrafa alterado com sucesso!")
        self.cor = nova_cor

    def set_tamanho(self, novo_tamanho):
        while novo_tamanho <= 0:
            print("Valor inválido!")
            novo_tamanho = int(input("Insira um valor válido para o tamanho da garrafa: "))
        print("Valor do tamanho alterado com sucesso!")
        self.tamanho = novo_tamanho

    def get_marca(self):
        return self.marca

    def get_cor(self):
        return self.cor

    def get_tamanho(self):
        return self.tamanho

    def verifica_tamanho(self, obj):
        print("/////Comparar tamanho/////")
        if self.tamanho > obj.tamanho:
            print(f"Garrafa maior com {self.tamanho}ml!\nGarrafa menor com {obj.tamanho}ml!")
        elif obj.tamanho > self.tamanho:
            print(f"Garrafa maior com {obj.tamanho}ml!\nGarrafa menor com {self.tamanho}ml!")
        else:
            print(f"Garrafas de mesmo tamanho com {self.tamanho}ml!")

    def retorna_cor_hexa(self):
        if self.cor == "branco":
            print("Código hexadecimal da cor branca '#FFFFFF'")
        elif self.cor == "preto":
            print("Código hexadecimal da cor preta '#000000'")
        elif self.cor == "azul":
            print("Código hexadecimal da cor azul '#0000FF'")
        elif self.cor == "cinza":
            print("Código hexadecimal da cor cinza '#808080'")
        else:
            print("Cor de garrafa não listado!")

    def __str__(self):
        s = f"Marca: {self.marca}\nCor: {self.cor}\nTamanho: {self.tamanho}ml"
        return s


if __name__ == '__main__':
    garrafa1 = Garrafa("Powerade", "azul", 800)
    garrafa2 = Garrafa("Wolf", "preto")
    garrafa3 = Garrafa("Stanley")
    linha()
    print(f"Marca garrafa 1: {garrafa1.get_marca()}")
    print(f"Tamanho garrafa 1: {garrafa1.get_tamanho()}")
    linha()
    print(f"Cor garrafa 2: {garrafa2.get_cor()}")
    linha()
    garrafa2.set_tamanho(300)
    garrafa3.set_cor("cinza")
    garrafa3.set_marca("Crystal")
    linha()
    garrafa1.verifica_tamanho(garrafa2)
    linha()
    garrafa3.retorna_cor_hexa()
    linha()
    print(garrafa1)
    linha()
    print(garrafa2)
    linha()
    print(garrafa3)
    linha()
