# Crie um arquivo de texto com várias linhas contendo nomes e idades de pessoas,
# separados por vírgula.
# Leia o arquivo e crie uma lista de dicionários com os dados de cada pessoa.
# Cada dicionário deve ter as chaves "nome" e "idade",
# e os valores devem ser as informações lidas do arquivo. Por fim,
# utilize a função filter() para filtrar as pessoas que têm idade superior a 30 anos.
import re

with open('pessoas.txt') as p:
    conteudo = p.readlines()
    padrao = r'(\w+),(\d+)'
    people = dict(re.findall(padrao, ''.join(conteudo)))
    pessoas = [{'Nome:': k, 'Idade': int(v)} for k, v in people.items()]
print(pessoas)
maiores30 = list(filter(lambda x: x['Idade'] > 30, pessoas))
print(maiores30)