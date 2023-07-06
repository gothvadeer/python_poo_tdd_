# Implemente um programa que simule um jogo de adivinhação. O programa deve gerar um número
# aleatório entre 1 e 10, e o jogador deve tentar adivinhar qual é esse número.
# O jogador terá um número limitado de tentativas para acertar o número.
#
# Requisitos:
#
# O programa deve solicitar ao jogador que digite um número.
# O programa deve informar se o número digitado é maior ou menor que o número aleatório.
# O programa deve informar ao jogador se ele acertou o número ou se esgotou as tentativas.
# Dicas:
#
# Utilize a função randint do módulo random para gerar o número aleatório.
# Utilize uma estrutura de repetição para permitir que o jogador faça várias tentativas.
# Utilize uma variável para contar o número de tentativas.
# Utilize a declaração if para verificar se o número digitado pelo jogador é igual ao número aleatório.
# Utilize a declaração break para sair do loop quando o jogador acertar o número ou esgotar as tentativas.
from biblioteca import libs
from random import randint


class Jogo:

    def jogada(self):
        numero = randint(1, 10)
        palpite = 0
        while palpite < 3:
            pt = libs.lerInt('Digite um número para adivinhar: ')
            if numero > pt:
                print(f'Ainda não é o número! Pense em um número maior!')
            elif numero < pt:
                print(f'Pense novamente! Pense em um numero menor!')
            elif numero == pt:
                print(f'Parabéns! Você acertou! O número pensado foi {numero}')
                return
            palpite += 1
        print(f'Acabaram os seus palpites! O número pensado foi {numero}')


jogador = Jogo()
jogador.jogada()



