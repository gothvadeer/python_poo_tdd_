#  Faça um programa que calcule a soma dos divisores de um número inteiro
# Definido pelo usuário. Ex: Se o usuário escolheu 10, temos 1 + 2 + 5 + 10 = 18
while True:
    soma = 0
    try:
        numero = int(input('Digite um número: '))
        for n in range(1, numero + 1):  # analisa cada indice de número
            if numero % n == 0:  # aqui ver se ele foi dividid
                soma += n
        print(f'A soma dos números é {soma}.')
        while True:
            opcao = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
            if opcao not in 'SN':
                print('ERRO! Opção inválida')
            if opcao == 'N':
                break
    except ValueError:
        print('Por favor, digite um número inteiro')
    break
print('\n===== Tenha um bom dia! =====')
