# Exercício 1:
# Escreva um programa que leia um arquivo de texto contendo várias linhas
# de números separados por vírgulas e crie uma lista de tuplas,
# onde cada tupla contém os números de uma linha do arquivo.

with open('tuplaNumeros.txt') as num:
    linhas = num.readlines()
    numeros = [tuple(int(n) for n in linha.strip().split(',')) for linha in linhas]
print(numeros)
