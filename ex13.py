# 1) Faça um programa que contabiliza time de heróis e vilões da seguinte forma:
# - Crie um dicionário chamado herói com chave sendo o nome do personagem e
# o elemento o nível de poder do personagem entre 1 a 100. Ex: herói =
# {‘Flash’:85}.
# - Crie outro dicionário que serão as armas que podem ser usadas pelo herói,
# sendo a chave o nome da arma e o elemento o nível de poder de 0 a 100. Ex:
# arma = {‘Escudo do Capitão América’:60}
# - Crie um último dicionário representado os vilões sendo a chave o nome e o
# elemento o nível de poder de 0 a 200. Ex: vilao={‘Thanos’:175}
# Após isso o usuário poderá escolher um herói, uma arma soma os pontos de
# poder e escolher um vilao para lutar, apresente quem foi o vencedor, caso for o
# herói imprima a arma usada. Caso resulte em empate informe na saída.
# Observação: Pode definir qualquer herói, vilao e arma que quiser.

from biblioteca import libs
from time import sleep

herois = {'Spiderman': 84, 'Superman': 100, 'Batman': 30, 'Capitão América': 30}
arma = {'Teias': 100, 'Sol Amarelo': 200, 'Traje Mech': 130, 'Escudo': 100}
viloes = {'Coringa': 180, 'Lex Luthor': 190, 'Duende Verde': 140, 'Barão Remo': 120}
while True:
    libs.linha('HERÓIS\n1º - Spiderman\n2º - Superman\n3º - Batman\n4º - Capitão América')
    h = str(input('Sua escolha: ')).strip().title()
    if h in herois:
        print('Carregando...')
        sleep(1)
        print(f'Você escolheu: {h}, boa escolha!')
    else:
        print('Carregando...')
        sleep(1)
        print(f'Não existe {h} na lista, digite um herói válido!')
        continue
    libs.linha('ARMAS\n1º - Teias\n2º - Sol Amarelo\n3º - Traje Mech\n4º - Escudo')
    a = str(input('Sua escolha: ')).strip().title()
    if a in arma:
        print('Carregando...')
        sleep(1)
        print(f'Muito bem! {a} é sua escolha de arma!')
    else:
        print('Carregando...')
        sleep(1)
        print(f'{a} não é uma arma válida')
        continue
    libs.linha('VILÕES\n1º - Coringa\n2º - Lex Luthor\n3º - Duende Verde\n4º - Barão Remo')
    v = str(input('Sua escolha: ')).strip().title()
    if v in viloes:
        print('Carregando...')
        sleep(1)
        print(f'{v} é o seu vilão!')
    else:
        print('Carregando...')
        sleep(1)
        print(f'{v} não está na lista! Tente de novo!')
        continue
    completo = herois[h] + arma[a]
    libs.linha(f'BATALHA INSANA!\n                               {h} vs {v}')
    sleep(1)
    if completo > viloes[v]:
        print(f'{h} VENCEU! com {completo} contra {viloes.get(v)} pontos')
    elif completo == viloes[v]:
        print(f'OPSS... EMPATE! ambos com {completo} pontos')
    else:
        print(f'{v} VENCEU! Você perdeu... {v} estava com {viloes.get(v)} e você apenas com {completo} pontos')
    break
