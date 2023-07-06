# Exercícios:
# 1) Crie uma lista que armazene inteiros de um usuário em um loop até que o
# usuário não deseje mais adicionar, trate o erro com try/except caso o usuário
# digite uma letra ao invés de um numero. Passe essa lista para uma função
# geradora que reconhecerá quais são os números primos dentro da lista
# passada inicialmente. Caso seja um numero primo, retorne pelo método yield,
# caso contrário passe para o próximo numero. Ao final, imprima os valores
# retornados pelo yield em forma de tupla
from biblioteca import libs


def isPrime(lista):
    for numero in lista:
        primo = True
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                primo = False
            break
        if primo:
            yield numero


numeroLista = []
while True:
    num = libs.lerInt('Digite um número: ')
    numeroLista.append(num)
    mais = str(input('Quer adicionar mais? [S/N]: ')).strip().upper()
    if mais not in 'SN':
        print('ERRO! Digite "S" para sim e "N" para não')
    if mais == 'N':
        break
    elif mais == 'S':
        continue
if len(numeroLista) == 0:
    print(f'Não foi digitado nenhum número primo')
else:
    print(tuple(isPrime(numeroLista)))



