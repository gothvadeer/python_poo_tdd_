# 1) Crie uma classe chamada Tatu que recebe em seu método construtor o
# nome dele, dentro dessa classe implemente os seguintes métodos:
# - comer: Retorna ‘Sou o NOME e estou comendo pizza’
# - beber: Retorna ‘Sou o NOME e estou bebendo suco’
# - cavar: Retorna ‘Sou o NOME e estou cavando sua grama’
# - acasalar: Retorna: ‘Sou o NOME e quero um filhote’
# Faça os testes para cada um dos métodos e crie dois objetos no setUp: Bola e
# Napoleão e use um ou outro para aplicar os testes. Além disso aplique o
# tearDown para apresentar a mensagem ‘Teste Concluido’.
# Observação: Utilize o método TDD.

class Tatu:
    def __init__(self, nome):
        self.__nome = nome

    def comer(self):
        return f'Sou o {self.__nome} e estou comendo pizza'

    def beber(self):
        return f'Sou o {self.__nome} e estou bebendo suco'

    def cavar(self):
        return f'Sou o {self.__nome} e estou cavando sua grama'

    def acasalar(self):
        return f'Sou o {self.__nome} e quero um filhote.'