    class Conta:
    def __init__(self,numero,saldo,nome,tipo,limite):
        self.numero = numero
        self.saldo = saldo
        self.nome = nome
        self.status = False
        self.tipo = tipo
        self.limite = limite
        self.saldo_devedor = 0

    def depositar(self,valor):
        if self.status == False:
            print(f'{self.nome} não possui conta ativa.')
        else:
            if valor > 0:
                if self.saldo_devedor > 0:
                    if self.saldo_devedor >= valor:
                        self.saldo_devedor -= valor
                        print(f'Você reduziu sua dívida em {valor:.2f}. Seu novo saldo devedor é {self.saldo_devedor: 2f}.')
                    else:
                        valor -= self.saldo_devedor
                        self.saldo_devedor = 0
                        self.saldo += valor
                        print(f'Saldo anterior = {self.saldo - valor:.2f} \n')
                        print(f'Novo saldo é {self.saldo:.2f}.')
                else:
                    print (f'Saldo anterior = {self.saldo:.2f}. \n')
                    self.saldo += valor
                    print(f'Novo saldo = {self.saldo:.2f}.')
            else:
                print('Valor de depósito inválido.')

    def sacar(self,valor):
        if self.status == False:
            print(f'{self.nome} não possui conta ativa.')
        else:
            if valor > self.saldo:
                if (self.saldo + sel.limite - self.saldo_devedor) >= valor:
                    self.saldo_devedor += valor - self.saldo
                    self.saldo = 0
                    print(f'Saldo devedor é {self.saldo_devedor:.2f}.')
                else:
                    print('Saldo insuficiente.')
            else:
                print(f'Saldo anterior = {self.saldo:.2f}')
                self.saldo -= valor
                print(f'Novo saldo é {self.saldo:.2f}')

    def ativarConta(self):
        if self.status == False:
            print(f'Conta ativada no nome de {self.nome}.')
            self.status = True
        else:
            print(f'{self.nome} já tem uma conta em seu nome de numero {self.numero}.')

    def verificarSaldo(self):
        if self.status == False:
            print(f'{self.nome} não possui conta ativa.')
        else:
            if self.saldo >= 0:
                print(f'Saldo da conta é {self.saldo:.2f}')
