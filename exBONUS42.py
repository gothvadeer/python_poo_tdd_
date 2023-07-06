# Tarefa: Crie uma classe chamada Venda para representar uma venda de produtos.
# A classe deve ter os seguintes atributos:
# codigo (int): representa o código da venda.
# produtos (list): uma lista de produtos vendidos na venda.
# Crie uma lista de objetos Venda para representar as vendas realizadas
# pela empresa. Adicione algumas vendas fictícias à lista,
# definindo seus códigos e os produtos vendidos em cada uma delas.
# Implemente os seguintes métodos na classe Venda:
# calcular_valor_total(): calcula o valor total da venda somando o preço de cada produto vendido.
# exibir_detalhes(): exibe os detalhes da venda, incluindo o código e os produtos vendidos.
# Utilizando a biblioteca csv, escreva as informações das vendas em um arquivo CSV chamado
# "vendas.csv", apresentando o código da venda e os produtos vendidos em cada uma delas.
# Utilizando a biblioteca jsonpickle, escreva a lista de objetos Venda em um arquivo JSONPICKLE
# chamado "vendas.pickle".
import jsonpickle
from csv import writer
valor_total = []
class Venda:
    def __init__(self, codigo, produtos, valor):
        self.__codigo = codigo
        self.__produtos = produtos
        self.__valor = valor

    @property
    def codigo(self):
        return self.__codigo

    @property
    def produtos(self):
        return self.__produtos

    @property
    def valor(self):
        return self.__valor

    def calcular_valor_total(self):
        for valor in self.valor:
            valor_total.append(valor)
        return f'Valor total: R$ {sum(valor_total):.2f}'

    def exibir_detalhes(self):
        print(f'Código: {self.codigo}')
        for i in range(len(self.produtos)):
            produto = self.produtos[i]
            valor = self.valor[i]
            print(f'Produto: {produto}\n'
                  f'Valor: R$ {valor:.2f}')


produto = Venda(1234, ['Vassoura', 'Camisa Polo', 'Caneta Bic'], [12.88, 21.90, 1.99])
produto.exibir_detalhes()
print(produto.calcular_valor_total())


with open('vendas.csv', 'w', encoding='utf-8', newline='') as csvfile:
    escrita = writer(csvfile)
    escrita.writerow(['Código','Produtos','Preços'])
    escrita.writerow([produto.codigo, produto.produtos, produto.valor])

with open('vendas.pickle', 'w') as jsonfile:
    jsonfile.write(jsonpickle.encode(produto))
    