# Você está desenvolvendo um sistema de gerenciamento de pedidos para uma pizzaria.
# Os pedidos são registrados em um arquivo chamado "pedidos.csv".
# Cada linha do arquivo contém as seguintes informações separadas por vírgulas:
# número do pedido, nome do cliente, sabor da pizza e valor total do pedido.
# Sua tarefa é criar um programa em Python que leia o arquivo "pedidos.csv" e
# identifique os pedidos que possuem um valor total acima de R$50,00. Em seguida,
# exiba o número do pedido, nome do cliente e valor total desses pedidos na tela.
# Além disso, a pizzaria recebeu um novo pedido e você precisa atualizar o arquivo "pedidos.csv".
# Adicione as seguintes informações no arquivo:
# Número do pedido: 1011
# Nome do cliente: João da Silva
# Sabor da pizza: Calabresa
# Valor total: R$42,90
# Após a atualização, leia novamente o arquivo e exiba o número do pedido, nome do cliente e valor total
# de todos os pedidos, incluindo o novo pedido adicionado.
from csv import reader
from csv import writer

with open('pedidos.csv', encoding='utf-8') as pedidos:
    leitura = reader(pedidos)
    next(leitura)
    print(f'Pedidos que custam mais que $ 50: \n')
    for linha in leitura:
        valor = float(linha[3])
        if valor > 50:
            print(f'Número do pedido: {linha[0]}\n'
                  f'Nome do cliente: {linha[1]}\n'
                  f'Sabor da pizza: {linha[2]}\n'
                  f'Valor total: R$ {valor}')
with open('pedidos.csv', 'a+', encoding='utf-8', newline='') as pedidos:
    escrita = writer(pedidos)
    escrita.writerow(['1011', 'João da Silva', 'Calabresa', '42.0'])
    pedidos.seek(0)
    leitura = reader(pedidos)
    next(leitura)
    print('=*'*30)
    for linha in leitura:
        print(f'Número do pedido: {linha[0]}\n'
              f'Nome do cliente: {linha[1]}\n'
              f'Sabor da pizza: {linha[2]}\n'
              f'Valor total: R$ {linha[3]}')
        print('~'*20)
