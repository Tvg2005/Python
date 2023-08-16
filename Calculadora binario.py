# -*- UTF:coding 8 -*-
sair = False
while sair == False:
    try:
        print("As operações possíveis são: binario para decimal(BD)")
        operacao = input("Insira a conversão desejada")
        if operacao == "BD":
            print("Será disponiblizado ate 12 números, caso deseje operar com menos preencha os numeros desejados e insira 0 nos outros")
            print("Para esta operação os números inseridos devem ser 0 ou 1 e devem ser inseridos de trás para frente")
            num1 = int(input("Insira o primeiro número desejado"))
            num2 = int(input("Insira o segundo número desejado"))
            num3 = int(input("Insira o terceiro número desejado"))
            num4 = int(input("Insira o quarto número desejado"))
            num5 = int(input("Insira o quinto número desejado"))
            num6 = int(input("Insira o sexto número desejado"))
            num7 = int(input("Insira o sétimo número desejado"))
            num8 = int(input("Insira o oitavo número desejado"))
            num9 = int(input("Insira o nono número desejado"))
            num10 = int(input("Insira o décimo número desejado"))
            num11 = int(input("Insira o décimo primeiro número desejado"))
            num12 = int(input("Insira o décimo segundo número desejado"))
            valor = (num1, num2, num3, num4, num5, num6, num7, num8, num9, num10, num11, num12)
            print("O número binario inserido foi: ", valor)
            teste2 = str(input("O valor está correto? (sim/nao)"))
            if teste2 == "sim":
                if operacao == "BD" and (num1, num2, num3, num4, num5, num6, num7, num8, num9, num10, num11, num12 == "0" or "1"):
                    conta = num12 * 2048 + num11 * 1024 + num10 * 512 + num9 * 256 + num8 * 128 + num7 * 64 + num6 * 32 + num5 * 16 + num4 * 8 + num3 * 4 + num2 * 2 + num1 * 1
                print("O número inserido em decimal é:", conta)
                teste = str(input("Deseja sair? (sim/nao)"))
                if teste == "sim":
                    sair = True
            else:
                teste3 = str(input("Deseja inserir novamente (sim/nao)"))
                if teste3 == "sim":
                    continue
                else:
                    sair = True
        else:
            print("A operação não foi reconhecida")
            continue
    except ValueError:
            print("Não foi digitado um numero")