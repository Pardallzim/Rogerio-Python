class Conta_corrente:
    def __init__(self, numero_conta:int, nome_correntista:str, saldo_conta=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo_conta = saldo_conta

    def alterar_nome(self, novo_nome):
        self.nome_correntista = novo_nome
    
    def depositar(self, deposito):
        self.saldo_conta += deposito

    def sacar(self, saque):
        if saque <= self.saldo_conta:
            self.saldo_conta -= saque
        else:
            print("!!!Saldo insuficiente!!!")
    
    def __str__(self):
        return f"Eu sou o {self.nome_correntista} dono da conta {self.numero_conta} e  tenho R${self.saldo_conta} na conta."


numero_conta =int(input("Digite o número da conta: "))
nome =str(input("Digite o nome do correntista: "))
saldo =float(input("Digite o saldo da conta: "))

conta = Conta_corrente(numero_conta, nome, saldo)
print(conta)
novo_nome =str(input("Digite o Nome do Correntista: "))
conta.alterar_nome(novo_nome)
print(conta)
deposito =float(input("Digite o valor do deposito: "))
conta.depositar(deposito)
print(conta)
saque =float(input("Digite o valor do saque: "))
conta.sacar(saque)
print(conta)
saque2 =float(input("Digite o valor do saque: "))
conta.sacar(saque2)
print(conta)