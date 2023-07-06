#  Uma empresa deseja controlar a quantidade de produtos em seu estoque.
#  Crie uma classe chamada Estoque que represente um produto em estoque.
#  O construtor da classe deve receber o nome do produto e a quantidade inicial em estoque.
# A classe Estoque deve ter métodos para realizar as seguintes operações:
# Adicionar unidades ao estoque: esse método deve receber a quantidade de unidades a serem adicionadas
# e atualizar a quantidade em estoque.
# Vender unidades do estoque: esse método deve receber a quantidade
# de unidades a serem vendidas e atualizar a quantidade em estoque.
# Verificar a quantidade atual em estoque: esse método deve retornar a
# quantidade atual de unidades em estoque.
# Crie três objetos da classe Estoque, cada um representando um produto diferente.
# Em seguida, chame os métodos para adicionar unidades, vender unidades e verificar
# a quantidade atual em estoque para cada um dos produtos criados.

from biblioteca import libs

class Estoque:
    def __init__(self, nomeProduto, quantidade):
        self.nomeProduto = nomeProduto
        self.quantidade = quantidade

    def adicionarQuantidade(self):
        qtd = libs.lerInt('Quantidade que deseja adicionar: ')
        if qtd > 0:
            self.quantidade += qtd
            print(f'Sua nova quantidade é de {self.quantidade}')
        else:
            print('Sua quantidade deve ser maior que 0')

    def venderQuantidade(self):
        vender = libs.lerInt('Quanto deseja comprar? ')
        if self.quantidade > 0:
            if vender > self.quantidade:
                print('Oops! Parece que você não tem estoque sucifiente para comprar essa quantidade!')
                print(f'Só temos {self.quantidade} em estoque!')
            else:
                self.quantidade -= vender
                print(f'Produto vendido!Estoque atualizado para {self.quantidade}')
        else:
            print('Ops! Não temos mais estoque desse produto!')

    def verificarQuantidade(self):
        if self.quantidade > 0:
            print(f'Seu estoque de {self.nomeProduto} é de {self.quantidade} produtos')
        else:
            print(f'Ops! Estamos sem estoque para esse produto')


produto1 = Estoque('Celular', 5)
produto1.adicionarQuantidade()
produto1.venderQuantidade()
produto2 = Estoque('Carregador', 8)
produto2.venderQuantidade()
produto3 = Estoque('Notebook', 2)
produto3.verificarQuantidade()