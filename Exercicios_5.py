ESTUDO PROVA
lista = []
print("Digite [-1] para sair!")
while True:
    numero = int(input("Insira um inteiro: "))
    if numero == -1:
        break
    lista.append(numero)
if len(lista) == 0:
    print("A lista esta vazia")
else:
    print(f"O maior valor inserido é {max(lista)}")
    print(f"O menor valor inserido é {min(lista)}")
    print(f"A quantidade de valores digitados foi: {len(lista)}")
    print(f"A soma dos valores digitados é {sum(lista)}")
    print(f"A media dos valores digitados é {sum(lista) / len(lista)}")

def conversor(horas=0, minutos=0):
    resultado = (horas * 60) + minutos
    return resultado


if __name__ == '__main__':
    h = int(input("Insira a quantidade de horas: "))
    m = int(input("Insira a quantidade de minutos: "))
    total = conversor(h, m)
    print(f"{h} horas + {m} minutos = {total} minutos")


def operacao(x=0, y=0):
    conta = 0
    if operador == "+":
        conta = x + y
    elif operador == "-":
        conta = x - y
    return conta


if __name__ == '__main__':
    num1 = int(input("Insira um numero: "))
    num2 = int(input("Insira outro numero: "))
    operador = input("Insira o operador [+] [-]: ")
    check = "+-"
    if operador not in check:
        print("Operador n reconhecido")
    else:
        resultado = operacao(num1, num2)
        print(f"{num1} {operador} {num2} = {resultado}")


def separador(x=0, y=0):
    if x > y:
        return x
    elif y > x:
        return y
    else:
        return x


if __name__ == '__main__':
    num1 = int(input("Insira um numero: "))
    num2 = int(input("Insira outro numero: "))
    if num1 != num2:
        print(f"O numero {separador(num1, num2)} é o maior")
    else:
        print(f"Ambos os numeros sao iguais")
print("Digite [0] para sair!")
lista_par = []
lista_impar = []
ct_linha = 0
while True:
    x = int(input("Insira um numero: "))
    if x == 0:
        break
    if x % 2 == 0:
        lista_par.append(x)
    else:
        lista_impar.append(x)
print("-" * 75)
if len(lista_par) == 0:
    print("Lista par vazia!")
else:
    ct_linha += 1
    print(f"A lista par possui {len(lista_par)} termos")
    print(f"A soma desses termos é {sum(lista_par)}")
    print(f"A media desses termos é {sum(lista_par) / len(lista_par):.2f}")
    print(f"O menor valor da lista par é {min(lista_par)}")
    print(f"O maior valor da lista par é {max(lista_par)}")
if ct_linha == 1:
    print("-" * 75)
if len(lista_impar) == 0:
    print("Lista impar vazia!")
else:
    print(f"A lista impar possui {len(lista_impar)} termos")
    print(f"A soma desses termos é {sum(lista_impar)}")
    print(f"A media desses termos é {sum(lista_impar) / len(lista_impar):.2f}")
    print(f"O menor valor da lista impar é {min(lista_impar)}")
    print(f"O maior valor da lista impar é {max(lista_impar)}")
print("-" * 75)
def multiplicador(x):
    def multiplicar(y):
        return y * x
    return multiplicar


num = int(input("Insira um numero: "))
num2 = int(input("Insira por quanto deseja multiplicar o numero: "))
funcao = multiplicador(num2)
print(f"{num} * {num2} = {funcao(num)}")
