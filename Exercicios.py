#EXERCICIO B
numero1 = int(input("Insira um número: "))
if numero1 > 0:
    print("Valor positivo")
elif numero1 < 0:
    print("Valor negativo")
else:
    print("Valor igual a 0")

#EXERCICIO C
nota1 = int(input("Insira a primeira nota: "))
nota2 = int(input("Insira a segunda nota: "))
media = (nota1 + nota2)/2
print("A media do aluno é", media)
if 10 > media >= 7:
    print("Aprovado")
elif media < 7:
    print("Reprovado")
elif media == 10:
    print("Aprovado com Distinção")


#EXERCICIO D
numero1 = int(input("Insira um número: "))
numero2 = int(input("Insira um número: "))
numero3 = int(input("Insira um número: "))
if numero1 > numero2 and numero1 > numero3:
    print("o maior é", numero1)
elif numero2 > numero1 and numero2 > numero3:
    print("o maior é", numero2)
elif numero3 > numero1 and numero3 > numero2:
    print("o maior é", numero3)
else:
    print("Todos são iguais", numero1, numero2, numero3)

#EXERCICIO E
morango = int(input("Insira a quantidade de kilos adquirida de morango: "))
maca = int(input("Insira a quantidade de kilos adquirida de maçã: "))
if morango <= 5:
    conta1 = morango * 2.5
else:
    conta1 = morango * 2.2
if maca <= 5:
    conta2 = maca * 1.8
else:
    conta2 = maca * 1.5
kg = morango + maca
total = conta1 + conta2
if kg > 8 or total > 25:
    desconto = total / 10
    total2 = total - desconto
    print(f"O valor total é de", total2, f"com um desconto de {desconto:.2f}")
else:
    print("O total é de", total)










