# Atividade: Cálculo de Lucro Anual
# Crie uma classe chamada Produto para representar um produto vendido por uma empresa.
# A classe deve ter os seguintes atributos:
# nome (string): representa o nome do produto.
# custo (float): representa o custo unitário do produto.
# preco (float): representa o preço de venda unitário do produto.
# Crie uma lista de objetos Produto para representar os produtos vendidos pela empresa.
# Preencha essa lista com alguns produtos fictícios, definindo seus nomes, custos e preços de venda.
# Calcule o lucro anual da empresa com base nos dados dos produtos. Para cada produto,
# multiplique a diferença entre o preço de venda e o custo pelo número de unidades vendidas no ano.
# Some o lucro de todos os produtos para obter o lucro anual da empresa.
# Escreva o lucro anual em um arquivo CSV chamado "lucro_anual.csv",
# apresentando o ano e o valor do lucro em milhões.
# Utilizando a biblioteca jsonpickle, escreva a lista de objetos Produto em um arquivo
# JSONPICKLE chamado "pro.pickle".
from csv import reader, writer
import jsonpickle


class Produto:
    def __init__(self, nome, custo, preco, unidade_vendida):
        self.__nome = nome
        self.__custo = custo
        self.__preco = preco
        self.__unidade_vendida = unidade_vendida

    @property
    def nome(self):
        return self.__nome
    @property
    def custo(self):
        return self.__custo
    @property
    def preco(self):
        return self.__preco
    @property
    def unidade_vendida(self):
        return self.__unidade_vendida


produtos = [Produto('Vassoura', 23.87, 40.0, 1000),
            Produto('Notebook', 2000.00, 5000.00, 3000),
            Produto('Celular', 1000.0, 2458.00, 10000),
            Produto('Mesa', 345.00, 1000.0, 587)]

lucro = []
for produto in produtos:
    diferenca = produto.preco - produto.custo
    valor_total = diferenca * produto.unidade_vendida
    lucro.append(valor_total)


with open('lucro_anual.csv', 'w+', encoding='utf-8', newline='') as csvfile:
    escrita = writer(csvfile, delimiter=':')
    escrita.writerow(['Lucro Anual (milhões)'])
    escrita.writerow(['R$', sum(lucro)])
    csvfile.seek(0)
    leitura = reader(csvfile)
    next(leitura)
    for linha in leitura:
        print(f'O lucro anual foi de {linha[0]}')

with open('pro.pickle', 'w') as jsonpickleFile:
    jsonpickleFile.write(jsonpickle.encode(produtos))

