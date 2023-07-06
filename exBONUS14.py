# Escreva um programa que leia um arquivo de texto contendo várias linhas de palavras
# separadas por espaço e crie uma lista de palavras únicas, ordenadas em ordem alfabética.

with open('palavras.txt') as palavras:
    linha = palavras.readlines()
    separada = [palavra.strip() for palavras in linha for palavra in palavras.split()]
    alfabetica = sorted(separada)
print(alfabetica)