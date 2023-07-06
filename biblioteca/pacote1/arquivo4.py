from biblioteca import libs
def adicionar_contato():
    while True:
        nome = str(input('Nome: ')).strip().title()
        telefone = libs.lerInt('Telefone: ')
        email = input('Email: ')
        mais = str(input('Deseja adicionar mais? [S/N]: ')).strip().upper()
        with open('contatos.txt', 'a') as arquivo:
            linhas = f'{nome}; {telefone}; {email}\n'
            arquivo.writelines(linhas)
        if mais == 'S':
            continue
        else:
            break
    print('Contato adicionado com sucesso!')


def consultar_contato():
    nomeBusca = str(input('Nome: ')).strip().title()
    with open('contatos.txt', 'r') as arquivo:
        for linha in arquivo:
            if ';' in linha:
                nome, telefone, email = linha.strip().split(';')
                if nome == nomeBusca:
                    print(f'O tefone de {nomeBusca} é: {telefone}')
                    print(f'O email de {nomeBusca} é: {email}')
                    break
                else:
                    print('Contato não existe na lista telefônica')
                    break


def listar_contato():
    with open('contatos.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
        print(f'NOME'.rjust(5), f'TELEFONE'.rjust(15), f'EMAIL'.rjust(10))
        print('~'*40)
        for linha in linhas:
            if ';' in linha:
                nome, telefone, email = linha.strip().split(';')
                print(f'{nome}'.rjust(5), f'{telefone}'.rjust(15), f'{email}'.rjust(15))


def editar_contato():
    print(f'[1] - EDITAR NOME\n[2] - EDITAR TELEFONE\n[3] - EDITAR EMAIL')
    op = libs.lerInt('Sua opção: ')
    nomeBusca = str(input('Digite o nome: ')).strip().title()
    with open('contatos.txt', 'r') as a:
        conteudo = a.readlines()
    conteudoEncontrado = False
    for i, linha in enumerate(conteudo):
        if ';' in linha:
            nome, telefone, email = linha.strip().split(';')
            if nome == nomeBusca:
                conteudoEncontrado = True
                if op == 1:
                    novoNome = str(input('Nome: ')).strip().title()
                    conteudo[i] = f'{novoNome}; {telefone}; {email}\n'
                    print(f'Contato atualizado com sucesso, o novo nome é {novoNome}')
                elif op == 2:
                    novoTelefone = libs.lerInt('Novo telefone: ')
                    conteudo[i] = f'{nome}; {novoTelefone}; {email}\n'
                    print(f'Contato atualizado com sucesso, o novo telefone é: {novoTelefone}')
                elif op == 3:
                    novoEmail = input('Novo email: ')
                    conteudo[i] = f'{nome}; {telefone}; {novoEmail}\n'
                    print(f'Contato atualizado com sucesso, o novo email é: {novoEmail}')
                else:
                    print('Digite uma das opções!')
                    break
    if not conteudoEncontrado:
        print(f'Contato não encontrado!')
    else:
        with open('contatos.txt', 'w') as arquivo:
            arquivo.writelines(conteudo)


def deletar_contato():
    nomeBusca = str(input('Nome do contato que deseja excluir: ')).strip().title()
    contatoEncontrado = False
    with open('contatos.txt') as arquivo:
        conteudo = arquivo.readlines()
        for i, linha in enumerate(conteudo):
            if ';' in linha:
                nome, telefone, email = linha.strip().split(';')
                if nomeBusca == nome:
                    contatoEncontrado = True
                    del conteudo[i]
                    print('Contato apagado com sucesso!')
                    break
        if not contatoEncontrado:
            print(f'Não existe {nomeBusca} na lista de contatos')
        else:
            with open('contatos.txt', 'w') as a:
                a.writelines(conteudo)
