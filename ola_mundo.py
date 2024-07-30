import math
from pyfiglet import Figlet
from time import sleep

def soma(x,y):
    return x+y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y 

def divisao(x,y):
    return x / y

def raiz(x):
    return math.sqrt(x)

def txt(x):
    print(t.renderText(str(x)))


def rsl_txt(x):
    print(r.renderText(str(x)))

def operacoes(x):
    print(op.renderText(str(x)))

lista = ["+","-","*","/"]

t = Figlet(font='fender')
r = Figlet(font='smkeyboard')
op = Figlet(font='larry3d')


txt('Calculadora')
print('-' * 80)
while True:
    print()
    txt('Operacoes possiveis:  (1)-Basicas  (2)-Raiz (3)-Sair')
    crud = input('Opção: ')
    if crud == "2":
        conta = int(input('Número: '))
        rsl_txt(raiz(conta))

    elif crud == "1":
        operacoes('+ - * /')
        
        conta = input('Operação: ')
        if conta in lista:
            x = int(input('Insira o primeiro número: '))
            z = int(input('Insira o segundo número: '))
        else:
            txt('Erro')
            sleep(1)
            continue
        if conta=="*":
            rsl_txt(multiplicacao(x, z))
            sleep(1)
        elif conta=="-":
            rsl_txt(subtracao(x, z))
            sleep(1)
        elif conta=="+":
            rsl_txt(soma(x, z))
            sleep(1)
        elif conta=="/" and z != 0:
            rsl_txt(divisao(x, z))
            sleep(1)
    elif crud == '3':
        break
    else:
        sleep(1)
        txt('Operacao nao existe')
