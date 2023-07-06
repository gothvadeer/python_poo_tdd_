# - Crie uma SuperClasse chamada 'Pessoa' que recebe como atributos nome,
# cpf e salário. Após isso, construa a Classe Filha: 'Funcionario', que possui o
# método sem parâmetros chamado 'promocao', que apenas acrescenta 10% no
# salário a algum funcionário. Por sua vez, a classe 'Funcionario' deve ser
# Classe Mãe de outras duas classes: 'Gerente' e 'Estagiario', e ambos precisam
# ter o atributo 'codigo' em seu método construtor. Além disso, o gerente precisa
# do atributo 'numEstagiarios', representando a quantidade de funcionário que
# ele é responsável. Ainda, na classe gerente deve haver um método que
# possibilite a alteração do código dos estagiários, sendo que os estagiários não
# têm acesso a troca de codigo. Instancie 3 estagiários e 1 gerente. Dê
# promoção para os dois primeiros estagiários e para o gerente.
# Obs.: Utilize também um método mágico para representar as classes
# 'Estagiário' e 'Gerente', e propriedades para acessar os atributos de 'Pessoa'.

class Pessoa:
    def __init__(self, nome, cpf, salario):
        self.__nome = nome
        self.__cpf = cpf
        self.__salario = salario

    @property
    def nome(self):
        return self.__nome
    @property
    def cpf(self):
        return self.__cpf
    @property
    def salario(self):
        return self.__salario
    @salario.setter
    def salario(self, aumento):
        self.__salario = aumento


class Funcionario(Pessoa):
    def promocao(self):
        aumento = self.salario * 0.10
        self.salario += aumento
        return self.salario


class Gerente(Funcionario):
    def __init__(self, nome, cpf, codigo, salario, numEstagiarios, codEstagiario):
        super().__init__(nome, cpf, salario)
        self.__codigo = codigo
        self.__numEstagiarios = numEstagiarios
        self.__codEstagiario = codEstagiario

    def trocarCodEstagiarios(self, novoCodEstagiarios):
        self.__codEstagiario = novoCodEstagiarios
        print(f'O novo código é: {self.__codEstagiario}')

    def __repr__(self):
        print(f'Olá, meu nome é {self.nome}, sou o gerente!\n'
              f'Ganho: {self.salario} por mês')


class Estagiario(Funcionario):
    def __init__(self, nome, cpf, salario, codigo):
        super().__init__(nome, cpf, salario)
        self.__codigo = codigo

    def __repr__(self):
        print(f'Funcionário: {self.nome}\n'
              f'CPF: {self.cpf}\n'
              f'Código: {self.__codigo}\n'
              f'Salário: {self.salario}')


gerente = Gerente('Cleiton', 182734, '737446LHF', 15000, 3, 'FHBABJ637')
estagiario1 = Estagiario('Joao', 4477575, 1000, '18387BFD')
estagiario1.__repr__()
print('=*'*10)
gerente.trocarNumEstagiarios = 'BgagjjFF'
gerente.__repr__()
print('=*'*10)
estagiario1.promocao()
estagiario1.__repr__()

