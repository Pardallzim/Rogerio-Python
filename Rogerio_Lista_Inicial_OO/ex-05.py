class Conta_corrente:
    def __init__(self, numero_conta:int, nome_correntista:str, saldo_conta=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo_conta = saldo_conta

    def alterar_nome(self):
        self.nome_correntista =str(input("Digite o Nome do Correntista: "))
    
    def depositar(self):
        deposito =float(input("Digite o valor do deposito: "))
        self.saldo_conta += deposito

    def sacar(self):
        saque =float(input("Digite o valor do saque: "))
        self.saldo_conta += saque

