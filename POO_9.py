import math


def linha():
    print("-" * 75)


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, novo_x):
        if novo_x == float:
            print("Valor inválido")
        else:
            self.x = novo_x

    def set_y(self, novo_y):
        self.y = novo_y

    def __str__(self):
        return f"X: {self.get_x()} Y: {self.get_y()}"

    def calcula_distancia_origem(self):
        distancia = math.sqrt(pow((self.get_x() - 0), 2) + pow(self.get_y() - 0, 2))
        print(f"Distancia origem: {distancia:.2f}")

    def calcula_distancia_2pontos(self, obj):
        distancia2 = math.sqrt(pow((self.get_x() - obj.get_x()), 2) + pow(self.get_y() - obj.get_y(), 2))
        print(f"Distancia 2 pontos: {distancia2:.2f}")

    def mais_distante_origem(self, obj):
        distancia_p1 = math.sqrt(pow((self.get_x() - 0), 2) + pow(self.get_y() - 0, 2))
        distancia_p2 = math.sqrt(pow((obj.get_x() - 0), 2) + pow(obj.get_y() - 0, 2))
        if distancia_p1 > distancia_p2:
            print("O primeiro ponto é mais distante da origem")
        elif distancia_p2 > distancia_p1:
            print("O segundo ponto é mais distante da origem")
        else:
            print("Os pontos possuem a mesma distância da origem")

    def retorna_mais_distante_origem(self, obj):
        distancia_p1 = math.sqrt(pow((self.get_x() - 0), 2) + pow(self.get_y() - 0, 2))
        distancia_p2 = math.sqrt(pow((obj.get_x() - 0), 2) + pow(obj.get_y() - 0, 2))
        if distancia_p1 > distancia_p2:
            return distancia_p1
        elif distancia_p2 > distancia_p1:
            return distancia_p2
        else:
            print("Os dois pontos possuem a mesma distancia!")
            return distancia_p1

    def ponto_medio(self, obj):
        m = (self.get_x() + obj.get_x()) / 2 + (self.get_y() + obj.get_y()) / 2
        print(f"Ponto médio: {m}")

    def return_ponto_medio(self, obj):
        m = (self.get_x() + obj.get_x()) / 2 + (self.get_y() + obj.get_y()) / 2
        return f"Ponto médio: {m}"


if __name__ == '__main__':
    p1 = Point()
    p2 = Point(2, 3)
    p3 = Point(3)
    p4 = Point(y=5)
    print(f"Ponto 1\nX: {p1.get_x()}\nY: {p1.get_y()}")
    linha()
    print(p1)
    p2.calcula_distancia_origem()
    linha()
    p2.calcula_distancia_2pontos(p3)
    linha()
    p2.calcula_distancia_2pontos(p4)
    linha()
    p2.mais_distante_origem(p4)
    linha()
    p2.ponto_medio(p3)
