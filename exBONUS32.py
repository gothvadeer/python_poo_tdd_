# # Crie uma classe chamada Produto que represente um produto. O construtor da classe
# # deve receber o nome, preço e quantidade em estoque do produto. A classe deve ter
# # um método chamado calcular_total, que retorna o valor total em estoque do produto
# # multiplicando o preço pela quantidade.
# # Crie três objetos da classe Produto, cada um representando um produto diferente.
# # Em seguida, chame o método calcular_total para cada um dos produtos criados,
# # exibindo o valor total em estoque para cada um deles.

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_total(self):
       return self.preco * self.quantidade


produto1 = Produto('Escova de cabelo', 1.40, 5)
print(f'O valor total de {produto1.nome} é {produto1.calcular_total()}')
produto2 = Produto('Chapinha', 204, 1)
print(f'O valor total de {produto2.nome} é {produto2.calcular_total()}')
produto3 = Produto('Shampoo', 44, 10)
print(f'O valor total de {produto3.nome} é {produto3.calcular_total()}')

