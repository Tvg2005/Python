def soma(x, y):
    conta = x + y
    print(f"{x = } + {y = } | x + y = {conta}")


num1 = int(input("Insira um numero: "))
num2 = int(input("Insira outro numero: "))
soma(num1, num2)
soma(2, 1)
soma(y=2, x=1)



def soma(x, y, z=None):
    if z is not None:
        print(f"{x = } + {y = } + {z = } = ", x + y + z)
    else:
        print(f"{x = } + {y = } = ", x + y)


soma(1, 2)
soma(4, 5, 6)
soma(10, 20)
soma(5, 30)


def calculadora(x=0, y=0, z=0):
    if operador == "+":
        if qtd == 1:
            return x
        elif qtd == 2:
            return x + y
        else:
            return x + y + z
    elif operador == "*":
        if qtd == 1:
            return x
        elif qtd == 2:
            return x * y
        else:
            return x * y * z
    elif operador == "/":
        if qtd == 1:
            return x
        elif qtd == 2:
            return x / y
        else:
            return x / y / z
    elif operador == "-":
        if qtd == 1:
            return x
        elif qtd == 2:
            return x - y
        else:
            return x - y - z


qtd = int(input("Insira a quantidade de numeros que deseja inserir[1-3]: "))
if qtd > 3 or qtd < 1:
    print("Quantidade invalida!")
else:
    operador = input("Insira a operação a ser realizada: ")
    check = "+-*/"
    if operador not in check:
        print("Operador invalido!")
    else:
        if operador == "+":
            palavra = "soma"
        elif operador == "-":
            palavra = "subtração"
        elif operador == "/":
            palavra = "divisão"
        else:
            palavra = "multiplição"
        if qtd == 1:
            num1 = int(input("Insira um numero: "))
            print(f"O resultado da {palavra} de {qtd} numero = {calculadora(num1)}")
        elif qtd == 2:
            num1 = int(input("Insira um numero: "))
            num2 = int(input("Insira outro numero: "))
            if num2 == 0 and operador == "/":
                print("Divisao por zero")
            else:
                print(f"O resultado da {palavra} de {qtd} numeros = {num1} {operador} {num2} = {calculadora(num1, num2)}")
        else:
            num1 = int(input("Insira um numero: "))
            num2 = int(input("Insira outro numero: "))
            num3 = int(input("Insira o ultimo numero: "))
            if num2 == 0 or num3 == 0 and operador == "/":
                print("Divisao por zero")
            else:
                print(f"O resultado da {palavra} de {qtd} numeros = {num1} {operador} {num2} {operador} {num3} = {calculadora(num1, num2, num3)}")



def multiplicacao(*args):
    conta = 1
    for numero in args:
        conta *= numero
    return conta


print(multiplicacao(1, 2, 3))


def separador():
    if num1 % 2 == 0:
        print(f"{num1} é par")
    else:
        print(f"{num1} é impar")


num1 = int(input("Insira um numero: "))
separador()
