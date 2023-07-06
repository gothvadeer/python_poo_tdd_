# - Fazer uma calculadora de 4 operações (soma, multiplicação, divisão inteira,
# potência).
# Peça a operação desejada e depois os dois números ao usuário

def menu():
    print('~*' * 20)
    print('[1] SOMA''\n' '[2] MULTIPLICAÇÃO''\n' '[3] DIVISÃO''\n' '[4] POTÊNCIA''\n' '[5] ENCERRAR')
    print('~*' * 20)


# programa principal
while True:
    n1 = int(input('Digite o 1ª número: '))
    n2 = int(input('Digite o 2º número: '))
    menu()
    opcao = int(input('Digite uma das opções [apenas números]: '))
    if opcao == 1:
        print(f'\033[1;32mA soma de {n1} + {n2} é {n1 + n2}\033[m')
    elif opcao == 2:
        print(f'\033[1;32mA multiplicação de {n1} x {n2} é {n1 * n2}\033[m')
    elif opcao == 3:
        print(f'\033[1;32mA divisão inteira de {n1} / {n2} é {n1 // n2}\033[m')
    elif opcao == 4:
        print(f'\033[1;32mA potência de {n1} e {n2} é {n1 ** n2}\033[m')
    elif opcao == 5:
        break
    else:
        print('OPÇÃO INVÁLIDA!')
    resposta = ' '     # solicitar se o usuário deseja continuar
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()
        if resposta not in 'SN':
            print('OPÇÃO INVÁLIDA')
    if resposta == 'N':
        break
print('Tenha um bom dia!')
