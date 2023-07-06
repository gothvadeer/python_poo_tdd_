# 1) Faça uma função que receba um número inteiro maior que zero e retorne a
# soma de todos os algarismos.
# Caso o valor seja negativo retorne 'Numero invalido'
# Exemplo:
# 251 = 2 + 5 + 1 = 8
numListFilt = ''
num = int(input('Digite um número: '))
print(num)
if num < 0:
    print('Número inválido')
else:
    numList = list(map(int, str(num))) # transforma o número em string para que
    # possa ser percorrido pelo mapa
    numListFilt = list(filter(lambda x: x > 0, numList)) # lambda retorna uma função anonima
for numero in numListFilt:
    print(f'=> {numero}', end='')
print(f' = {sum(numListFilt)}', end='')


