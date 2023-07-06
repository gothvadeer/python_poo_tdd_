#  Faça um programa que calcule a soma dos divisores de um número inteiro
# Definido pelo usuário. Ex: Se o usuário escolheu 10, temos 1 + 2 + 5 + 10 = 18

while True:
    try:
        numero = int(input('Digite um número: '))
        soma = sum([n for n in range(1, numero + 1) if numero % n == 0])
        print(f'A soma dos divisores de {numero} é {soma}')
        if input('Deseja continuar? [S/N]: ').strip().upper() == 'N': # resolve o problema de repetição
            break
    except ValueError:
        print('ERRO! Digite uma opção válida ')