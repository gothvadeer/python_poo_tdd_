# - Receba numeros inteiros do usuário e armazene-os em uma lista. Crie uma
# condição para o número 0 finalizar o processo de preenchimento. Após isso,
# imprima o maior valor da lista utilizando as funções sorted() e len(). Por fim,
# utilize reversed() para inverter a lista e obtenha, pelo índice, o valor
# intermediário da mesma.
# Obs.: Caso o número de valores da lista seja par, pegue a média dos dois
# valores centrais.
from biblioteca import libs

while True:
    lista = []
    while True:
        lista.append(libs.lerInt('Digite um número: '))
        op = str(input('Deseja adicionar mais?[S/N]: ')).strip().upper()[0]
        if op not in 'SN':
            print('ERRO! Digite "S" para sim e "N" para não')
            continue
        if op == 'S':
            continue
        elif op != 'S':
            break
    break
listaOrdenada = sorted(lista)
listaInvertida = list(reversed(listaOrdenada))
tamanho = len(lista)
print(f'O maior número digitado foi: {max(lista)}')
print(f'O menor número da lista foi: {min(lista)}')
if len(lista) % 2 == 1:
    print(f'O valor intermediário é: {listaInvertida[tamanho//2]}')
else:
    print(f'O valor intermediário é: '
          f'{listaInvertida[tamanho // 2] + listaInvertida[(tamanho //2)- 1] / 2}')