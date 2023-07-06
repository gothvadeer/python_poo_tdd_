# 1 - Crie uma superclasse chamada 'FormaGeometrica', que possui um método
# 'calcula_area' e recebe o nome de uma figura geométrica em seu método
# construtor. Após isso, crie duas subclasses ('Areaquadrado' e 'Areacirculo') que
# herdam de 'FormaGeométrica' e calculam a área de sua respectiva forma. O
# método nas Classes Filhas deve ter o nome 'calcula_area', igual em sua Classe
# Mãe.

class FormaGeometrica:
    def __init__(self, nome):
        self.__nome = nome

    def calcula_area(self):
        pass


class AreaQuadrado(FormaGeometrica):
    def __init__(self, lado):
        super().__init__('Quadrado')
        self.lado = lado

    def calcula_area(self):
        print(f'A área do quadrado é: {self.lado ** 2}')


class AreaCirculo(FormaGeometrica):
    def __init__(self, raio):
        super().__init__('Circulo')
        self.raio = raio

    def calcula_area(self):
        print(f'A área do circulo é: {3.141593 * (self.raio ** 2)}')

quadrado = AreaQuadrado(5)
quadrado.calcula_area()
circulo = AreaCirculo(3)
circulo.calcula_area()








