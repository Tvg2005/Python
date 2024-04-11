"""
Sistema de criptografia de acordo com a Cifra de César
Data: 11/04/2024
Feito por Thiago Venâncio

A ser tratado:
    - Possibilitar a inserção de frases com acentos e simbolos
"""

from random import randint

def linha():
    print("-" * 100)

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
                frase_criptografada.append(var + 4)
            else:
                frase_criptografada.append(var + 8)

        # Execção caso seja letra ou espaço
        except TypeError:
            if var != "$":
                # Criptografa as letras
                
                

                # Busca o indice na lista com o alfabeto
                pos = lista_letras.index(var)

                # Insere na lista o valor da letra com 3 posições a frente 
                frase_criptografada.append(lista_letras[pos + 3])
            else:

                # Criptografa os espaços de maneira aleatória de acordo com os simbolos presentes na "lista_simb"
                aux = randint(0, 5)
                frase_criptografada.append(lista_simb[aux])


def descriptografa():
    for i in range(len(frase_criptografada)):
        # Seta o ponteiro
        var = frase_criptografada[i]

        # Teste pra ver se é número ou letra/espaço
        try:
            # Descriptografa os números // diferente para par ou ímpar
            if var % 2 == 0:
                frase_descriptografada.append(var - 4)
            else:
                frase_descriptografada.append(var - 8)
        
        # Execção caso seja letra ou espaço
        except:
            
            # Verifica se o ponteiro não está apontando para um simbolo
            if var not in lista_simb:
                # Descriptografa as letras

                # Busca o indice na lista com o alfabeto
                pos = lista_letras.index(var)

                # Insere na lista o valor da letra com 3 posições para trás // retorna ao original 
                frase_descriptografada.append(lista_letras[pos - 3])
            else:
                # Descriptografa os espaços
                frase_descriptografada.append(" ")


if __name__ == "__main__":
    # Declaração das variáveis utilizadas no código
    frase = "" # ...
    senha = "123"
    sair = False
    frase_tratada = []
    frase_criptografada = []
    frase_descriptografada = []
    lista_letras = []
    lista_simb = "%$#@*&"
    letras = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"

    # Cria o while para o usuário inserir a frase. 
    while not sair:
        linha()
        print("Sistema de criptografia")
        linha()
        escolha = int(input("1 - Inserir frase\n2 - Descriptografar frase: "))
        
        # Criptografia 
        if escolha == 1:
            frase = input("Insira a frase: ").lower()
            trata_frase()
            criptografa()
            linha()
            print("Frase criptografada: \n", *frase_criptografada)
        
        # Descriptografia
        elif escolha == 2:
            ver_senha = input("Insira a senha para descriptografar: ")
            if ver_senha == "123":
                if len(frase) == 0:
                    print("Frase não foi cadastrada!")
                else:
                    descriptografa()
                    linha()
                    print("Frase descriptografa: \n", *frase_descriptografada)
                    break
            # Senha inserida errada
            else:
                print("Acesso negado!")
        # Escolha inserida diferente de 1|2
        else:
            print("Escolha inválida!")
