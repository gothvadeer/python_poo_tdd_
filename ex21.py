# 1 - Faça o sistema de uma corrida entre MerCúrio, Papa-Léguas, SoNic, FlaSh,
# LiGeirinho e Super Homem (MC, PL, SN, FS, LG, SH). Crie uma função que
# receba os 6 corredores em ordem do vencedor até o último (pedir ao usuário),
# sendo os três primeiros em variáveis obrigatórias e os três últimos em kwargs,
# com as chaves sendo as posições na corrida. Pedir ao usuário se houve
# trapaça:
#  - se não houve: apresentar a classificação final.
#  - se houve: pedir ao usuário quem trapaceou e quem foi prejudicado. Depois,
# trocá-los de posições. Por fim, apresentar a classificação final.

from biblioteca import libs


def classificacaoParcial(primeiro, segundo, terceiro, **outros):
    while True:
        quarto = ''
        ultimo = ''
        opcao = str(input('Teve trapaça? [S/N]: ')).strip().upper()[0]
        if opcao == 'N':
            for posicao, corredor in outros.items():
                if posicao == 4:
                    quarto = corredor
                elif posicao == 5:
                    ultimo = corredor
            classFinal(primeiro, segundo, terceiro, quarto, ultimo)
            break
        elif opcao == 'S':
            colocacao = [primeiro, segundo, terceiro]
            colocacao.extend(outros.values())
            babaca = str(input('Quem trapaceou?: ')).strip().upper()
            vitima = str(input('Quem foi a vítima?: ')).strip().upper()
            posBabaca = colocacao.index(babaca)
            posVitima = colocacao.index(vitima)
            colocacao[posBabaca] = vitima
            colocacao[posVitima] = babaca
            classFinal(*colocacao)
            break
        else:
            print('Digite uma opção válida!')
            continue


def classFinal(primeiro, segundo, terceiro, quarto, ultimo):
    print('========= CLASSIFICAÇÃO FINAL =========')
    print(f'1º Classificado: {primeiro}')
    print(f'2º Classificado: {segundo}')
    print(f'3º Classificado: {terceiro}')
    print(f'4º Classificiado: {quarto}')
    print(f'5º Último: {ultimo}')


if __name__ == '__main__': # isso diz que é o programa principal
    libs.linha('CORREDORES:\nMERCÚRIO - MC\nPAPA-LÉGUAS - PL\nSONIC - SN\nLIGEIRINHO - LG\nSUPER-HOMEM - SH')
    pri = input('Primeiro: ').strip().upper()
    seg = input('Segundo: ').strip().upper()
    terc = input('Terceiro: ').strip().upper()
    qua = input('Quarto: ').strip().upper()
    ult = input('Último: ').strip().upper()
    outros = {'4': qua, '5': ult}
    classificacaoParcial(pri, seg, terc, **outros)
