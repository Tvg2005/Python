lista = []
print("Digite [0] - sair")
ct = 0
while True:
    x = int(input("Insira um número para adicionar na lista: "))
    if x == 0:
        break
    else:
        lista.append(x)

print(f"Tamanho lista {len(lista)}")
print(f"Soma da lista {sum(lista)}")
print(f"Maior número da lista {max(lista)}")
print(f"Menor número da lista {min(lista)}")

y = int(input("Insira um valor para verificar na lista: "))
if y in lista:
    print(f"Valor {y} na lista no índice {lista.index(y)}")
else:
    print(f"Valor {y} não está na lista!")
print(f"Lista em ordem crescente {sorted(lista)}")
lista.insert(1, 33)
print(f"Número 33 inserido na lista, lista atualizada {lista}")
lista.sort(reverse=True)
print(f"Lista invertida {lista}")
print(f"Media da lista {sum(lista)/len(lista):.2f}")
for i in range(len(lista)):
    if lista[i] >= 10:
        ct += 1
porcentagem = ct / len(lista) * 100
print(f"Porcentagem de números maiores ou igual a dez na lista {porcentagem}%")