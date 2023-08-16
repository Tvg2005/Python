velocidade = 60
local_carro = 100
RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1
vel_car_rad = velocidade >= RADAR_1
min_radar = LOCAL_1 - RADAR_RANGE
max_radar = LOCAL_1 + RADAR_RANGE
passou = min_radar <= local_carro <= max_radar
multa = passou and vel_car_rad
if vel_car_rad:
    print("Carro passou do limite de velocidade do radar 1")
if passou:
    print("Carro passou no radar 1")
if multa:
    print("Carro multado no radar 1")



condicao = False
passou = None
if condicao:
    passou = True
    print("faça algo")
else:
    print("Não faça algo")

if passou is None:
    print("Não passou")
if passou is not None:
    print("Passou no if")


f = int(input("Insira um valor em graus Fahrenheit: "))
conta = 5 * (f - 32) / 9
print(f"O valor em Celsius é : {conta}")


try:
    num1 = int(input("Insira um valor inteiro: "))
except:
    print("Valor não é um número inteiro!")
    exit()
if num1 % 5 == 0:
    if num1 % 2 == 0:
        print("O número é par e múltiplo de cinco!")
    else:
        print("O número é impar e múltiplo de cinco!")
else:
    if num1 % 2 == 0:
        print("O número é par e não é múltiplo de cinco!")
    else:
        print("O número é impar e não é múltiplo de cinco!")


ct = 0
soma = 0
idade_maior = 0
while True:
    idade = int(input("Insira sua idade [0]- Sair: "))
    if idade == 0:
        break
    peso = int(input("Insira seu peso [0]- Sair: "))
    if peso == 0:
        break
    soma = soma + peso
    ct += 1

    if idade > idade_maior:
        idade_maior = idade
print(f"A quantidade de pessoas analisadas é de {ct}")
print(f"A soma dos pesos é {soma}")
print(f"A pessoa mais velha é {idade_maior}")

genero = input("Insira seu genero [M] [F]: ")
if genero == "M":
    altura = float(input("Insira sua altura: "))
    if altura >= 1.80:
        print("Pode ser modelo!")
    else:
        print("Não pode ser modelo")

if genero == "F":
    altura = float(input("Insira sua altura:"))
    if altura >= 1.75:
        print("Pode ser modelo!")
    else:
        print("Não pode ser modelo")


f = float(input("Insira um valor em fahrenheit: "))
conta = (5 * (f - 32))/9
print(f"O resultado da conta é {conta}")

num1 = int(input("Insira um valor inteiro: "))
if num1 % 2 == 0:
    if num1 % 5 == 0:
        print("O número é par e divisivel por 5!")
    else:
        print("O número é par e n eh divisivel por 5!")
else:
    if num1 % 5 == 0:
        print("O valor é par e divisivel por 5!")
    else:
        print("O valor é impar e n divisivel por 5!")

ct = 0
idade_maior = 0
soma = 0
print("Digite [0] para sair em qualquer um dos campos!")
while True:
    idade = int(input("Insira sua idade: "))
    if idade == 0:
        break
    peso = float(input("Insira seu peso: "))
    if peso == 0:
        break
    soma = soma + idade
    ct += 1
    if idade_maior < idade:
        idade_maior = idade
    print("Dados inseridos com sucesso! Proximo!")
print(f"A quantidade de pessoas analisadas foi {ct}")
print(f"A maior idade foi {idade_maior}")
print(f"A soma das idades foi {soma}")

