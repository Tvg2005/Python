import random
import os
from time import sleep


def add_car():
    global qtd_operacao, total_operacao, total_compra, qtd_carrinho, parar
    peso = 0
    chave = ""
    mult = 0
    produto = ""
    if adicionar == "1":
        chave = "alface"
        mult = 0.003
        produto = produto1
    elif adicionar == "2":
        chave = "tomate"
        mult = 0.012
        produto = produto2
    elif adicionar == "3":
        chave = "abacaxi"
        mult = 0.010
        produto = produto3
    elif adicionar == "4":
        chave = "melancia"
        mult = 0.002
        produto = produto4
    elif adicionar == "5":
        chave = "batata"
        mult = 0.006
        produto = produto5
    elif adicionar == "0":
        print("Nenhum produto foi adicionado!")
    if chave != "":
        qtd_carrinho = int(input(f"Insira a quantidade de {chave} a ser adicionado ao carrinho: "))
        linha()
        if qtd_carrinho > produto["Quantidade em estoque (UN)"]:
            print(f"Quantidade de produto indisponivel!")
            parar += 1
        else:
            produto["Quantidade em estoque (UN)"] = produto["Quantidade em estoque (UN)"] - qtd_carrinho
            print(f"Será escolhido por nossos vendedores {qtd_carrinho} unidades de {chave}!")
            linha()
            for k in range(qtd_carrinho):
                if adicionar == "1":
                    peso = random.randint(250, 350)
                elif adicionar == "2":
                    peso = random.randint(200, 300)
                elif adicionar == "3":
                    peso = random.randint(700, 900)
                elif adicionar == "4":
                    peso = random.randint(900, 1100)
                elif adicionar == "5":
                    peso = random.randint(70, 150)
                carrinho.append(f"{chave} com peso {peso}")
                if chave[-1] == "a":
                    print(f"Peso da {chave} escolhido (Gramas): {peso}")
                else:
                    print(f"Peso do {chave} escolhido (Gramas): {peso}")
                qtd_operacao += 1
                total_operacao += peso * mult
            linha()
            print("Produtos inseridos ao carrinho com sucesso!")
            total_compra += total_operacao


def abastecer():
    global saldo, gasto
    key = ""
    price = 0
    produto = ""
    if abastecimento == "1":
        key = "alface"
        price = 1.5
        produto = produto1
    elif abastecimento == "2":
        key = "tomate"
        price = 9
        produto = produto2
    elif abastecimento == "3":
        key = "abacaxi"
        price = 7
        produto = produto3
    elif abastecimento == "4":
        key = "melancia"
        price = 1
        produto = produto4
    elif abastecimento == "5":
        key = "batata"
        price = 3.5
        produto = produto5
    print(f"O estabelecimento possui {saldo} R$ de saldo")
    print(f"Preço kg {key} do fornecedor = {price}R$")
    qtd_abastecimento = int(input("Quantos kg deseja reabastecer: "))
    linha()
    confirmacao = input(f"Deseja confirmar a compra de {qtd_abastecimento} KGs de {key} com preço de"
                        f" {price}R$ cada? (1-Sim/2-Não): ")
    linha()
    if confirmacao == "1":
        conta = qtd_abastecimento * price
        if conta <= saldo:
            produto["Quantidade em estoque (UN)"] = produto["Quantidade em estoque (UN)"] + qtd_abastecimento
            print(f"Produto abastecido com sucesso!")
            print(f"Quantidade em estoque de {key} atual (UN):",
                  produto["Quantidade em estoque (UN)"])
            saldo -= conta
            gasto += conta
            print(f"Saldo depois da compra = {saldo}")
            sleep(5)
            os.system("cls")
        else:
            print(f"Saldo insuficiente! Saldo total = {saldo}")
    else:
        print("Abastecimento cancelado!")


def escrever():
    global arq
    arq = open("dados_clientes.txt", "a+")
    arq.write("Dados do cliente:")
    arq.write(f"\nNome: {nome}\nCPF: {cpf}\nEndereço: {endereco}\nValor da compra: {total_compra:.2f}")
    arq.write(f"\nCartão: {cartao}\nValidade do cartão: {validade}\n{'-' * 75}")


def retirada():
    if "alface" in carrinho[retirar_num - 1]:
        produto1["Quantidade em estoque (UN)"] = produto1["Quantidade em estoque (UN)"] + 1
    elif "tomate" in carrinho[retirar_num - 1]:
        produto2["Quantidade em estoque (UN)"] = produto2["Quantidade em estoque (UN)"] + 1
    elif "abacaxi" in carrinho[retirar_num - 1]:
        produto3["Quantidade em estoque (UN)"] = produto3["Quantidade em estoque (UN)"] + 1
    elif "melancia" in carrinho[retirar_num - 1]:
        produto4["Quantidade em estoque (UN)"] = produto4["Quantidade em estoque (UN)"] + 1
    elif "batata" in carrinho[retirar_num - 1]:
        produto5["Quantidade em estoque (UN)"] = produto5["Quantidade em estoque (UN)"] + 1


def linha():
    print("-" * 75)


def print_produto():
    linha()
    global i
    for i in produto1:
        print(i, produto1[i])
    linha()
    for i in produto2:
        print(i, produto2[i])
    linha()
    for i in produto3:
        print(i, produto3[i])
    linha()
    for i in produto4:
        print(i, produto4[i])
    linha()
    for i in produto5:
        print(i, produto5[i])


produto1 = {
    "Produto 1:": "Alface",
    "Preço kg": 3,
    "Quantidade em estoque (UN)": 20,
}

produto2 = {
    "Produto 2:": "Tomate",
    "Preço kg": 12,
    "Quantidade em estoque (UN)": 30,
}

produto3 = {
    "Produto 3:": "Abacaxi",
    "Preço kg": 10,
    "Quantidade em estoque (UN)": 10,
}

produto4 = {
    "Produto 4:": "Melancia",
    "Preço kg": 2,
    "Quantidade em estoque (UN)": 10,
}

produto5 = {
    "Produto 5:": "Batata",
    "Preço kg": 6,
    "Quantidade em estoque (UN)": 50,
}
# Adicionar novos produtos, criar protudo, adicionar no def - print_produto, retirada, abastecer, add_car
saldo = 1000
password = "Thiagodev2023"
sair = False
carrinho = []
gasto = 0
parar = 0
qtd_carrinho = 0
qtd_operacao = 0
total_operacao = 0
total_compra = 0
arq = ""
lucro = 0
ganho = 0
while not sair:
    linha()
    print("Loja Aoba - Frutas e Verduras!")
    linha()
    admin = int(input("Insira [1] - Aba Cliente e [2] - Aba de administrador [3] - Sair: "))
    linha()
    tentativas = 3
    if admin == 1:
        print("Operações possiveis: [1] - Ver produtos da loja [2] - Ver o carrinho [3] - Finalizar compra "
              "[4] - Deixar sugestões")
        linha()
        escolha_cliente = input("Qual operação deseja realizar: ")
        if escolha_cliente == "1":
            print_produto()
            linha()
            adicionar = input("Digite o numero do produto que deseja adicionar ao carrinho [0] - Nenhum: ")
            linha()
            check_add = "012345"
            if adicionar in check_add:
                add_car()
                if parar == 1:
                    continue
            else:
                print("Código de produto não reconhecido!")
        elif escolha_cliente == "2":
            linha()
            print("Carrinho: ")
            for i in range(len(carrinho)):
                print(f"{i + 1} {carrinho[i]}")
            print(f"Preço total: {total_compra:.2f}")
            linha()
            retirar = input("Deseja retirar algum produto? [S]/[N]: ").lower()
            if retirar == "s":
                linha()
                qtd_retirar = int(input("Quantos produtos deseja retirar: "))
                linha()
                for i in range(qtd_retirar):
                    retirar_num = int(input("Digite o numero do produto que deseja retirar: "))
                    linha()
                    retirada()
                    carrinho.pop(retirar_num - 1)
                    print("Carrinho: ")
                    for j in range(len(carrinho)):
                        print(f"{j + 1} {carrinho[j]}")
                    linha()
                print("Produtos retirados com sucesso!")
        elif escolha_cliente == "3":
            linha()
            print("Carrinho: ")
            for i in range(len(carrinho)):
                print(f"{i + 1} {carrinho[i]}")
            print(f"Preço total: {total_compra:.2f}")
            linha()
            confirm = input("Deseja continuar para o pagamento [S]/[N]: ").lower()
            linha()
            if confirm == "s":
                pagamento = input("Qual a forma de pagamento [1] - Pix [2] - Débito [3] - Crédito: ")
                if pagamento == "1":
                    linha()
                    print("Forma de pagamento: Pix")
                    linha()
                    print(f"Fazer pix no valor {total_compra:.2f} para o cpf 026.167.141-32!")
                    nome = input("Insira o nome do comprador: ")
                    cpf = int(input("Insira o cpf do comprador: "))
                    endereco = input("Insira o endereço para entrega: ")
                    linha()
                    print(f"Obrigado pela preferência! Volte sempre!")
                    arq = open("dados_clientes.txt", "a+")
                    arq.write(f"\nNome: {nome}\nCPF: {cpf}\nEndereço: {endereco}\n"
                              f"Valor total da compra: {total_compra:.2f}\n{'-' * 75}")
                    saldo += total_compra
                    ganho += total_compra
                    total_compra = 0
                elif pagamento == "2":
                    linha()
                    print("Forma de pagamento: Débito")
                    linha()
                    cartao = int(input("Insira o número do cartão: "))
                    cvc = int(input("Insira o codigo de 3 digitos do cartão (CVC): "))
                    nome = input("Insira o nome do titular do cartão: ")
                    validade = input("Insira a data de vencimento do cartão: ")
                    cpf = int(input("Insira o cpf do comprador: "))
                    endereco = input("Insira o endereço para entrega: ")
                    linha()
                    print(f"Obrigado pela preferência! Volte sempre!")
                    escrever()
                    saldo += total_compra
                    ganho += total_compra
                    total_compra = 0
                elif pagamento == "3":
                    linha()
                    print("Forma de pagamento: Crédito")
                    linha()
                    cartao = int(input("Insira o número do cartão: "))
                    cvc = int(input("Insira o codigo de 3 digitos do cartão (CVC): "))
                    nome = input("Insira o nome do titular do cartão: ")
                    validade = input("Insira a data de vencimento do cartão: ")
                    cpf = int(input("Insira o cpf do comprador: "))
                    endereco = input("Insira o endereço para entrega: ")
                    linha()
                    print(f"Obrigado pela preferência! Volte sempre!")
                    escrever()
                    saldo += total_compra
                    ganho += total_compra
                    total_compra = 0
                else:
                    print("Opção de pagamento não reconhecida!")
            else:
                print("Pagamento cancelado!")
        elif escolha_cliente == "4":
            linha()
            sugestao = input("Deixe a sua sugestão/avaliação para melhora da loja: ")
            sugest = open("sugestao.txt", "a+")
            sugest.write(f"{sugestao}\n")
            print("Avaliação anotada!")
            print(f"Obrigado pela preferência!Volte sempre!")
        else:
            print("Escolha não reconhecida!")
    elif admin == 2:
        for i in range(3):
            senha = input("Insira a senha para liberar o acesso de admin: ")
            if senha == password:
                break
            else:
                tentativas -= 1
                print(f"Senha incorreta. Tentativas restantes = {tentativas}")
                linha()
        if tentativas == 0:
            print("A senha inserida incorretamente três vezes.\nAcesso negado!")
            linha()
            sair = True
        else:
            linha()
            print("Acesso autorizado!")
            print("Operações possiveis: [1 - Verificar estoque] [2 - Reabastecer estoque] [3 - Alterar senha adm]"
                  " [4 - Verificar saldo] [5] - Ler sugestões")
            linha()
            escolha_adm = input("Qual operação deseja realizar: ")
            if escolha_adm == "1":
                print_produto()
            elif escolha_adm == "2":
                print("Produtos:\n1 - Alface\n2 - Tomate\n3 - Abacaxi\n4 - Melancia\n5 - Batata")
                linha()
                abastecimento = input("Qual produto deseja reabastecer: ").lower()
                linha()
                check_abastecimento = "12345"
                if abastecimento in check_abastecimento:
                    abastecer()
                else:
                    print(f"Produto não reconhecido!")
            elif escolha_adm == "3":
                caracteres_fortes = "!@#$%^&*()[]`-=+_{}\|;:,<.>/?"
                tentativa_recriacao = 3
                for i in range(3):
                    checagem = input("Insira a senha atual: ")
                    if checagem == password:
                        print("Senha correta!")
                        linha()
                        break
                    else:
                        tentativa_recriacao -= 1
                        print(f"Senha incorreta. Tentativas restantes = {tentativa_recriacao}")
                        linha()
                while True:
                    senha_nova = input("Digite a nova senha: ")
                    linha()
                    if caracteres_fortes not in senha_nova or len(senha_nova) < 8:
                        print("Senha fraca!")
                        confirm_senha = input("Deseja continuar com a senha fraca?(S/N): ").lower()
                        linha()
                        if confirm_senha == "s":
                            print(f"Senha anterior: {password}\nSenha atual: {senha_nova}")
                            password = senha_nova
                            sleep(4)
                            os.system("cls")
                            break
                        else:
                            continue
                    else:
                        print("Senha forte!")
                        confirm_senha = input(f"Deseja confirmar a troca de senha?(S/N): ").lower()
                        linha()
                        if confirm_senha == "s":
                            print(f"Senha anterior: {password}\nSenha atual: {senha_nova}")
                            password = senha_nova
                            sleep(4)
                            os.system("cls")
                            break
                        else:
                            continue
            elif escolha_adm == "4":
                linha()
                print(f"Saldo da loja: {saldo}")
                print(f"Os gastos da loja foram: {gasto}")
                print(f"Os ganhos da loja foram: {ganho}")
                print(f"O lucro da loja foi: {ganho - gasto}")
            elif escolha_adm == "5":
                arq = open("sugestao.txt", "r")
                line = arq.readlines()
                for i in line:
                    print(i)
                limpar = input("Deseja limpar a lista de sugestão [S]/[N]: ").lower()
                if limpar == "s":
                    arq = open("sugestao.txt", "w+")
                    arq.write("Lista de sugestoes:\n")
                print("Lista limpa")
            else:
                print("Escolha não reconhecida!")
    elif admin == 3:
        exit()
    else:
        print("Escolha não reconhecida!")
