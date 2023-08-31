from random import randint


def linha():
    return "-" * 75


def mostrar_times():
    print(linha())
    print(f"Time 1:\n{time1.get_nome()}\nTitulos: {time1.get_titulos()}\nAno de criação: {time1.get_ano()}\n{linha()}")
    print(f"Time 2:\n{time2.get_nome()}\nTitulos: {time2.get_titulos()}\nAno de criação: {time2.get_ano()}\n{linha()}")
    print(f"Time 3:\n{time3.get_nome()}\nTitulos: {time3.get_titulos()}\nAno de criação: {time3.get_ano()}\n{linha()}")


class Time:
    def __init__(self, nome, titulos, ano):
        self.nome = nome
        self.titulos = titulos
        self.ano = ano

    def get_nome(self):
        return self.nome

    def get_titulos(self):
        return self.titulos

    def get_ano(self):
        return self.ano

    def set_nome(self, novo_nome):
        if len(novo_nome) <= 0:
            print("Número de caracteres inválido!")
        else:
            self.nome = novo_nome

    def set_titulos(self, novo_titulos):
        self.titulos = novo_titulos

    def set_ano(self, novo_ano):
        self.ano = novo_ano

    def aumentar_titulos(self):
        titulos_add = int(input("Insira quantos titulos deseja adicionar: "))
        self.titulos = titulos_add + self.titulos

    def campeonato(self):
        numero_primeiro_time = randint(0, 38)
        numero_segundo_time = randint(0, 38)
        numero_terceiro_time = randint(0, 38)
        if numero_primeiro_time > numero_segundo_time and numero_primeiro_time > numero_terceiro_time:
            print(f"{time1.get_nome()} foi o vencedor do campeonato! Somando {numero_primeiro_time} vitórias!")
            print(linha())
            print(f"Vitórias dos demais:\n{time2.get_nome()}: {numero_segundo_time}"
                  f"\n{time3.get_nome()}: {numero_terceiro_time}")
        elif numero_segundo_time > numero_primeiro_time and numero_segundo_time > numero_terceiro_time:
            print(f"{time2.get_nome()} foi o vencedor do campeonato! Somando {numero_segundo_time} vitórias!")
            print(linha())
            print(f"Vitórias dos demais:\n{time1.get_nome()}: {numero_primeiro_time}"
                  f"\n{time3.get_nome()}: {numero_terceiro_time}")
        else:
            print(f"{time3.get_nome()} foi o vencedor do campeonato! Somando {numero_terceiro_time} vitórias!")
            print(linha())
            print(f"Vitórias dos demais:\n{time2.get_nome()}: {numero_segundo_time}"
                  f"\n{time1.get_nome()}: {numero_primeiro_time}")


if __name__ == '__main__':
    time1 = Time("Palmeiras", 20, 1930)
    time2 = Time("Flamengo", 5, 0)  # Vai dar erro caso n coloque todos os atributos
    time3 = Time("Cruzeiro", 0, 0)
    mostrar_times()
    time2.set_ano(1940)
    print("Ano do time 2 alterado!")
    time3.set_titulos(8)
    time3.set_ano(1920)
    time3.set_nome("Fluminense")
    print(linha())
    print("Time 3 alterado!")
    mostrar_times()
    print("----------------------------Campeonato de times----------------------------")
    time1.campeonato()
