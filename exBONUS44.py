# Crie uma classe chamada ContaBancaria que recebe no método construtor os seguintes parâmetros:
# titular (str) e saldo (float). Esses parâmetros devem ser atributos da classe ContaBancaria.
# Declare um método chamado depositar na classe ContaBancaria que recebe um parâmetro valor (float)
# e atualiza o saldo da conta bancária somando o valor depositado.
# Declare um método chamado sacar na classe ContaBancaria que recebe um parâmetro valor (float)
# e verifica se há saldo suficiente na conta para realizar o saque. Se houver saldo suficiente,
# atualize o saldo da conta subtraindo o valor sacado. Caso contrário, exiba a mensagem
# "Saldo insuficiente para saque".
# Crie uma classe filha de ContaBancaria chamada ContaPoupanca.
# Na classe ContaPoupanca, implemente o método rendimento_mensal que recebe um parâmetro taxa (float)
# e calcula o rendimento mensal da conta de acordo com a fórmula: rendimento = saldo * (taxa / 100).
# Crie uma classe filha de ContaBancaria chamada ContaCorrente.
# Na classe ContaCorrente, implemente o método verificar_cheque_especial que verifica se o saldo da conta
# está abaixo de zero e exibe a mensagem "Cheque especial utilizado" caso seja verdadeiro. Caso contrário,
# exibe a mensagem "Saldo positivo".
# Utilize doctests para fazer testes na classe ContaPoupanca e unittests na classe ContaCorrente.
# Utilize a metodologia TDD (Test-Driven Development) para desenvolver os testes primeiro e depois
# a implementação das classes.

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    def depositar(self, valor):
        """
        Função que deposita um valor na conta, aumentando o saldo do usuário se o valor for acima de 0
        caso contrário, retorna uma mensagem de desposito inválido
        >>> gabe = ContaBancaria('Gabriel', 100.0)
        >>> gabe.depositar(50.0)
        'R$ 150.00'
        """
        if valor >= 0:
            valor += self.saldo
            return f'R$ {valor:.2f}'
        else:
            print('Deposite um valor válido!')

    def sacar(self, valor):
        """
        Função que saca um valor na conta, subtraindo do saldo principal, caso o valor do saldo
        for menor que o valor do saque, caso contrário, envia uma mensagem de valor insuficiente
        >>> raquel = ContaBancaria('Raquel', 100.0)
        >>> raquel.sacar(50.0)
        'R$ 50.00'
        """
        if valor > 0:
            if self.saldo >= valor:
                self.__saldo -= valor
                return f'R$ {self.saldo:.2f}'
        else:
            print('Não há valor suficiente em sua conta!')


class ContaPoupanca(ContaBancaria):

    def __init__(self, titular, saldo):
        super().__init__(titular, saldo)

    def rendimento_mensal(self, taxa):
        """
        Função que calcula o rendimento mensal do usuário, retornando o valor total de rendimentos
        >>> heitor = ContaPoupanca('Heitor', 100.0)
        >>> heitor.rendimento_mensal(2.0)
        'R$ 2.00'
        """
        rendimento = self.saldo * (taxa / 100)
        return f'R$ {rendimento:.2f}'


class ContaCorrente(ContaBancaria):
    def __init__(self, titular, saldo):
        super().__init__(titular, saldo)

    def verificar_cheque_especial(self):
        """
        Função que verifica se o saldo da conta está abaixo de zero, se estiver
        exibe uma mensagem de cheque especial, caso contrário, uma de saldo positivo
        """
        if self.saldo < 0:
            return 'Cheque especial utilizado'
        else:
            return 'Saldo positivo'


