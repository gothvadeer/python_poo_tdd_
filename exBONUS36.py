# Crie uma superclasse chamada 'Animal' que possui os atributos nome,
# idade e som. Ela também possui um método chamado 'emitir_som' que imprime o som do animal.
# Construa a classe filha 'Cachorro' que herda de 'Animal'. Ela possui um atributo
# adicional chamado 'raca' e um método chamado 'abanar_rabo' que imprime uma mensagem
# indicando que o cachorro está abanando o rabo.
# Crie outra classe filha chamada 'Gato' que também herda de 'Animal'.
# Ela tem um atributo adicional chamado 'cor' e um método chamado 'arranhar_sofa'
# que imprime uma mensagem indicando que o gato está arranhando o sofá.


class Animal:
    def __init__(self, nome, idade, som):
        self.__nome = nome
        self.__idade = idade
        self.__som = som
    @property
    def nome(self):
        return self.__nome
    @property
    def idade(self):
        return self.__idade
    @property
    def som(self):
        return self.__som

    def emitir_som(self):
        print(self.__som)


class Cachorro(Animal):
    def __init__(self, nome, idade, som, raca):
        super().__init__(nome, idade, som)
        self.__raca = raca

    def abanar_rabo(self):
        print('Estou abanando o rabo...')

    def emitir_som(self):
        return self.som

    def __repr__(self):
        if self.idade == 1:
            print(f'Olá! Eu sou um cachorro, sou da raça {self.__raca}\n'
                  f'meu nome é {self.nome}\n'
                  f'e tenho {self.idade} ano.')
        else:
            print(f'Olá! Eu sou um cachorro, sou da raça {self.__raca}\n'
              f'meu nome é {self.nome}\n'
              f'e tenho {self.idade} anos.')

class Gato(Animal):
    def __init__(self, nome, idade, som, cor):
        super().__init__(nome, idade, som)
        self.__cor = cor

    def arranhar_sofa(self):
        print('Eu estou arranhando o sofá...')

    def emitir_som(self):
        return self.som

    def __repr__(self):
        if self.idade == 1:
            print(f'Olá, eu sou um gato, meu nome é {self.nome}\n'
                  f'sou da cor {self.__cor} e tenho {self.idade} ano.')
        else:
            print(f'Olá, eu sou um gato, meu nome é {self.nome}\n'
                  f'sou da cor {self.__cor} e tenho {self.idade} anos.')


gato = Gato('Manda Chuva', 2, 'miaaau miaau', 'preta')
gato.__repr__()
print(gato.emitir_som())
gato.arranhar_sofa()
print(gato.emitir_som())
cachorro = Cachorro('Spike', 1, 'auauauu', 'vira-lata')
print(cachorro.emitir_som())
cachorro.__repr__()
cachorro.abanar_rabo()
