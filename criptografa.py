"""
Sistema de criptografia de acordo com a Cifra de César
Data: 11/04/2024
Feito por Thiago Venâncio
 
requirements - pip install unidecode 
"""
# Bibliotecas
from random import randint
from unidecode import unidecode



# Linha para estética
def linha():
    print("-" * 100)


# Declara as variáveis
def dec_var():
    global frase, senha, frase_tratada, frase_criptografada, frase_descriptografada, lista_letras, lista_simb, letras, lista_simb2
    frase = ""
    senha = "123"
    frase_tratada = []
    frase_criptografada = []
    frase_descriptografada = []
    lista_letras = []
    lista_simb = "~^`´"
    lista_simb2 = "!@#$%&*()°]}[{|;:>,./<-_=+'?!@#$%&*()°]}[{|;:>,./<-_=+'?"
    letras = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"


# Faz a inicialização do código
def inicializacao():
    global escolha
    linha()
    print("Sistema de criptografia")
    linha()
    escolha = int(input(f"1 - Inserir frase\n2 - Descriptografar frase: \n{"-" * 100}\nOpção: "))


# Faz o tratamento da frase inicial para a lógica do código
def trata_frase():
    # Insere as letras em uma lista para facilitar a lógica do código

    for i in letras:
        lista_letras.append(i)

    for i in range(len(frase)):

        # Insere "$" no lugar do espaço, informação será usada no código "def criptografa():"
        if frase[i] == " ":
            frase_tratada.append("$")
        
        # Converte os números presentes na frase para inteiros            
        else:
            try:
                var = int(frase[i])
                frase_tratada.append(var)
            except:
                frase_tratada.append(frase[i])


def criptografa():
    for i in range(len(frase_tratada)):
        # Seta o ponteiro
        var = frase_tratada[i]
        
        # Teste para ver se é número ou letras/espaço
        try:
            # Criptografa os números // Diferente para impar e par
            if var % 2 == 0:
                frase_criptografada.append(var + 2)
            else:
                frase_criptografada.append(var + 2)

        # Execção caso seja letra ou espaço
        except TypeError:
            if var not in lista_simb2:
                # Criptografa as letras
                
                

                # Busca o indice na lista com o alfabeto
                pos = lista_letras.index(var)

                # Insere na lista o valor da letra com 3 posições a frente 
                frase_criptografada.append(lista_letras[pos + 3])
            else:
                if var == "$":
                    # Criptografa os espaços de maneira aleatória de acordo com os simbolos presentes na "lista_simb"
                    aux = randint(0, 3)
                    frase_criptografada.append(lista_simb[aux])
                else:
                    # Criptografa os símbolos de acordo com a lista_simb2
                    pos = lista_simb2.index(var)
                    frase_criptografada.append(lista_simb2[pos + 3])


def descriptografa():
    for i in range(len(frase_criptografada)):
        # Seta o ponteiro
        var = frase_criptografada[i]

        # Teste pra ver se é número ou letra/espaço
        try:
            # Descriptografa os números // diferente para par ou ímpar
            if var % 2 == 0:
                frase_descriptografada.append(var - 2)
            else:
                frase_descriptografada.append(var - 2)
        
        # Execção caso seja letra ou espaço
        except:
            
            # Verifica se o ponteiro não está apontando para um simbolo
            if var not in lista_simb2 and var not in lista_simb:
                # Descriptografa as letras

                # Busca o indice na lista com o alfabeto
                pos = lista_letras.index(var)

                # Insere na lista o valor da letra com 3 posições para trás // retorna ao original 
                frase_descriptografada.append(lista_letras[pos - 3])
            else:
                if var in lista_simb:
                    # Descriptografa os espaços
                    frase_descriptografada.append("+")
                else:
                    pos = lista_simb2.index(var)
                    frase_descriptografada.append(lista_simb2[pos-3])


# Trata o input da descriptografia
def input_descripto():
    frase_cripto = input("Insira a frase criptografada: ")
    for i in frase_cripto:
        frase_criptografada.append(i)


# Faz a lógica do print, printando de forma que a resposta fique formatada corretamente
def print_inline(x):
    if len(frase) != 0:
        print("Frase Criptografada:")
    else:
        print("Frase Descriptografada:")
    for i in x:
        if i == "+":
            print(" ",end="")
        elif i != " ":
            print(i,end="")
    print()
    linha()
    

# Chama as funções da descriptografia
def func_descripto():
    linha()
    input_descripto()
    if len(frase_criptografada) == 0:
        print("Frase não foi cadastrada!")
    else:
        trata_frase()
        descriptografa()
        linha()
        print_inline(frase_descriptografada)


# Chama as funções da criptografia
def func_cripto():
    global frase
    linha()
    frase = unidecode(input("Insira a frase: ").lower())
    trata_frase()
    criptografa()
    linha()
    print_inline(frase_criptografada)
    
    
def main():
    dec_var() # Declara as variáveis
    while True:
        inicializacao() # Da inicio aos códigos
        if escolha == 1:
            func_cripto() # Chama as funções utilizadas na criptografia
            break
        elif escolha == 2:
            linha()
            ver_senha = input("Insira a senha para descriptografar: ") 
            if ver_senha == "123":  # Verifica a senha para descriptografar
                func_descripto() # Chama as funções utilizadas na descriptografia
                break
            else:
                print("Acesso negado!")
        else:
            print("Escolha inválida!")


if __name__ == "__main__":
    main()
