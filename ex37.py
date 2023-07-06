# 1 - Crie um arquivo de texto na pasta onde está seu programa Python. O
# arquivo deve conter alguns números de 4 dígitos separados por linha,
# representando números de uma rifa. Após isso, itere no arquivo para colocar os
# valores em uma lista. Por fim, utilize a função choice() para determinar o
# ganhador.

from random import choice

with open('arq.txt') as arquivo:
    numeros = [linha.strip() for linha in arquivo]
    ganhador = choice(numeros)

print(f'O ganhador é: {ganhador}')
