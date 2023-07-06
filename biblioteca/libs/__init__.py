import hashlib
login = False
cadastroFeito = False
username = ''
senha = ''
anterior = ''


def fazer_hash(senha):
    return hashlib.sha256(senha.encode()).hexdigest()


def linha(text):
    print('~*' * len(text))
    print(f'{text}'.center(len(text) * 2))
    print('~*' * len(text))


def mostraLista(lista):
    for pos, lista in enumerate(lista):
        print(f'{pos + 1} - {lista} ')


def montaTabela(titulo, headers, dados):
    print(f'{titulo}'.center(100))
    print('~' * 100)
    for i, header in enumerate(headers):
        print(f'{header:^20s}', end='')
    print()
    for row in dados:
        for col in row:
            print(f'{col:^20}', end='')
        print()
    print('~' * 100)


def montaTabDict(dicionario):
    print(f'TIPO'.rjust(15), 'PREÇO'.rjust(20))
    for k, v in dicionario.items():
        print(f'{k}'.rjust(15), f'R$ {v}'.rjust(20))


def lerInt(text):
    while True:
        try:
            ler = int(input(text))
            return ler
        except ValueError:
            print('ERRO! Digite um número inteiro!')
        continue


def montaMenu(txt):
    print('~'*80)
    print(f'{txt}'.center(40))
    print('~'*80)
    return


def cadastro():
    global username
    global cadastroFeito
    global senha
    username = input('Digite seu nome de usuário: ').strip()
    senha = input('Digite sua senha: ').strip()
    fazer_hash(senha)
    cadastroFeito = True
    print('===========  CADASTRO FEITO COM SUCESSO =========== ')
    return menuPrincipal()


def loginSistema():
    global username
    global senha
    global login
    if not login:
        u = input('Username: ').strip()
        s = input('Senha: ').strip()
        if u == username and s == senha:
            login = True
        if login:
            print('=========== VOCÊ ESTÁ LOGADO! ===========')
            return menuPrincipal()
        else:
            print('Username ou senha incorretos!')
            loginSistema()


def mudarSenha():
    global senha
    global login
    if login:
        s = input('Senha atual: ')
        if s == senha:
            senha = input('Nova senha: ').strip()
            fazer_hash(senha)
            print('=========== SENHA ATUALIZADA ===========')
        else:
            print('Senha atual incorreta')
            mudarSenha()
    else:
        print('=========== FAÇA LOGIN ANTES ===========')
    return menuPrincipal()


def logOut():
    global login
    login = False
    print('=========== DESLOGADO ===========')
    return menuPrincipal()


# função principal
def menuPrincipal():
    global login
    global cadastroFeito
    while True:
        linha('BEM VINDO(A)!\n[1] - CADASTRO\n[2] - LOGIN\n[3] - MUDAR A SENHA\n[4] - LOGOUT\n[5] - SAIR')
        op = lerInt('Digite um número: ')
        if op == 1:
            if not cadastroFeito:
                cadastro()
            else:
                print('=========== CADASTRO JÁ FEITO ANTERIORMENTE ===========')
        elif op == 2:
            if cadastroFeito:
                loginSistema()
            else:
                print('=========== FAÇA O CADASTRO ANTES ===========')
        elif op == 3:
            if cadastroFeito:
                mudarSenha()
            else:
                print('=========== FAÇA O CADASTRO ANTES ===========')
        elif op == 4:
            if login:
                logOut()
            else:
                print('=========== FAÇA O LOGIN ANTES ===========')
        elif op == 5:
            print('=========== PROGRAMA ENCERRADO =========== ')
            break
        else:
            print('Opção inválida')
