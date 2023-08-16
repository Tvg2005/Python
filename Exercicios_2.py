ct = 0
soma = 0
ct1 = 0


def linha():
    print("-" * 25)


print("Insira [-1] para finalizar a inserção de notas")
linha()
nome = input("Insira o nome do aluno: ")
while True:
    ct1 = ct + 1
    linha()
    nota = float(input(f"Insira a nota{ct1}: "))
    if nota == -1:
        break
    else:
        soma = soma + nota
        ct += 1
if ct == 0:
    print("Divisão por zero")
    exit()
media = soma / ct
linha()
print(f"A media do aluno {nome} é {media:.2f}")
