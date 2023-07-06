# Escreva um programa que receba como entrada uma lista de números e calcule a média aritmética
# dos valores. Em seguida, o programa deve exibir na tela todos os valores da lista que são maiores
# do que a média calculada.
# Por exemplo, se a lista de entrada for [5, 10, 15, 20],
# a média aritmética será 12.5. O programa deve exibir na tela os valores 15 e 20,
# que são maiores do que 12.5.
# Dica: Para calcular a média aritmética, basta somar todos os
# valores da lista e dividir pela quantidade de elementos.
# Você pode usar a função "sum" para somar os valores da lista e a função "len" para
# obter a quantidade de elementos.
from biblioteca import libs
lista = []
media = maiores = 0
for j in range(1, 5):
    lista.append(libs.lerInt(f'Digite {j}ª número: '))
    media = sum(lista) / len(lista)
    maiores = list(filter(lambda x: x > media, lista))
print(f'Lista completa: {lista}')
print(f'Média: {media}')
print(f'Maiores: {maiores}')




