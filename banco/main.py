from datetime import datetime
import os

sair = False
senha1 = 1

while sair == False:
    try:
        print("[Conta Banco do Brasil]")
        print("Acesse seu cofre com sua senha")
        if senha1 != "123":
            senha1 = input("Insira a senha do cofre: ")
        if senha1 == "123":
            print("Senha correta. Acesso liberado!")
            operacao = input("Qual operacao deseja fazer? (1 - Transferir, 2 - Depositar, 3 - Consultar o saldo,"
                             " 4 - Histórico, 5 - Apagar Histórico): ")
            arq = open("saldobanco.txt")
            linhas = arq.readlines()
            for saldo in linhas:
                saldo = float(saldo)
            if operacao == "3":
                print(f"O saldo da sua conta é {saldo}")
            if operacao == "1":
                num1 = float(input("Insira a quantidade a ser transferida: "))
                cpf = input("Insira o cpf da conta a ser transferido: ")
                print(f"O valor a ser transferido é {num1} para a conta do cpf {cpf}")
                confirmacao = input("Deseja confirmar a transação? (s/n): ")
                if confirmacao == "s":
                    if num1 <= saldo:
                        conta = float(saldo) - float(num1)
                        print(f"O valor {num1} foi transferido para a conta {cpf} com sucesso")
                        print(f"O saldo atual na sua conta é {conta}")
                        arq = open("saldobanco.txt", "w+")
                        arq.write(str(conta))
                        arq = open("historico.txt", "a+")
                        data = datetime.now()
                        data = data.strftime("%d/%m/%Y %H:%M")
                        tipo = " - Transferencia - "
                        arq.write(str(data))
                        arq.write(str(tipo))
                        arq.write(str(num1))
                        arq.write(" - ")
                        arq.write(str(conta))
                        arq.write("\n")
                    else:
                        print("Saldo insuficiente")
                        print(f"O seu saldo é {saldo} ")
            if operacao == "2":
                num2 = float(input("Insira a quantidade a ser depositada: "))
                print(f"O valor a ser depositado é {num2}")
                confirmacao2 = input("Deseja confirmar o deposito? (s/n): ")
                if confirmacao2 == "s":
                    conta = float(saldo) + float(num2)
                    print(f"O valor {num2} foi depositado com sucesso! ")
                    print(f"O saldo atual na sua conta é {conta}")
                    arq = open("saldobanco.txt", "w+")
                    arq.write(str(conta))
                    arq = open("historico.txt", "a+")
                    data = datetime.now()
                    data = data.strftime("%d/%m/%Y %H:%M")
                    tipo = " - Deposito - "
                    arq.write(str(data))
                    arq.write(str(tipo))
                    arq.write(str(num2))
                    arq.write(" - ")
                    arq.write(str(conta))
                    arq.write("\n")
            if operacao == "4":
                arq = open("historico.txt")
                linha2 = arq.readlines()
                hist = ""
                for historico in linha2:
                    hist = hist + historico
                print(f"Histórico: \n{hist}")
            if operacao == "5":
                teste2 = input("Deseja apagar o histórico? (s/n): ")
                if teste2 == "s":
                    layout = "Data - Tipo - Valor - Saldo"
                    arq = open("historico.txt", "w+")
                    arq.write(str(layout))
                    arq = open("historico.txt")
                    linha2 = arq.readlines()
                    hist = ""
                    for historico in linha2:
                        hist = hist + historico
                    print(f"O seu histórico foi apagado com sucesso! \nHistórico: \n{hist}")
            teste1 = input("Deseja sair? (s/n): ")
            if teste1 == "s":
                sair = True
            else:
                os.system("cls")
        else:
            print("Acesso negado""\n""Senha incorreta")
    except:
        print("Operação não reconhecida")
        continue
