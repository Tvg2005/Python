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
        numero1 = input("Insira o primeiro número da operação: ")
        numero1 = int(numero1)
        numero2 = input("Insira o segundo número da operação: ")
        numero2 = int(numero2)
        print("Legenda das operacões: * para multiplicação, + para somar, - para subtrair, / para dividir, ** para elevar")
        operação = input("Insira a operação desejada")

        conta = "resultado nao existente"

        if operação == "+":
            conta = numero1 + numero2

        if operação == "-":
            conta = numero1 - numero2

        if operação == "*":
            conta = numero1 * numero2

        if operação == "/" and numero2 != 0:
            conta = numero1 / numero2

        if operação == "**":
            conta = numero1 ** numero2


        print("O Resultado foi: ")
        print(conta)
        teste = input("Deseja sair? (Sim/Nao): ")
        if teste == "Sim":
            sair = True

    except:
        print("Operacao invalida")
        sair = False
        continue