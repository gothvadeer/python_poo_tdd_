# Crie um programa que leia uma lista de nomes do usuário,
# e depois utilize as funções map e filter para criar uma nova lista contendo
# apenas os nomes que começam com a letra "A"
# , e em seguida converta cada nome em letras maiúsculas.

nomes = input('Digite vários nomes, separe por espaços: ').split()
listNomes = list(map(str, nomes))
listaNomesA = list(map(lambda x: x.upper(), filter(lambda x: x[0] == 'a', listNomes)))
print(listaNomesA)