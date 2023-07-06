# Você está desenvolvendo um sistema de gerenciamento de estoque para uma loja de eletrônicos.
# O estoque é representado por um arquivo chamado "produtos.csv". Cada linha do arquivo contém
# as seguintes informações separadas por vírgulas: nome do produto, preço unitário e quantidade em estoque.
# Sua tarefa é criar um programa em Python que leia o arquivo "produtos.csv" e identifique os produtos
# que estão com a quantidade em estoque abaixo de 10 unidades. Em seguida, exiba o nome e a quantidade
# atual desses produtos na tela.
# Além disso, a loja recebeu uma nova remessa de produtos e você precisa atualizar o estoque.
# Adicione as seguintes informações no arquivo "produtos.csv":
# Produto: Fone de Ouvido Bluetooth
# Preço: 99.99
# Quantidade: 20
# Após a atualização, leia novamente o arquivo e exiba o nome,
# preço e quantidade atual de todos os produtos, incluindo o novo item adicionado.
from csv import reader
from csv import writer

with open('produtos.csv', encoding='utf-8') as arq:
    leitura = reader(arq)
    next(arq)
    print(f'Produtos com menos de 10 quantidades no estoque: \n')
    for linha in leitura:
        quantidade = int(linha[2])
        if quantidade < 10:
            print(f' ==> {linha[0]} tem apenas {linha[2]} quantidades no estoque')
print('=*'*40)
with open('produtos.csv', 'a+', encoding='utf-8', newline='') as arq:
    escrita = writer(arq)
    escrita.writerow(['Fone de ouvido Bluetooth', '99.99', '20'])
    arq.seek(0)
    leitura = reader(arq)
    next(leitura)
    for linha in leitura:
        print(f'Produto: {linha[0]}\n'
              f'Preço: R$ {linha[1]}\n'
              f'Quantidade: {linha[2]}')
        print('~'*20)