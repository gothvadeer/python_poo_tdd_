# Crie um programa em Python que leia um arquivo de texto chamado "emails.txt",
# que contém endereços de email em cada linha. O programa deve criar um novo arquivo chamado
# "dominios.txt",
# que contém apenas os domínios dos endereços de email, sem o nome do usuário e o "@".

with open('emails.txt') as emails:
    linhas = emails.readlines()
    arquivo = [linha.strip().split('@') for linha in linhas]
    dominios = [nomes[1] for nomes in arquivo]

with open('dominios.txt', 'w') as dom:
    stringDom = '\n'.join(dominios) # transforma lista em string
    dom.write(stringDom)


