def linha():
    print("-" * 75)


class Produto:
    def __init__(self, nome, vlr_compra=0.00, vlr_venda=0.00, qtd_estoque=0, qtd_minima=0):
        self.nome = nome
        self.vlr_compra = vlr_compra
        self.vlr_venda = vlr_venda
        self.qtd_estoque = qtd_estoque
        self.qtd_minima = qtd_minima

    def get_nome(self):
        return self.nome

    def get_qtd_minima(self):
        return self.qtd_minima

    def get_qtd_estoque(self):
        return self.qtd_estoque

    def set_nome(self, novo_nome):
        while len(novo_nome) <= 0:
            print("Tamanho nome inválido")
            novo_nome = input("Insira um nome válido: ")
            linha()
        print("Nome alterado!")
        self.nome = novo_nome

    def set_qtd_minima(self, nova_qtd_minima):
        print("Qtd minima alterada!")
        self.qtd_minima = nova_qtd_minima

    def set_qtd_estoque(self, nova_qtd_estoque):
        while nova_qtd_estoque < 0:
            print("Valor inválido!")
            nova_qtd_estoque = int(input("Insira um valor válido: "))
            linha()
        print("Qtd estoque alterado!")
        self.qtd_estoque = nova_qtd_estoque

    def set_vlr_compra(self, novo_vlr_compra):
        if novo_vlr_compra > 15:
            print("Valor não aceito pela loja!")
        else:
            print("Valor compra alterado!")
            self.vlr_compra = novo_vlr_compra

    def __str__(self):
        return f"Nome: {self.nome}\nValor compra: {self.vlr_compra}\nValor venda: {self.vlr_venda}\n" \
               f"Qtd estoque: {self.qtd_estoque}\nQtd minima: {self.qtd_minima}"

    def lucro(self):
        conta = self.vlr_venda - self.vlr_compra
        return conta

    def atualiza_estoque(self, qtd_vendas):
        self.qtd_estoque = self.qtd_estoque - qtd_vendas
        print("Estoque atualizado!")

    def repor_produto(self, qtd_compras):
        self.qtd_estoque = self.qtd_estoque + qtd_compras
        print("Estoque atualizado!")

    def alerta_estoque(self):
        if self.qtd_estoque < self.qtd_minima:
            return True
        else:
            return False

    def maior_qtd(self, obj):
        if self.qtd_estoque > obj.qtd_estoque:
            print(f"Maior qantidade de estoque {self.qtd_estoque}")
            print(f"Menor quantidade de estoque {obj.qtd_estoque}")
        elif obj.qtd_estoque > self.qtd_estoque:
            print(f"Maior quantidade de estoque {obj.qtd_estoque}")
            print(f"Menor quantidade de estoque {self.qtd_estoque}")
        else:
            print(f"Os estoques são iguais {self.qtd_estoque}")

    def maior_lucro(self, obj):
        if self.lucro() > obj.lucro():
            print(f"Maior qantidade de lucro {self.lucro()}")
            print(f"Menor quantidade de lucro {obj.lucro()}")
        elif obj.lucro() > self.lucro():
            print(f"Maior quantidade de lucro {obj.lucro()}")
            print(f"Menor quantidade de lucro {self.lucro()}")
        else:
            print(f"Os lucro são iguais {self.lucro()}")

    def retorna_qtd(self):
        return len(lista_produtos)


if __name__ == '__main__':
    lista_produtos = []
    prod_1 = Produto("Arroz", 19.00, 27.50, 67, 20)
    prod_1.set_qtd_minima(15)
    prod_1.set_vlr_compra(13)
    linha()
    print(f"Produto 1\n{prod_1}")
    linha()
    print(f"Lucro produto 1: {prod_1.lucro()}")
    linha()
    prod_1.atualiza_estoque(30)
    linha()
    prod_1.repor_produto(5)
    linha()
    print(prod_1.alerta_estoque())
    prod_2 = Produto("Batata")
    prod_3 = Produto("Feijão", 200.50)
    prod_4 = Produto("Carne", qtd_estoque=20)
    linha()
    prod_1.maior_qtd(prod_4)
    linha()
    prod_1.maior_lucro(prod_2)
    linha()
    lista_produtos.append(prod_1)
    lista_produtos.append(prod_2)
    lista_produtos.append(prod_3)
    lista_produtos.append(prod_4)
    print(f"Quantidade de objetos criado: {len(lista_produtos)}")
    linha()
    print(f"Quantidade de objetos criados: {prod_1.retorna_qtd()}")
