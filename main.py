lista = []
print("Digite [0] - sair")
ct = 0
while True:
    x = int(input("Insira um numero para adicionar na lista: "))
    if x == 0:
        break
    else:
        lista.append(x)

print("A - ", len(lista))
print("B - ", sum(lista))
print("C - ", max(lista))
print("D - ", min(lista))

y = int(input("Insira um valor para verificar na lista: "))
if y in lista:
    print(f"E , F - Valor {y} na lista no indice {lista.index(y)}")
else:
    print(f"Valor {y} não está na lista!")

print("G - ", sorted(lista))
lista.insert(1, 33)
print("H - 33 inserido na lista", lista)
lista.sort(reverse=True)
print("I - ", lista)
print("J - ", sum(lista)/len(lista))
print(f"K - {sum(lista)/len(lista):.3f}")
for i in range(len(lista)):
    if lista[i] >= 10:
        ct += 1
porcentagem = ct / len(lista) * 100
print(f"L - {porcentagem:.2f}%")
