# use Assertions no código abaixo


class ContaCorrente:
    def __init__(self, nome, num_conta, saldo=0.0):
        self.__nome = nome
        self.__num_conta = num_conta
        self.__saldo = saldo

    @property
    def nome(self):
        return self.__nome
    @property
    def saldo(self):
        return self.__saldo
    @property
    def num_conta(self):
        return self.__num_conta

    def deposito(self, valor):
        self.__saldo = self.__saldo + valor
    def saque(self,valor):
        self.__saldo = self.__saldo - valor

pessoa = ContaCorrente('Sandro',12345)
pessoa2 = ContaCorrente('Vanessa',67891,500.0)
pessoa1 = 'oi'
assert isinstance(pessoa, ContaCorrente), 'Não pertence a Classe'
assert isinstance(pessoa1, ContaCorrente), 'Não pertence a Classe'