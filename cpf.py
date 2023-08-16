import random


def linha():
    print("-" * 75)


sair = False
while not sair:
    escolha = input("Deseja gera um cpf ou validar o cpf [1] - Gerar [2] - Validar: ")
    linha()
    if escolha == "2":
        print("Validador de cpf!")
        cpf = input("Insira o cpf: ")
        linha()
        cpf_formatado = []
        conta = 0
        digito_um = 0
        conta_digito2 = 0
        ct = 10
        ct_2 = 11
        for i in range(len(cpf)):
            if cpf[i] != "-" and cpf[i] != ".":
                cpf_formatado.append(cpf[i])
        for j in range(len(cpf_formatado) - 2):
            cpf_formatado[j] = int(cpf_formatado[j])
            if j == 8:
                cpf_formatado[j + 1] = int(cpf_formatado[j + 1])
                cpf_formatado[j + 2] = int(cpf_formatado[j + 2])
            conta += ct * cpf_formatado[j]
            ct -= 1
        conta *= 10
        resto = conta % 11
        digito_um = 0 if resto > 9 else resto
        for k in range(len(cpf_formatado) - 1):
            conta_digito2 += ct_2 * cpf_formatado[k]
            ct_2 -= 1
        conta_digito2 *= 10
        resto2 = conta_digito2 % 11
        digito_dois = 0 if resto2 > 9 else resto2
        if cpf_formatado[9] != digito_um or cpf_formatado[10] != digito_dois:
            print("O cpf é inválido!")
        else:
            print(f"O CPF digitado foi: {cpf}")
            print("CPF válido!")
            linha()
            continuar = input("Digite [S] - Sair ou outra coisa para continuar: ").upper()
            linha()
            if continuar == "S":
                sair = True
    elif escolha == "1":
        qtd = int(input("Quantos CPFs deseja gerar: "))
        linha()
        ct_qtd = 1
        qtd += 1
        while qtd != ct_qtd:
            cpf = ""
            for i in range(0, 11):
                cpf += str(random.randint(0, 9))
            cpf_formatado = []
            cpf_arrumado = ""
            conta = 0
            digito_um = 0
            conta_digito2 = 0
            ct = 10
            ct_2 = 11
            ct_3 = 0
            for i in range(len(cpf)):
                cpf_formatado.append(cpf[i])
            for j in range(len(cpf_formatado) - 2):
                cpf_formatado[j] = int(cpf_formatado[j])
                if j == 8:
                    cpf_formatado[j + 1] = int(cpf_formatado[j + 1])
                    cpf_formatado[j + 2] = int(cpf_formatado[j + 2])
                conta += ct * cpf_formatado[j]
                ct -= 1
            conta *= 10
            resto = conta % 11
            digito_um = 0 if resto > 9 else resto
            for k in range(len(cpf_formatado) - 1):
                conta_digito2 += ct_2 * cpf_formatado[k]
                ct_2 -= 1
            conta_digito2 *= 10
            resto2 = conta_digito2 % 11
            digito_dois = 0 if resto2 > 9 else resto2
            for i in range(len(cpf_formatado)):
                cpf_formatado[i] = str(cpf_formatado[i])
            if cpf_formatado[9] == str(digito_um) and cpf_formatado[10] == str(digito_dois):
                for i in range(len(cpf_formatado)):
                    if i == 3 or i == 6:
                        cpf_arrumado += "."
                    if i == 9:
                        cpf_arrumado += "-"
                    try:
                        cpf_arrumado += cpf_formatado[ct_3]
                    except:
                        cpf_arrumado += cpf_formatado[9]
                        cpf_arrumado += cpf_formatado[10]
                    ct_3 += 1
                print(f"O CPF numero {ct_qtd} gerado foi: {cpf}")
                print(f"O CPF numero {ct_qtd} formatado fica: {cpf_arrumado}")
                linha()
                ct_qtd += 1
        continuar = input("Digite [S] - Sair ou outra coisa para continuar: ").upper()
        linha()
        if continuar == "S":
            sair = True
    else:
        print("Operação não identificada!")
