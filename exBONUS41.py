# Crie uma classe chamada Produto para representar um produto em estoque.
# A classe deve ter os seguintes atributos:
# nome (string): representa o nome do produto.
# quantidade (int): representa a quantidade disponível em estoque.
# preco (float): representa o preço unitário do produto.
# Crie uma lista de objetos Produto para representar o estoque da empresa.
# Adicione alguns produtos fictícios à lista, definindo seus nomes,
# quantidades e preços correspondentes.
# Implemente os seguintes métodos na classe Produto:
# adicionar_estoque(quantidade): recebe a quantidade de produtos
# a serem adicionados ao estoque e atualiza a quantidade disponível.
# vender(quantidade): recebe a quantidade de produtos vendidos e atualiza
# a quantidade disponível, verificando se há estoque suficiente.
# calcular_valor_total(): calcula o valor total do estoque multiplicando
# a quantidade disponível pelo preço unitário de cada produto.
# exibir_estoque(): exibe as informações de todos os produtos no estoque,
# incluindo nome, quantidade e preço.
# Utilize a biblioteca csv para escrever as informações do estoque em um arquivo
# CSV chamado "estoque.csv", apresentando o nome, quantidade e preço de cada produto.
# Utilizando a biblioteca jsonpickle, escreva a lista de objetos Produto em um arquivo
# JSONPICKLE chamado "estoque.pickle"

import jsonpickle
from csv import writer

class Produto:
    def __init__(self, nome, quantidade, preco):
        self.__nome = nome
        self.__quantidade = quantidade
        self.__preco = preco

    @property
    def nome(self):
        return self.__nome
    @property
    def quantidade(self):
        return self.__quantidade
    @property
    def preco(self):
        return self.__preco

    def adiciona_estoque(self, quantidade):
        self.__quantidade += quantidade
        print(f'quantidade adicionada com sucesso')


    def vender(self, quantidade):
        if self.quantidade >= quantidade:
            self.__quantidade -= quantidade
            print(f'Produto vendido com sucesso!')
        else:
            print(f'Produto fora de estoque')


    def calcular_valor_total(self):
            print(self.quantidade * self.preco)

    def exibir_estoque(self):
            print(f'Produto: {self.nome}\n'
                  f'Quantidade: {self.quantidade}\n'
                  f'Preço: R$ {self.preco}')


produtos = [Produto('Vassoura', 1000, 23.5),
            Produto('Notebook', 3000, 5000.0),
            Produto('Celular', 10000, 3198),
            Produto('Mesa', 587, 827.88)]


with open('estoque.csv', 'w', encoding='utf-8', newline='') as csvfile:
    escrita = writer(csvfile)
    for produto in produtos:
        escrita.writerow([produto.nome, produto.quantidade, produto.preco])

with open('estoque.pickle', 'w') as jsonfile:
    jsonfile.write(jsonpickle.encode(produtos))