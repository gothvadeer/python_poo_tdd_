# 1 - Crie duas classes chamadas 'Homem' e 'Urso', que recebem apenas nome
# como parâmetro. Estas classes devem herdar de outras duas chamadas
# 'Carnivoros' e 'Herbivoros', que possuem dois métodos cada ('caçar_animal' e
# 'comer_carne' para 'Carnivoros', 'procurar_arvore' e 'comer_folhas' para
# 'Herbivoros') e herdam de uma Superclasse chamada 'Animal', na qual possui
# os métodos 'andar' e 'correr'. Por fim, instancie dois objetos, da classe 'Homem'
# e da classe 'Urso', e execute todos os métodos.
# Obs.: Crie um método para as classes 'Homem' e 'Urso' representando uma
# ação característica de cada, por exemplo ler um livro para o homem e hibernar
# para o urso


class Animal:
    def andar(self):
        print('Estou andando...')

    def correr(self):
        print('Estou correndo...')


class Carnivoro(Animal):

    def cacar_animal(self):
        print('Eu caço animais...')

    def comer_carne(self):
        print('Comendo carnes que eu cacei')


class Herbivoro(Animal):
    def procurar_arvore(self):
        print('Procurando árvores...')

    def comer_folhas(self):
        print('Comendo as folhas que achei...')


class Urso(Carnivoro, Herbivoro):
    def __init__(self, nome):
        super().__init__()
        self.__nome = nome

    @property
    def hibernar(self):
        return f'Olá, eu sou um urso, meu nome é... {self.__nome} e eu hiberno'


class Homem(Carnivoro, Herbivoro):
    def __init__(self, nome):
        super().__init__()
        self.__nome = nome

    @property
    def ler_livros(self):
        return f' Olá, eu sou humano, meu nome é... {self.__nome} e eu leio livros'




pessoa = Homem('José')
print(pessoa.ler_livros)
pessoa.andar()
pessoa.cacar_animal()
pessoa.comer_carne()
animal = Urso('Zé Coméia')
print(animal.hibernar)
animal.cacar_animal()
animal.procurar_arvore()