def linha():
    print("-" * 75)

class Titular(object):
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def get_sobrenome(self):
        return self.sobrenome
    
    def get_nome(self):
        return self.nome

    def get_cpf(self):
        return self.cpf

    def get_nome_completo(self):
        return f"{self.nome} {self.sobrenome}"

    def set_nome(self, novo_nome):
        self.nome = novo_nome

class Conta:
    def __init__(self, num_conta, saldo, vl_limite, obj_titular):
        self.num_conta = num_conta
        self.saldo = saldo
        self.vl_limite = vl_limite
        self.obj_titular = obj_titular

    def get_num_conta(self):
        return self.num_conta
    
    def get_saldo(self):
        return self.saldo
    
    def get_vl_limite(self):
        return self.vl_limite
    
    def extrato_reduzido(self):
        return f"Num conta: {self.num_conta}/nSaldo: {self.saldo}"
    
    def extrato_normal(self):
        titular_info = self.obj_titular
        return f"Nome: {titular_info.get_nome()}\nSobrenome: {titular_info.get_sobrenome()}\nCpf: {titular_info.get_cpf()}\nNum Conta: {self.get_num_conta()}\nSaldo: {self.get_saldo()}"

    def dados_titular(self):
        titular_info = self.obj_titular
        return f"Nome: {titular_info.get_nome()}\nSobrenome: {titular_info.get_sobrenome()}\nCpf: {titular_info.get_cpf()}"
    
    def deposito(self, aumento):
        self.saldo += aumento

    def saque(self, vl_saque):
        if vl_saque > self.saldo:
            print("Saldo insuficiente!")
        else:
            self.saldo -= vl_saque
    
    def tranferencia(self, vl_tranfer, obj):
        if vl_tranfer > self.saldo:
            print("Saldo insuficiente!")
        else:
            self.saldo -= vl_tranfer
            obj.saldo += vl_tranfer
    
    def rsco(self):
        if self.saldo <= 500:
            return "E"
        elif self.saldo <= 1000 and self.saldo > 500:
            return "D"
        elif self.saldo <= 1500 and self.saldo > 1000:
            return "C"
        elif self.saldo <= 2000 and self.saldo > 1500:
            return "B"
        elif self.saldo > 2000:
            return "A"
        
if __name__ == '__main__':
    titular1 = Titular("Thiago", "Venâncio", "026167141-32")
    conta1 = Conta("4431-045", 1000, 2000, titular1)
    print(f"Nome: {titular1.get_nome()}")
    print(f"Sobrenome: {titular1.get_sobrenome()}")
    print(f"Cpf: {titular1.get_cpf()}")
    linha()
    print(f"Nome: {conta1.obj_titular.get_nome()}")
    print(f"Sobrenome: {conta1.obj_titular.get_sobrenome()}")
    print(f"Cpf: {conta1.obj_titular.get_cpf()}")
    linha()
    print(conta1.extrato_normal())
    conta2 = Conta("4132-891", 3000, 5000, titular1)
    conta1.tranferencia(200, conta2)
    linha()
    print(f"Risco Cliente: {conta2.rsco()}")