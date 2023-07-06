# 1) Sami e Dudu irão fazer uma competição de quem visita mais Estados no Brasil
# em um período de 6 meses, até então Dudu já visitou o Espírito Santo e São
# Paulo, enquanto Sami visitou Rio de Janeiro e Bahia. Crie dois conjuntos
# diferentes para simbolizar os estados que cada um foi. Após 6 meses Dudu
# visitou Bahia, Acre, Santa Catarina e Sergipe, enquanto Sami visitou Bahia,
# Minas Gerais, Amazonas e Paraná, atualize cada um dos conjuntos com os
# novos Estados. Responda:
# - Quais Estados Dudu visitou que Sami não foi?
# - Quais Estados ambos foram?
# - Sendo 27 Estados no Brasil todo, qual porcentagem o vencedor visitou?
from biblioteca import libs

sami = {'RJ', 'BH'}
dudu = {'ES', 'SP'}
libs.linha(f'COMPETIÇÃO SAMI & DUDU\n => Sami: {sami}\n => Dudu: {dudu}')
while True:
    libs.montaMenu(''
                   '[1] - ADICIONAR ESTADO NA SAMI\n'
                   '[2] - ADICIONAR ESTADO NO DUDU\n'
                   '[3] - COMPARAR A DIFERENÇA DE ESTADOS\n'
                   '[4] - ESTADOS EM COMUM\n'
                   '[5] - SAIR / GANHADOR')
    escolha = libs.lerInt('Sua escolha: ')
    if escolha == 1:
        estadoSami = str(input('Estado [use apenas sigla]: ')).strip().upper()
        sami.add(estadoSami)
        print(f'{estadoSami} foi adicionado com sucesso!')
    elif escolha == 2:
        estadoDudu = str(input('Estado [use apenas siglas]: ')).strip().upper()
        dudu.add(estadoDudu)
        print(f'{estadoDudu} foi adicionado com sucesso!')
    elif escolha == 3:
        print(f'Os estados que Dudu visitou e a Sami não visitou foram:'
              f'\n{dudu.difference(sami)}')
        print(f'Os estados que a Sami vistitou e o Dudu não visitou foram:\n'
              f'{sami.difference(dudu)}')
    elif escolha == 4:
        if len(sami.intersection(dudu)) > 0:
            print(f'Os estados que ambos visitaram foram:\n'
                  f'{sami.intersection(dudu)}')
        else:
            print('Eles não visitaram nenhum estado em comum!')
    elif escolha == 5:
        print('Programa finalizado...\n')
        break
# condicionais + resultado
if len(dudu) > len(sami):
    print(f'O vencedor foi Dudu com {len(dudu)} estados visitados,'
          f' totalizando {(len(dudu) * 100 // 27)}% dos estados do Brasil!')
elif len(dudu) < len(sami):
    print(f'A vencedora foi Sami com {len(sami)} estados visitados,'
          f' totalizando {(len(sami) * 100 // 27)}% dos estados do Brasil!')
else:
    print(
        f'Empate! Dudu e Sami visitaram {len(sami)} estados,'
        f' totalizando {(len(dudu) * 100 // 27)}% dos estados brasileiros')
