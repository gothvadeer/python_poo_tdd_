#  Crie uma Classe Pessoa que recebe no método construtor: nome, idade, cpf
# e o tempo de trabalho como atributos de uma pessoa. Também, declare um
# método chamado aposentadoria e outro com o nome de salario_aposentadoria,
# ambos serão implementados pelas classes Filhas. Dica: Utilize os conceitos
# aprendidos em polimorfismo.
# Após isso, crie duas classes: Homem e Mulher, as duas sendo classes Filhas
# de Pessoa. Dentro da classe Homem desenvolva o método aposentadoria que
# irá testar se o objeto possui idade maior ou igual a 65 e um tempo de trabalho
# maior ou igual a 15 anos, caso positivo, retorne ‘Você pode se aposentar’, caso
# contrário ‘Ainda não atingiu os requisitos para se aposentar’. Também
# implemente o método salario_aposentadoria que irá testar se o objeto possui
# idade maior ou igual a 65 e um tempo de trabalho maior ou igual a 15 anos,
# caso positivo, calcule e retorne o sálario de direito pela seguinte equação:
# salário=1000+(tempode trabalho−15)∗200
# Caso contrário, retorne ‘Você não pode se aposentar’. Faça o mesmo
# procedimento da classe Homem, para a classe Mulher, porém ao invés da
# idade utilizada como comparação ser 65, faça com 60.
# Utilize Doctests para fazer testes na classe Homem e Unittests na classe
# Mulher. Utilize o método TDD

class Pessoa:
    def __init__(self, nome, idade, cpf, tempoTrabalho, salario):
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf
        self.__tempoTrabalho = tempoTrabalho
        self.__salario = salario

    @property
    def nome(self):
        return self.__nome
    @property
    def idade(self):
        return self.__idade
    @property
    def cpf(self):
        return self.__cpf
    @property
    def tempoTrabalho(self):
        return self.__tempoTrabalho
    @property
    def salario(self):
        return self.__salario

    def aposentadoria(self):
        raise NotImplementedError('Metódo especifico a critério da SubClass')

    def salario_aposentadoria(self):
        raise NotImplementedError('Metódo especifico a critério da SubClass')


class Homem(Pessoa):
    def __init__(self, nome, idade, cpf, tempoTrabalho, salario):
        super().__init__(nome, idade, cpf, tempoTrabalho, salario)

    def aposentadoria(self):
        """
        Função que retorna se o homem pode ou não se aposentar, caso não, retorna quanto tempo
        falta para a aposentadoria.
        >>> mike = Homem('Mike', 65, 88363678, 15, 1500)
        >>> mike.aposentadoria()
        Você poderá se aposentar!
        >>> kevin = Homem('Kevin', 65, 87393939, 12, 1500)
        >>> kevin.aposentadoria()
        Tem idade para se aposentar, mas não tem tempo de trabalho suficiente!
        >>> leo = Homem('Leo', 60, 9383748, 10, 1500)
        >>> leo.aposentadoria()
        Faltam 5 anos para você se aposentar!
        """
        if self.idade >= 65 and self.tempoTrabalho >= 15:
            print('Você poderá se aposentar!')
        elif self.idade >= 65 and self.tempoTrabalho < 15:
            print('Tem idade para se aposentar, mas não tem tempo de trabalho suficiente!')
        else:
            print(f'Faltam {65 - self.idade} anos para você se aposentar!')

    def salario_aposentadoria(self):
        """
        Função que irá calcular o salário de aposentadoria que o homem irá receber
        >>> mike = Homem('Mike', 65, 88363678, 17, 1500)
        >>> mike.salario_aposentadoria()
        R$ 1900.00
        """
        if self.idade >= 65 and self.tempoTrabalho >= 15:
            print(f'R$ {self.salario + (self.tempoTrabalho-15) * 200:.2f}')
        else:
            print(f'Ainda não tem os requisitos para se aponsentar')


class Mulher(Pessoa):
    def __init__(self, nome, idade, cpf, tempoTrabalho, salario):
        super().__init__(nome, idade, cpf, tempoTrabalho, salario)

    def aposentadoria(self):
        if self.idade >= 60 and self.tempoTrabalho >= 15:
            return 'Você poderá se aposentar!'
        elif self.idade >= 60 and self.tempoTrabalho < 15:
            return 'Tem idade para se aposentar, mas não tem tempo de trabalho suficiente!'
        else:
            return f'Faltam {60 - self.idade} anos para você se aposentar!'

    def salario_aposentadoria(self):
        if self.idade >= 60 and self.tempoTrabalho >= 15:
            return f'R$ {self.salario + (self.tempoTrabalho - 15) * 200:.2f}'
        else:
            return 'Ainda não tem os requisitos para se aponsentar'




