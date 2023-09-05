from datetime import date


def linha():
    print("-" * 75)


def mostra_dados(self):
    print(f"Nome: {self.nome}")
    print(f"Peso: {self.peso}")
    print(f"Altura: {self.altura}")
    print(f"Data de nascimento: {self.ano}")


class Pessoa:
    def __init__(self, nome, peso, altura, ano=2000):
        self.nome = nome
        self.peso = peso
        self.altura = altura
        self.ano = ano

    def get_nome(self):
        return self.nome

    def get_peso(self):
        return self.peso

    def get_altura(self):
        return self.altura

    def get_ano(self):
        return self.ano

    def set_nome(self, novo_nome):
        if len(novo_nome) <= 0 or novo_nome.isnumeric():
            print("Nome inválido")
        else:
            self.nome = novo_nome
            print("Nome alterado!")

    def set_peso(self, novo_peso):
        self.peso = novo_peso

    def set_altura(self, nova_altura):
        self.altura = nova_altura

    def set_ano(self, novo_ano):
        self.ano = novo_ano

    def imc(self):
        conta = self.peso / (self.altura * self.altura)
        return conta

    def calcula_idade(self):
        data_atual = date.today()
        data_ano = data_atual.strftime("%Y")
        conta = int(data_ano) - self.ano
        return conta

    def __str__(self):
        s = f"Nome: {self.nome}\nPeso: {self.peso}\nAno de nascimento: {self.ano}"
        return s

    def mais_velho(self, obj):
        if self.ano < obj.ano:
            print(f"Ano de nascimento mais velho: {self.ano}")
            print(f"Ano de nascimento mais novo: {obj.ano}")
        elif obj.ano < self.ano:
            print(f"Ano de nascimento mais velho: {obj.ano}")
            print(f"Ano de nascimento mais novo: {self.ano}")
        else:
            print("As datas são iguais!")


if __name__ == '__main__':
    pessoa1 = Pessoa("Thiago", 68, 1.80, 2005)
    pessoa2 = Pessoa("Giovana", 53, 1.60, 2006)
    mostra_dados(pessoa1)
    linha()
    mostra_dados(pessoa2)
    pessoa2.set_ano(2005)
    linha()
    nome = input("Insira um nome: ")
    pessoa1.set_nome(nome)
    linha()
    pessoa3 = Pessoa("Pedro", 50, 1.60, 2030)
    mostra_dados(pessoa3)
    linha()
    pessoa4 = Pessoa("Alice", 40, 1.40)
    mostra_dados(pessoa4)
    linha()
    print(f"Imc pessoa 1: {pessoa1.imc():.2f}")
    pessoa1.set_ano(2000)
    print("Ano de nascimento pessoa 1 alterado!")
    print(f"Idade pessoa 1: {pessoa1.calcula_idade()}")
    linha()
    print(f"Nome pessoa 2: {pessoa2.get_nome()}")
    print(f"Idade pessoa 2: {pessoa2.calcula_idade()}")
    linha()
    print(pessoa3)
    linha()
    pessoa1.mais_velho(pessoa2)
