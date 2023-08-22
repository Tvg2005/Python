ct = 0


def linha():
    print("-" * 75)


def mostra_dados(x):
    global ct
    linha()
    ct += 1
    print(f"Aluno {ct}:")
    print(f"Nome: {x.get_nome()}")
    print(f"Mensalidae: {x.get_mensalidade()}")
    print(f"Idade {x.get_idade()}")


def cnh(y):
    if y.get_idade() >= 18:
        print("Pode tirar cnh")
    else:
        print("Não pode tirar cnh")

class Aluno:
    def __init__(self, nome, mensalidade, idade):
        self.nome = nome
        self.mensalidade = mensalidade
        self.idade = idade

    def get_nome(self):
        return self.nome

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_mensalidade(self):
        return self.mensalidade

    def set_mensalidade(self, valor):
        self.mensalidade = valor

    def get_idade(self):
        return self.idade

    def set_idade(self, nova_idade):
        self.idade = nova_idade

    def aumento_mensalidade_valor(self, nova_mensalidade):
        self.mensalidade = nova_mensalidade + self.mensalidade
        return self.mensalidade

    def aumento_mensalidade_porcentagem(self, porcentagem):
        self.mensalidade = self.mensalidade + self.mensalidade / 100 * porcentagem
        return self.mensalidade

    def reset(self):
        self.mensalidade = 1000
        self.idade = 18


if __name__ == '__main__':
    aluno1 = Aluno("Thiago", 1100.00, 18)
    aluno2 = Aluno("Giovana", 900.00, 17)
    mostra_dados(aluno1)
    mostra_dados(aluno2)
    linha()
    aluno1.set_nome("Fernando")
    print(f"Aluno novo: {aluno1.get_nome()}")
    linha()
    aumento = int(input("Insira a quantidade para aumentar a mensalidade aluno1: "))
    aluno1.aumento_mensalidade_valor(aumento)
    print(f"Mensalidade nova do aluno 1: {aluno1.get_mensalidade()}")
    linha()
    aumento_porcent = int(input("Insira a porcentagem de aumento da mensalidade: "))
    aluno2.aumento_mensalidade_porcentagem(aumento_porcent)
    print(f"Mensalidade com aumento de {aumento_porcent}% do aluno2: {aluno2.get_mensalidade()}")
    linha()
    cnh_input = int(input("Insira o aluno para verificar se pode tirar cnh [1][2]: "))
    if cnh_input == 1:
        cnh(aluno1)
    else:
        cnh(aluno2)
    aluno1.reset()
    aluno2.reset()
    linha()
    print("Mensalidade e idades voltaram ao padrão")
    ct = 0
    aluno1.set_nome("Thiago")
    mostra_dados(aluno1)
    mostra_dados(aluno2)
    linha()