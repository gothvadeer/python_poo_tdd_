#  exercício para gerenciamento de uma loja de eletrônicos:
# 1 - Faça um programa para gerenciar uma loja de eletrônicos.
# O programa deve ter um menu com as seguintes opções:
# a) Cadastrar produto: o usuário deverá informar o nome do produto,
# o preço unitário e a quantidade em estoque. Essas informações devem ser armazenadas
# em um arquivo chamado "produtos.txt".
# b) Consultar produto: o usuário deverá informar o nome do produto e o programa deverá exibir
# o preço unitário e a quantidade em estoque.
# c) Listar produtos: o programa deverá exibir a lista de todos os produtos cadastrados,
# juntamente com seus preços unitários e quantidades em estoque.
# d) Vender produto: o usuário deverá informar o nome do produto e a
# quantidade vendida. Se a quantidade em estoque for suficiente, o programa deverá atualizar
# o arquivo "produtos.txt" com a nova quantidade em estoque e exibir o valor total da venda.
# Caso contrário, o programa deverá exibir uma mensagem informando que não há estoque suficiente.
# e) Sair: encerra o programa.

from biblioteca import libs
from biblioteca.pacote1 import arquivo3

while True:
    libs.linha('\n[1] - CADASTRAR PRODUTO\n[2] - CONSULTAR PRODUTO\n[3] - LISTAR PRODUTOS\n'
               '[4] - VENDER PRODUTO\n[5] - SAIR')
    op = libs.lerInt('Qual opção?: ')
    if op == 1:
        arquivo3.cadastrar()
    elif op == 2:
        arquivo3.consultar()
    elif op == 3:
        arquivo3.listar()
    elif op == 4:
        arquivo3.vender()
    elif op == 5:
        break
    elif op > 5:
        print('Erro, escolha uma das opções acima')

