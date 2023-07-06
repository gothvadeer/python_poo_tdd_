# Rafael deseja entrar em uma onda fitness, para isso colocou várias metas
# como, acordar cedo, definir um tempo de exercício, definir dias de descanso e
# qual esporte iria praticar. Para isso aplique o método TDD para criar e testar as
# próximas três funções:
# a) acordar_cedo: Essa função recebe a hora que ele acordou como parâmetro
# e testa se ele acordou após as 6 horas, caso afirmativo retorne ‘Tente
# novamente amanhã’, caso contrário ‘Você é um guerreiro’.
# b) tempo_exercicio: Essa função recebe a quantidade de horas exercitadas e o
# peso (kg) de Rafael, caso o tempo seja inferior a 2 horas, utilize pass, caso
# contrário, reduza 1 kg do peso e retorne o valor.
# c) tem_exercicio: Função que reconhece se é um dia de descanso ou não,
# recebe como parâmetro o esporte que irá praticar no dia, caso receba a string
# ‘Descanso’ retorna False (Para mostrar que hoje não há exercício), caso
# contrário retorna True.
# - Nota: Cada aluno poderá desenvolver um conjunto de testes diferente um do
# outro, mas será aplicado uma das possíveis soluções abaixo.
from random import choice

def acordar_cedo():
    hora = [hora for hora in range(5, 12)]
    hora_comecar = choice(hora)
    if hora_comecar <= 6:
        print(f'Acordou às {hora_comecar}h\n'
                f'Você é um guerreiro!')
    else:
        print(f'Ops! {hora_comecar}h não é uma boa hora pra começar!\n'
                f'Tente novamente amanhã')

def tempo_exercicio(horas, peso):
    if horas < 2:
         pass
    else:
        peso -= 1
        return peso

def tem_exercicio():
    dayOff = ['Descanso', 'Treino']
    dayOff_choice = choice(dayOff)
    if dayOff_choice == 'Descanso':
        print('Descanso')
        return False

    else:
        print(f'{dayOff_choice}: Natação')
        return True






