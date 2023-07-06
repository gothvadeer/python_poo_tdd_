# Faça um programa que imprima os n primeiros múltiplos de 5, sendo n definido
# pelo usuário. Ex: Se o usuário escolheu n=3, será impresso 5,10,15
def linha(text):
    print('~'*len(text)*2)
    print(f'{text}'.center(len(text)*2))
    print('~'*len(text)*2)
    return


while True:
    try:
        linha('OS PRIMEIROS MULTIPLOS DE 5')
        num = int(input('Digite um número: '))
        print(f'\nOs {num} primeiros multiplos de 5 são: \n')
        for n in range(1, num+1):
            print('=> ', n*5)
        break
    except ValueError:
        print('Erro! Digite uma opção válida!')
linha('FIM')