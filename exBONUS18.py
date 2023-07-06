# Crie um programa em Python que solicite ao usuário que
# digite um nome de arquivo de texto contendo frases, uma frase por linha.
# O programa deve ler o arquivo e imprimir na tela todas as frases que contêm
# uma determinada palavra fornecida pelo usuário.
# O programa deve solicitar ao usuário que digite a palavra a ser procurada.

with open('frases.txt') as frases:
    user = str(input('Digite uma palavra-chave: ')).strip().lower()
    frasesPalavraChave = [frase.strip() for frase in frases if user.lower() in frase.lower()]
    if frasesPalavraChave:
        for frase in frasesPalavraChave:
            print(frase)
    else:
        print('Não há frase com a palavra-chave disponível')


