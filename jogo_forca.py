import os


def linha():
    print("-" * 25)


def desenho():
    if vidas == 5:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()
    elif vidas == 4:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|    | ")
        print("|    | ")
        print("|      ")
        print("_      ")
        print()
    elif vidas == 3:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|    |\ ")
        print("|    | ")
        print("|      ")
        print("_      ")
        print()
    elif vidas == 2:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /|\ ")
        print("|    | ")
        print("|      ")
        print("_      ")
        print()
    elif vidas == 1:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /|\ ")
        print("|    | ")
        print("|     \ ")
        print("_      ")
        print()
    elif vidas == 0:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /|\ ")
        print("|    | ")
        print("|   / \ ")
        print("_      ")
        print()


while True:
    escolha = input("Escolha a palavra da forca!: ").upper()
    os.system("cls")
    escolha_sem_espaco = escolha.replace(" ", "")
    if not escolha_sem_espaco.isalpha():
        print("Insira apenas letras!")
    else:
        break
palavra = escolha
print("JOGO DA FORCA!\nVOCÊ TEM 6 VIDAS")
letra_acertada = ""
letras_erradas = ""
palavra_formatada_rep = []
for i in range(len(escolha)):
    palavra_formatada_rep.append("")
for k in range(len(escolha)):
    palavra_formatada_rep[k] = str(escolha[k])
    if palavra_formatada_rep[k] == " ":
        palavra_formatada_rep[k] = ""
        letra_acertada += " "
vidas = 6
ct = 0
ct_e = 0
ct_for = 0
i = 0
sair = False
while not sair:
    ct += 1
    linha()
    letra = input("Insira uma letra: ").upper()
    if len(letra) == 0:
        linha()
        print("Você não pode deixar em branco!")
        continue
    elif not letra.isalpha():
        linha()
        print("Caractere inválido!")
        continue
    elif len(letra) != 1:
        linha()
        print("Digite apenas uma letra!")
        continue
    if letra not in palavra:
        if letra not in letras_erradas:
            letras_erradas += letra
            print("Letra incorreta, tente outra!")
            vidas -= 1
            print(f"Agora você tem {vidas} vidas")
            desenho()
            ct_e += 1
            linha()
        else:
            print("Essa letra ja foi errada!\nTente novamente!")
            print(f"Você não perdeu vidas!\nVidas: {vidas}")
            continue
    if letra in palavra:
        if letra in letra_acertada:
            print("Essa letra ja havia sido acertada!")
            continue
        else:
            letra_acertada += letra
            for j in range(len(escolha)):
                if palavra_formatada_rep[j] == letra:
                    palavra_formatada_rep[j] = ""
    for letra_secreta in palavra:
        i += 1
        if letra_secreta in letra_acertada:
            print(letra_secreta, end="")
        else:
            print("*", end="")
        if i == len(palavra):
            print("\n")
            i = 0
    ct_for = 0
    for j in range(len(escolha)):
        if palavra_formatada_rep[j] != "":
            ct_for += 1
    if ct_for == 0:
        print("PARABENS VOCÊ CONSEGUIU!!!")
        sair = True
    if vidas == 0:
        print("Suas vidas acabaram, você perdeu!")
        print(f"A palavra era {palavra}")
        sair = True
print(f"Tentativas totais: {ct}")
print(f"Total de tentativas erradas: {ct_e}")
print(f"Vidas restantes {vidas}")
if len(letras_erradas) == 0:
    print("Nenhuma letra errada")
else:
    print("As letras erradas foram:")
    for i in range(len(letras_erradas)):
        if i < len(letras_erradas)-1:
            print(f"{letras_erradas[i]} / ", end="")
        else:
            print(f"{letras_erradas[i]}")
