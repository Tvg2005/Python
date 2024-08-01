'''
Criadores: Thiago Venâncio & Mayssa Dias
Data: 01/08/2024
Versão: 1.0
'''

lista_nomes = []
lista_email = []
lista_telefone = []

def adicionar():
    nome = input("Digite o nome: ")
    email = input("Digite o email: ")
    verificar_email(email)
    telefone = input("Digite o telefone acompanhado do DDD: ")
    verificar_tel(telefone)
    linha()
    lista_nomes.append(nome)
    lista_email.append(email)
    lista_telefone.append(telefone)
    print("Informações inseridas!")
    linha()

def linha():
    print('-' * 75)

def listar():
    if len(lista_nomes) == 0:
        print('Lista vazia, por favor inserir nomes primeiro!')
    else:
        for i in range(len(lista_nomes)):
            print(f'Informações: {lista_nomes[i]} | {lista_email[i]} | {lista_telefone[i]}')
            linha()

def procurar():
    if len(lista_nomes) == 0:
        print('Lista vazia, por favor inserir nomes primeiro!')
    else:
        nome_procurar = input('Escolha o nome que deseja procurar: ')
        if nome_procurar in lista_nomes:
            linha()
            indice = lista_nomes.index(nome_procurar)
            print(f'Informações: {lista_nomes[indice]} | {lista_email[indice]} | {lista_telefone[indice]}')
            linha()
        else:
            linha()
            print('Nome não está na lista!')
            linha()

def verificar_tel(telefone):
    if len(telefone) != 11:
        linha()
        print('Telefone inválido!')
        linha()
        telefone = input("Digite o telefone acompanhado do DDD: ")
        return telefone
    
def verificar_email(email):
    if '@' not in email or '.com' not in email:
        linha()
        print("Email inválido!")
        linha()
        email = input("Digite o email: ")
        return email

def main ():
    while True:
        escolha=(int(input("1 - Adicionar | 2 - Listar | 3 - Procurar | 4 - Sair: ")))
        linha()
        if escolha == 1:
            adicionar()
        elif escolha == 2:
            listar()
        elif escolha == 3:
            procurar()
        elif escolha == 4:
            print('Fechando programa!')
            linha()
            break
        else:
            print('Informação inválida')

if __name__ == '__main__':
    main()
    