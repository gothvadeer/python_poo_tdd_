def cadastrar():
    produtoNome = str(input('Nome do produto: ')).title().strip()
    produtoPreco = float(input('Preço do produto: '))
    produtoQuantidade = int(input('Quantidade em estoque: '))
    with open('produtos.txt', 'a') as cadastro:
        cadastro.write(f'{produtoNome}; {produtoPreco}; {int(produtoQuantidade)}\n')
        print(f'O {produtoNome} foi cadastrado com sucesso!')


def consultar():
    busca = str(input('Digite o nome do produto: ')).title().strip()
    with open('produtos.txt', 'r') as arquivo:
        for linha in arquivo:
            if ';' in linha:
                produto, preco, quantidade = linha.strip().split(';')
                if produto == busca:
                    print(f'Preço unitário: R$ {preco:.2f}')
                    print(f'Quantidade em estoque: {quantidade}')
                    break
        else:
            print('Produto não encontrado no estoque!')


def listar():
    with open('produtos.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
        print('PRODUTO'.rjust(5), 'PREÇO'.rjust(10), 'QUANTIDADE'.rjust(15))
        for linha in linhas:
            produto, preco, quantidade = linha.strip().split(';')
            print(f'{produto}', f'R${preco}'.rjust(10), f'{quantidade}'.rjust(10))


def vender():
    nome = str(input('Digite o nome do produto: ')).strip().title()
    quantidadeVendida = int(input('Digite a quantidade que deseja comprar: '))
    with open('produtos.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
        for i, linha in enumerate(linhas):
            produto, preco, quantidade = linha.strip().split(';')
            if produto == nome:
                if int(quantidade) >= int(quantidadeVendida):
                    novaQuantidade = int(quantidade) - quantidadeVendida
                    linhas[i] = f'{produto}; {preco}; {novaQuantidade}'
                    valorTotal = float(preco) * quantidadeVendida
                    print(f'COMPRA FEITA COM SUCESSO!\nValor total: R$ {valorTotal}')
                    break
                else:
                    print('Não há estoque suficiente')
                    break
            elif int(quantidade) < int(quantidadeVendida):
                print('Não existe produto no estoque')
        with open('produtos.txt', 'w') as arquivo:
            arquivo.writelines(linhas)
