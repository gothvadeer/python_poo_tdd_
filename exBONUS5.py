# Crie um programa que leia duas listas de nomes do usuário,
# e depois utilize as funções filter e zip para criar uma nova lista contendo
# apenas os nomes que são iguais nas duas listas, e que têm um número ímpar de letras.

nomes1 = input('Digite nomes, separe por espaço: ').split()
nomes2 = input('Digite mais nomes, separe por espaços: ').split()
listaNomes1 = list(map(str, nomes1))
listaNomes2 = list(map(str, nomes2))
iguais = list(filter(lambda x: x[0] == x[1] and len(x[0]) % 2 == 1, zip(listaNomes1, listaNomes2)))
print(iguais)
