# 1) Crie uma função que contenha 3 funções dentro:
# - Uma delas deixa a string toda maiúscula.
# - Outra que Soma dois números passados pelo usuário.
# - E, a ultima soma um numero passado pelo usuário com um numero aleatório
# entre 0 e 15 com o comando randint().
# A função mais externa recebe todos os parâmetros com *args e deve-se fazer
# tratamento com try, except caso o usuário passe de forma errada os dados
# desejados. A função em args deve receber primeiro o nome da função interna
# que deseja acessar e os parâmetros necessários nessa ordem
# especificamente. Ex: função_externa(‘soma_num’,2,3), no caso está chamando
# a função interna que soma dois números (2,3). Cada função deve imprimir seu
# resultado
from biblioteca import libs
from random import randint


def resposta(*args):
    if args[0] == "upper":
        def upper():
            try:
                print(f'{args[1].upper()}')
            except AttributeError:
                print('Apenas strings são aceitas')

        return upper()
    elif args[0] == "soma_num":
        def soma_num():
            try:
                print(f'A soma dos dois números é: {args[1] + args[2]}')
            except TypeError:
                print('Apenas numeros podem ser somados')

        return soma_num()
    elif args[0] == "soma_aleatoria":
        def soma_aleatoria():
            try:
                aleatorio = randint(0, 15)
                print(f'A soma de: {args[1]} + {aleatorio} = {args[1] + aleatorio}')
            except TypeError:
                print('Apenas números podem ser somados')

        return soma_aleatoria()
    else:
        def erro():
            print('Não existe a função chamada')
        return erro()


resposta('soma_num', 7, 8)
