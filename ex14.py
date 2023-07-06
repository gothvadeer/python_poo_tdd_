# 1) Chegou o famoso dia dos namorados, Mateus deixou para decidir o presente
# em cima da hora. Ele resolveu comprar um tipo de flor, um presente e escolher
# um lugar para saírem, ele anotou todas as opções
# - Crie um programa que descubra qual a combinação mais cara, em seguida
# mais barata e a média opção. Imprima a combinação em cada caso.
# - Use um dicionário para cada item (flor, lugar e presente).

from biblioteca import libs
from time import sleep

flores = {'Rosas vermelhas': 145.00, 'Girasóis': 125.00, 'Margaridas': 120.00, 'Flores do campo': 140.00}
presentes = {'Urso de pelúcia': 55.00, 'Caixa de bombom': 60.00, 'Colar': 75.00, 'Roupas': 100.00}
lugares = {'Praia': 70.00, 'Jantar': 150.00, 'Fun park': 120.00, 'Hotel': 180.00}
# declaração de variáveis
flor = presente = lugar = precoTotal = aux = 0
florCara = ''
lugarCaro = ''
presenteCaro = ''
florBarata = ''
presenteBarato = ''
lugarBarato = ''
list = []
# programa principal
while True:
    libs.linha('FELIZ DIA DOS NAMORADOS! ESCOLHA 3 OPÇÕES DE PRESENTE')
    print('[1] FLORES\n[2] PRESENTES\n[3] LUGAR\n[4] COMBOS\n[5] SAIR')
    print('~' * 48)
    ler = input('Sua escolha: ')
    if ler.isdigit():
        ler = int(ler)
        if ler == 1:
            libs.montaTabDict(flores)
            print('~' * 48)
            opcaoF = str(input('Digite a flor desejada: ')).strip().capitalize()
            if opcaoF in flores:
                flor = opcaoF
                sleep(1)
                print(f'{opcaoF} colocado no carrinho!')
                continue
            else:
                print('Não existe essa opção no catálogo!')
        elif ler == 2:
            libs.montaTabDict(presentes)
            print('~' * 48)
            opcaoP = str(input('Digite o presente desejado: ')).strip().capitalize()
            if opcaoP in presentes:
                presente = opcaoP
                sleep(1)
                print(f'{opcaoP} colocado no carrinho')
                continue
            else:
                print('Não existe essa opção no catálogo!')
        elif ler == 3:
            libs.montaTabDict(lugares)
            print('~' * 48)
            opcaoL = str(input('Digite o lugar desejado: ')).strip().capitalize()
            if opcaoL in lugares:
                lugar = opcaoL
                sleep(1)
                print(f'{opcaoL} colocado no carrinho!')
            else:
                print('Não existe essa opção no catálogo!')
        elif ler == 4:
            for f, a in flores.items():
                for p, b in presentes.items():
                    for l, c in lugares.items():
                        preco_atual = a + b + c
                        if preco_atual > precoTotal:
                            precoTotal = preco_atual
                            florCara = f
                            presenteCaro = p
                            lugarCaro = l
            libs.linha('SE INSPIRE NOS NOSSOS COMBOS: ')
            print(f'COMBO DELUXE:\nFlor: {florCara}\nPresente: {presenteCaro}\nLugar: {lugarCaro}\n'
                  f'Total: R$ {precoTotal:.2f}')
            print('~' * 45)
            for f, a in flores.items():
                for p, b in presentes.items():
                    for l, c in lugares.items():
                        list.append(a + b + c)
                        list.sort()  # ordena para pegar o meio
            precoTotal = list[len(list) // 2]  # parte no meio
            for f, a in flores.items():  # recomeça para pegar os valores
                for p, b in presentes.items():
                    for l, c in lugares.items():
                        if a + b + c == precoTotal:
                            print(f'COMBO VIP:\nFlor: {f}\nPresente: {p}\nLugar:{l}')
                            print(f'Total: R$ {precoTotal:.2f}')
                            print('~' * 45)
            for f, a in flores.items():
                for p, b in presentes.items():
                    for l, c in lugares.items():
                        if aux == 0:
                            precoTotal = a + b + c
                            aux = +1
                        else:
                            preco_atual = a + b + c
                            if precoTotal > preco_atual:
                                precoTotal = preco_atual
                                florBarata = f
                                presenteBarato = p
                                lugarBarato = l
            print(f'COMBO STANDARD:\nFlor: {florBarata}\nPresente: {presenteBarato}\nLugar: {lugarBarato}')
            print(f'Total: R$ {precoTotal:.2f}')
            print('~' * 45)
            continue
        elif ler == 5:
            break
        else:
            print('Opção inválida!')
        libs.linha('CALCULANDO O TOTAL... ')
        print(f'FLORES: {flor}, R$ {flores[flor]:.2f}\n'
              f'PRESENTE: {presente}, R$ {presentes[presente]:.2f}\n'
              f'LUGAR: {lugar}, R$ {lugares[lugar]:.2f}')
        print(f'Total: R$ {sum((presentes[presente], flores[flor], lugares[lugar])):.2f}')
        break
