from random import choice as ch


def sorteio(cartela1, cartela2, max):
    numSorteados = []
    nums1 = []
    nums2 = []
    vencedor = ''
    sorteador = [num for num in range(1, max+1)]
    while vencedor == '':
        numS = ch(sorteador)
        sorteador.pop(sorteador.index(numS))
        numSorteados.append(numS)
        if numS in cartela1:
            nums1.append(cartela1.pop(cartela1.index(numS)))
            if len(cartela1) == 0:
                vencedor = 'João'
                print(f'O vencedor é {vencedor}!\n'
                      f'Cartela: {nums1}')
        if numS in cartela2:
            nums2.append(cartela2.pop(cartela2.index(numS)))
            if len(cartela2) == 0:
                vencedor = 'Maria'
                print(f'A vencedora é {vencedor}!\n'
                      f'Cartela: {nums2}')
            print(f'Números sorteados: {numSorteados}')
