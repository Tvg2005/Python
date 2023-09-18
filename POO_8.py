def linha():
    print("-" * 75)


class Monitor:
    def __init__(self, marca, preco, hz=60):
        self.marca = marca
        self.preco = preco
        self.hz = hz

    def get_hz(self):
        return self.hz

    def get_marca(self):
        return self.marca

    def get_preco(self):
        return self.preco

    def set_hz(self, novo_hz):
        if novo_hz <= 60:
            print("Valor invalido para HZ para o monitor!")
            self.hz = int(input("Insira um valor valido: "))
            print("Valor de hz alterado!")
        else:
            print("Valor de hz alterado!")
            self.hz = novo_hz

    def set_marca(self, nova_marca):
        print("Marca alterada!")
        self.marca = nova_marca

    def set_preco(self, novo_preco):
        print("Valor de preço alterado!")
        self.preco = novo_preco

    def retorna_custo_beneficio(self):
        conta = self.hz / self.preco
        print(f"O monitor tem relação de HZ/Preço de {conta}. Ou seja a cada real gasto o comprador adquire {conta} HZ")

    def qtd_produtos(self):
        return len(lista)

    def compara_hz(self, obj):
        print("/////Comparar quantidade hz/////")
        if self.hz > obj.hz:
            print(f"Monitor com mais hz: {self.hz}\nMonitor com menos hz: {obj.hz}")
        elif obj.hz > self.hz:
            print(f"Monitor com mais hz: {obj.hz}\nMonitor com menos hz: {self.hz}")
        else:
            print(f"Monitor com mesma quantidade de hz {self.hz}")

    def __str__(self):
        return f"Marca: {self.get_marca()}\nHZ: {self.get_hz()}\nPreço: {self.get_preco()}"


if __name__ == '__main__':
    lista = []
    chama_funcao = Monitor("", 0, 0)
    produto1 = Monitor("Samsung", 500, 75)
    produto2 = Monitor("Red dragon", 1000)
    produto3 = Monitor("Lenovo", 0)  # Se passar os 2 em branco, vai dar erro, tendo em vista que apenas hz tem default
    lista.append(produto1)
    lista.append(produto2)
    lista.append(produto3)
    print(f"Produto 1:\n{produto1}")
    linha()
    print(f"Produto 2:\n{produto2}")
    linha()
    print(f"Produto 3:\n{produto3}")
    linha()
    produto3.set_hz(60)
    linha()
    produto3.set_preco(300)
    linha()
    produto2.set_marca("LG")
    linha()
    print(f"Produto 2\n{produto2.get_marca()}\n{produto2.get_hz()}\n{produto2.get_preco()}")
    linha()
    print(f"Quantidade de produtos inseridos {chama_funcao.qtd_produtos()}")
    linha()
    produto1.compara_hz(produto2)
    linha()
    produto3.retorna_custo_beneficio()
    linha()
