from random import (
randint, choice, random, shuffle,
)
nomes = ['camila', 'laura', 'priscila']
print(choice(nomes)) # escolhe um nome aleatório da lista
x = round(random() * 10) # arredonda um número real aleatório e multiplica por 10
aleatorios = [randint(0, 100) for i in range(x)] # faz uma lista de números
# inteiros aleatórios de 0 à 100 (X) vezes
print(x)
print(aleatorios)
shuffle(aleatorios) # Embaralha a lista
print(aleatorios)
escolhido = choice(aleatorios) # Escolhe um número da lista
print(escolhido)
maiores = list(filter(lambda x: x > escolhido, aleatorios)) # filtra os numeros maiores que o escolhido
print(maiores)

