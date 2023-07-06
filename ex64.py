#  Crie um programa representando uma calculadora que realiza as operações
# de multiplicação, divisão, potência e fatorial com até dois números. Receba do
# usuário a operação que deseja fazer e os números escolhidos por ele.
# Implemente uma função para cada operação matemática utilizando os Doctests.
# Por fim, faça o tratamento de erros com try/except/else/finally.
# Observação: Utilize o método TDD

import math
from biblioteca import libs
from time import sleep


def multiplicacao(n1, n2):
        """
        Função que multiplica dois números fornecidos pelo usuário
        >>> multiplicacao(2,2)
        4
        """
        return n1 * n2


def divisao(n1, n2):
    """
    Função que divide o valor por um número fornecido pelo usuário
     >>> divisao(2,2)
     1.0
     """
    if n2 < 0 or n2 == 0:
        print(f'Não é possível dividir por {n2}')
    return n1 / n2


def potencia(n1, n2):
    """
    Função que retorna o resultado do "valor" (base)
    com um número fornecido pelo usuário (expoente)
    >>> potencia(2,2)
    4
    """
    return n1**n2


def fatorial(numero):
    """
    Função que retorna o fatorial do número fornecido pelo usuário.
    >>> math.factorial(5)
    120
    """
    if numero < 0:
        raise ValueError('Não é possível calcular números abaixo de zero')
    return math.factorial(numero)


while True:
    libs.montaMenu('CALCULADORA!\n'
                   '[1] - MULTIPLICAÇÃO\n'
                   '[2] - DIVISÃO\n'
                   '[3] - POTÊNCIA\n'
                   '[4] - FATORIAL\n'
                   '[5] - SAIR')
    op = libs.lerInt('Sua opção: ')
    if op == 1:
        print('Escolha os números que deseja multiplicar...')
        sleep(1)
        n1 = libs.lerInt('1º número: ')
        n2 = libs.lerInt('2º número: ')
        print(multiplicacao(n1, n2))
    elif op == 2:
        print('Escolha os números que deseja divir...')
        sleep(1)
        n1 = libs.lerInt('1ª número: ')
        n2 = libs.lerInt('2º número: ')
        print(divisao(n1, n2))
    elif op == 3:
        print('Escolha os números para a potência: ')
        sleep(1)
        n1 = libs.lerInt('1º número: ')
        n2 = libs.lerInt('2º número: ')
        print(potencia(n1, n2))
    elif op == 4:
        print('Escolha o número para saber o fatorial..')
        sleep(1)
        numero = libs.lerInt('Numero: ')
        print(fatorial(numero))
    elif op == 5:
        print('Saindo do programa...')
        sleep(1.5)
        print('Programa finalizado com sucesso!')
        break

