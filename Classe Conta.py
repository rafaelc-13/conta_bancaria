class Conta
    def __init__(self,numero,saldo,nome,tipo,limite):
        self.numero = numero
        self.saldo = saldo
        self.nome = nome
        self.status = False
        self.tipo = tipo
        self.limite = limite

    def depositar(self,valor):
        if self.status == False:
            print(f'{self.nome} não possui conta ativa.')
        else:
            if valor > 0:
                print(f'Saldo anterior = {self.saldo:.2f}. \n')
                self.saldo += valor
                print(f'Novo saldo é {self.saldo:.2f}')
            else:
                print ('Valor inválido para depósito.')

    def sacar(self,valor):
        if self.status == False:
            print(f'{self.nome} não possui conta ativa.')
        else:
            if valor <= self.saldo + self.limite:
                print(f'Saldo anterior = {self.saldo:.2f}. \n')
                self.saldo -= valor
                print(f'Novo saldo é {self.saldo:.2f}')
            else:
                print('Saldo insuficiente.')

    def ativarConta(self):
        if self.status == False:
            print(f'Conta ativada no nome de {self.nome}.')
            self.status = True
        else:
            print(f'{self.nome} já tem uma conta em seu nome de numero {self.numero}.')

    def verificarSaldo(self,):
        if self.status == False:
            print(f'{self.nome} não possui conta ativa.')
        else:
            if self.saldo >= 0:
                print(f'Saldo da conta é {self.saldo:.2f}')
