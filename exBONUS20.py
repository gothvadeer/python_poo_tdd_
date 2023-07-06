# Suponha que você tenha um arquivo chamado "notas.txt" com as notas de alunos em um curso,
# uma por linha. Cada nota é um número inteiro de 0 a 10.
# Escreva um programa em Python que leia o arquivo "notas.txt" e armazene as notas em uma lista.
# Em seguida, calcule a média das notas e imprima o resultado na tela.

with open('notas.txt') as notasCurso:
    linhas = notasCurso.readlines()
    listaNotas = [int(notas) for linha in linhas for notas in linha.split()] # apenas uma lista
    media = sum(listaNotas) / len(listaNotas)
print(listaNotas)
print(media)
