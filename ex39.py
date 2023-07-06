# 1 - Criar um arquivo de texto, inserir o lucro mensal de uma startup entre os
# meses de janeiro e maio, informando o mês e o valor, através da entrada do
# usuário. Após isso, ler o arquivo e imprimir o mês de maior lucro.
from biblioteca import libs
with open('lucro.txt', 'w') as lucros:
    for l in range(5):
        mes = input(f'Digite o {l+1}ª mês: ').strip().title()
        lucro = input(f'Digite o lucro do {l+1}º mês: ')
        lucros.write(f'{mes}: ')
        lucros.write(lucro)
        lucros.write('\n')
libs.linha('MESES E LUCROS')
relatorio = {}
with open('lucro.txt') as lucros:
    for lines in lucros:
        relatorio[lines[0:3]] = int(lines[5:]) # de 0 à 3 é a chave e de 5 até o final é o valor
print(relatorio)
maiorMes = ''
maiorLucro = 0
for mes, lucro in relatorio.items():
    if lucro > maiorLucro:
        maiorMes = mes
        maiorLucro = lucro
print(f'\n--> O mês mais lucrativo foi o mês de {maiorMes} com o rendimento de {maiorLucro}')

