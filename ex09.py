# Criar um sistema de comando de uma loja de jogos. O programa deve
# conter pelo menos 6 listas: uma indicando quais jogos estão disponíveis para
# venda, uma para mostrar o preço de cada jogo, uma para mostrar a quantidade
# de jogos disponíveis na loja para venda, uma informando o preço de fábrica
# dos jogos para aumentar o estoque, uma para registrar as vendas e uma para
# registrar as compras de estoque. Todas as informações de um jogo devem
# estar no mesmo índice nas listas. Criar um menu interativo com as seguintes
# opções para o usuário: Registrar venda, Compra de estoque, Resumo da loja,
# Sair. Ao sair indicar que o caixa está fechado. O usuário deve controlar o
# sistema da loja, registrando as vendas e as compras de estoque, sem esquecer
# de alterar os valores da lista de quantidade.
from biblioteca import libs
from time import sleep

disponiveis = ["God Of War", "The Last Of Us", "Gta", "Detroit Become Human"]
preco = [100.72, 84.99, 14.55, 66.80]
quantidade = [2, 3, 4, 10]
vendas = []
opcao = 0
while True:
    libs.linha('GAMER NERD FUTURAMA')
    print('''[1] VENDA\n[2] COMPRA DE ESTOQUE \n[3] RESUMO DA LOJA\n[4] SAIR''')
    try:
        opcao = int(input('\033[1mSua escolha: \033[m'))
    except ValueError:
        print('Opção inválida')
    if opcao == 1:
        libs.linha('JOGOS')
        libs.mostraLista(disponiveis)
        jogoVendido = str(input('Qual jogo deseja?: ')).strip().title()
        if jogoVendido not in disponiveis:
            print('Opção inválida')
            continue
        quantidadeVendida = int(input('Quantidade: '))
        indice = disponiveis.index(jogoVendido)
        if quantidadeVendida <= quantidade[indice]:
            print('Jogo vendido!')
            quantidade[indice] -= quantidadeVendida
            vendas.append(preco[indice] * quantidadeVendida)
        else:
            sleep(1)
            print('Essa quantidade não está disponível no estoque!')
            continue
    elif opcao == 2:
        libs.linha('COMPRA DE ESTOQUE')
        while True:
            try:
                disponiveis.append(str(input('Qual jogo deseja comprar? ')).strip().title())
                quantidade.append(int(input('Quantidade: ')))
                preco.append(float(input('Preço: ')))
                sleep(1)
                print('Compra concluída com sucesso!')
                mais = str(input('Deseja comprar mais jogos?[S/N]: ').strip().upper())
                if mais not in 'SN':
                    print('OPÇÃO INVÁLIDA')
                if mais == 'N':
                    sleep(1)
                    print('Compra de estoque concluída com sucesso!')
                    break
            except ValueError:
                print('Erro! Digite um valor válido!')
    elif opcao == 3:
        headers = ['JOGO', 'QUANTIDADE', 'PREÇO', 'VALOR TOTAL']
        dados = []
        total = 0
        for i in range(len(disponiveis)):
            valorTotal = preco[i] * quantidade[i]
            dados.append([disponiveis[i], quantidade[i], preco[i], valorTotal])
            total += valorTotal
        libs.montaTabela('TABELA', headers, dados)
        print(f'O total das vendas é: R$ {sum(vendas):.2f}')
        print(f'Valor total de estoque: R$ {total - sum(vendas):.2f}')
    elif opcao == 4:
        libs.linha('SAINDO DA LOJA...')
        sleep(1)
        break
    else:
        print('Opção indisponível')
print('Tenha um bom dia!')
