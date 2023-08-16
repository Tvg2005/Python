from time import sleep
import os


def linha():
    print("-" * 100)


while True:
    linha()
    escolha = int(input("Digite [1]- Adicionar produtos / [2]- Remover produtos / [3]- Apagar a lista "
                        "/ [4] - Consultar a lista / [5] - Limpar prompt de comando / [0] - Encerrar aplicação: "))
    if escolha == 0:
        break
    elif escolha == 1:
        linha()
        produtos = input("Insira os produtos para serem adicionados a lista: ").lower()
        linha()
        confirm = input(f"Deseja adicionar {produtos} a lista? [s]: ").lower()
        if confirm == "s":
            arq = open("lista.txt", "a+")
            arq.write(str(produtos))
            arq.write("\n")
            linha()
            sleep(0.5)
            print(f"O produto {produtos} foi adicionado a lista com sucesso!")
        else:
            print("Produto não adicionado a lista!")
    elif escolha == 2:
        linha()
        retirar = input("Insira o produto que deseja retirar da lista: ").lower()
        try:
            with open('lista.txt', 'r') as fr:
                lines = fr.readlines()

                with open('lista.txt', 'w') as fw:
                    for line in lines:

                        if line.strip('\n') != retirar:
                            fw.write(line)
            linha()
            sleep(0.5)
            print("Produto retirado com sucesso!")
        except:
            print("Algo não ocorreu como esperado!")
    elif escolha == 3:
        linha()
        erase = input("Deseja apagar a lista por completo? [s]: ").lower()
        if erase == "s":
            arq = open("lista.txt", "w+")
            arq.write("Lista de compras:\n")
            sleep(0.5)
            linha()
            print("Lista completamente apagada!")
            continue
        else:
            print("Lista não apagada!")
            continue
    elif escolha == 4:
        print("#" * 100)
        arq = open("lista.txt", "r")
        print(arq.read())
        print("#" * 100)
    elif escolha == 5:
        os.system("cls")
        continue
    else:
        linha()
        print("Valor não reconhecido!")
