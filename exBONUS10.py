# Escreva um programa que receba como entrada uma lista de palavras e um número inteiro "n"
# O programa deve exibir todas as palavras da lista que têm comprimento maior do que "n".
# Por exemplo, se a lista de entrada for ["banana", "maçã", "abacaxi", "uva"]
# e o número "n" for 4, o programa deve exibir na tela as palavras "banana", "abacaxi" e "uva",
# que têm comprimento maior do que 4.
# Dica: Para calcular o comprimento de uma palavra em Python,
# basta usar a função "len". Para percorrer todos os elementos da lista,
# você pode usar um laço "for". Para exibir as palavras na tela, basta usar o comando "print".
from biblioteca import libs
lista = []
num = libs.lerInt('Digite um número: ')
for j in range(1, 5):
    lista.append(str(input(f'Digite o {j}ª nome: ')).strip().upper())
    maiores = list(filter(lambda x: len(x) > num, lista))
print(f'\nPalavras na lista com o comprimento maior que {num}:\n'
      f'{maiores}')