# Crie um sistema de cadastro e login de um site, utilizando um username e
# senha informados pelo usuário.

def linha(text):
    tamanho = len(text) + 8
    print('~'* tamanho)
    print(f'{text.center(tamanho)}')
    print('~'* tamanho)


login = False
linha('CADASTRO')
usuario = str(input('Digite seu nome de usuário: ')).strip().lower()
senha = input('Digite sua senha: ').strip()
linha('LOGIN')
while True:
    if input('USUÁRIO: ') == usuario and input('SENHA: ') == senha:
        login = True
    if login:
        print(f'Bem vindo(a), {usuario}!')
        break
    else:
        print('Usuário ou senha inválidos, tente novamente!')


