# Crie um programa em Python que leia um arquivo texto contendo várias linhas,
# onde cada linha contém uma palavra ou uma frase.
# imprima a primeira palavra de cada linha em uma única lista;

with open('palavrasEfrases.txt') as p:
    linhas = p.readlines()
    palavras = [[palavras.split() for palavras in linha.strip().split(',')] for linha in linhas if linha.strip()]
    unicaLista = [palavra[0][0] for palavra in palavras]
print(palavras)
print(unicaLista)
