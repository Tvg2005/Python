# -*- coding: utf-8 -*-
"""
Calculadora
Autor: Thiago Venancio
Função: fazer contas.
"""

print("-----CALCULADORA V1.0-----")
sair = False

while sair == False:
    try:
        numero1 = int(input("Insira o primeiro número da operação: "))
        numero2 = int(input("Insira o segundo número da operação: "))
        print("Legenda das operações: [*] - multiplicação, [+] - somar, [-] - subtrair, [/] - dividir, [**] - elevar")
        operacao = input("Insira a operação desejada: ")

        conta = "resultado nao existente"

        if operacao == "+":
            conta = numero1 + numero2

        elif operacao == "-":
            conta = numero1 - numero2

        elif operacao == "*":
            conta = numero1 * numero2

        elif operacao == "/" and numero2 != 0:
            conta = numero1 / numero2

        elif operacao == "**":
            conta = numero1 ** numero2


        print("O Resultado foi: ")
        print(conta)
        teste = input("Deseja sair? (Sim/Nao): ").upper
        if teste == "SIM":
            sair = True

    except:
        print("Operacao invalida")
        sair = False
        continue
