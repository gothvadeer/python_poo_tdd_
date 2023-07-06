# 1) Foi realizada uma pesquisa de algumas características e gostos de quatro
# habitantes incluindo: nome, sexo, esporte favorito (Natação, Futebol, Volêi,
# Tênis) e idade. Com esses dados faça:
# - Função que armazene os dados em uma lista. Dica: Use dicionários dentro da
# lista.
# - Calcule a idade média de homens que gostam de natação. Caso não haja
# homens que gostam de natação chame uma função e imprima um aviso de que
# não há homens que gostam de natação.

habitantes = [{'Nome': 'João', 'Sexo': 'Masculino', 'Esporte': 'Futebol', 'Idade': 20},
              {'Nome': 'Laura', 'Sexo': 'Feminino', 'Esporte': 'Tênis', 'Idade': 21},
              {'Nome': 'Gabriel', 'Sexo': 'Masculino', 'Esporte': 'Futebol', 'Idade': 29},
              {'Nome': 'Luísa', 'Sexo': 'Feminino', 'Esporte': 'Futebol', 'Idade': 30}]


def hab_pesquisa():
    for p in habitantes:
        print(f'{p}')


hab_pesquisa()

idades = [p['Idade'] for p in habitantes if p['Sexo'] == 'Masculino' and p['Esporte'] == 'Futebol']
if len(idades) == 0:
    print('=> Não há homens que gostam de futebol na lista')
else:
    print(f'\033[1mA média de idade dos homens que gostam de futebol: {sum(idades) / len(idades)}')
