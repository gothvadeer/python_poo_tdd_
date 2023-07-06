# 1) Decorar o exercício da Aula de Nested Functions e executar as três funções.
# - Na função que executa a string maiúscula use um decorador para imprimir:
# ’Estou gritando’.
# - Na função que soma dois números decore com ‘O maior entre os dois é:
# {maior}’.
# - Na função que soma um número com outro aleatório decore com ‘Somando
# com o aleatório:'
# - Faça o tratamento com Wraps do programa.


from random import randint
from functools import wraps

global aleatorio
aleatorio = randint(0, 15)
def decorando(funcao):
    """
    função decoradora
    """
    print(f'{decorando.__doc__}')
    @wraps(funcao)
    def wrapper(*args):
        if args[0] == 'upper':
            print('--> EU ESTOU GRITANDO: ', end='')
            return funcao(args[0], args[1].upper())
        elif args[0] == 'soma_num':
            if args[1] > args[2]:
                print(f'O maior numero é: {args[1]}')
            else:
                print(f'--> O maior numero é {args[2]}')
            return funcao(*args)
        elif args[0] == 'soma_aleatoria':
            global aleatorio
            print(f'--> O numero aleatório é: {aleatorio}')
            return funcao(*args) + aleatorio
        else:
            def erro():
                print('Não existe função chamada')
            return erro
    return wrapper

@decorando
def resposta(op, *args):
    """
    função que retorna a resposta decorada
    """
    print(f'{resposta.__doc__}')

    if op == 'upper':
        def upper():
            print(args[0])
        return upper()
    elif op == 'soma_num':
        def soma_num(*args):
            print(f'{args[0]} + {args[1]} = {args[0] + args[1]}')
        return soma_num(args[0], args[1])
    elif op == 'soma_aleatoria':
        def soma_aleatoria():
            global aleatorio
            print(f'{args[0]} + {aleatorio} = {args[0] + aleatorio}')
            return args[0] + aleatorio
        return soma_aleatoria()



resposta('upper', 'eu te amo')
resposta('soma_num', 13, 19)
resposta('soma_aleatoria', 19)