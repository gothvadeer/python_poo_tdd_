# Dudu é um famosinho do instagram e precisa manter postagens em seu
# feed regularmente. Portanto teve a ideia de criar um programa em Python que
# agende suas publicações para todas segundas, quartas e sextas ao longo de
# um mês, a partir deste momento. Além disso, seus posts irão variar entre os
# temas: saúde, vida pessoal e motivacional. Com isso, utilize choice() para
# selecionar cada conteúdo aleatoriamente. Faça um programa que implemente
# a ideia de Dudu, imprimindo o conteúdo de cada um dos dias e seus
# respectivos dias de postagem.
from random import choice
import datetime
import locale
postagem = ['Saude',
            'Vida pessoal',
            'Motivacional']

class Instagram:
    days = 0
    @classmethod
    def programarPostagem(cls):
        delta = datetime.timedelta(days=30)
        data_atual = datetime.datetime.now()
        data_final = data_atual + delta
        locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')
        while data_atual < data_final:
            if data_atual.weekday() in [0, 2, 4]:
                cls.days += 1
                print(f'Postagem: {choice(postagem)}\n'
                      f'Dia da semana: {data_atual.strftime("%A")}\n'
                      f'Total de postagens: {cls.days}')
                print('~'*30)
            data_atual += datetime.timedelta(days=1)


dudu = Instagram()
dudu.programarPostagem()

