# Crie uma classe chamada Animal que represente um animal. O construtor da classe
# deve receber o nome do animal e a sua idade. A classe deve ter um método chamado
# fazer_som, que imprime o som do animal.

# Crie três objetos da classe Animal, cada um representando um animal diferente.
# Em seguida, chame o método fazer_som para cada um dos animais criados, exibindo
# o som que cada um deles faz.


class Animal:
    def __init__(self, nome_animal, idade):
        self.nome_animal = nome_animal.upper()
        self.idade = idade

    def fazer_som(self):
        if self.nome_animal == 'GATO':
            print('MIAAAU')
        elif self.nome_animal in ['CACHORRO']:
            print('AUAUAUAUAUAU')
        elif self.nome_animal in ['CABRA', 'OVELHA', 'BEZERRO', 'CARNEIRO']:
            print('BEEEEEERRR')
        elif self.nome_animal in ['BOI', 'VACA']:
            print('MUUUUUUUU')
        elif self.nome_animal in ['GALINHA', 'GALO']:
            print('COCORICÓ')
        else:
            print('Não sabemos o som desse animal')


animal1 = Animal('cabra', 2)
animal1.fazer_som()
animal2 = Animal('galinha', 3)
animal2.fazer_som()
animal3 = Animal('cachorro', 5)
animal3.fazer_som()
