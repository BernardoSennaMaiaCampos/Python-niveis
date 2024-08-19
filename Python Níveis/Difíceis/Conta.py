from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, nome_cliente, numero_conta, pin):
        self.nome_cliente = nome_cliente
        self.numero_conta = numero_conta
        self.pin = pin
        self.saldo = 0.0
        self.movimentos = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.__registra(f'Depósito de R${valor:.2f}')
        else:
            print("Valor de depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            self.__registra(f'Saque de R${valor:.2f}')
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            print("Valor de saque deve ser positivo.")

    def __registra(self, movimento):
        self.movimentos.append(movimento)

    @abstractmethod
    def extrato(self):
        pass

class ContaPF(Conta):
    def __init__(self, nome_cliente, numero_conta, pin, cpf):
        super().__init__(nome_cliente, numero_conta, pin)
        self.cpf = cpf

    def extrato(self):
        print(f'Extrato da Conta PF')
        print(f'Cliente: {self.nome_cliente}')
        print(f'CPF: {self.cpf}')
        print(f'Número da Conta: {self.numero_conta}')
        print('Movimentos:')
        for movimento in self.movimentos:
            print(movimento)
        print(f'Saldo Atual: R${self.saldo:.2f}\n')

class ContaPJ(Conta):
    def __init__(self, nome_cliente, numero_conta, pin, cnpj):
        super().__init__(nome_cliente, numero_conta, pin)
        self.cnpj = cnpj

    def extrato(self):
        print(f'Extrato da Conta PJ')
        print(f'Cliente: {self.nome_cliente}')
        print(f'CNPJ: {self.cnpj}')
        print(f'Número da Conta: {self.numero_conta}')
        print('Movimentos:')
        for movimento in self.movimentos:
            print(movimento)
        print(f'Saldo Atual: R${self.saldo:.2f}\n')

# Testando o código
conta_pf = ContaPF('João Silva', '123456', '1234', '123.456.789-00')
conta_pf.depositar(1000)
conta_pf.sacar(200)
conta_pf.extrato()

conta_pj = ContaPJ('Empresa XYZ', '654321', '5678', '12.345.678/0001-00')
conta_pj.depositar(5000)
conta_pj.sacar(1500)
conta_pj.extrato()
