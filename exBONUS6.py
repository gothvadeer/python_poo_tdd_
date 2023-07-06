# # Tarefa 1: Elevar ao quadrado e filtrar números pares em uma lista
# #
# # Crie uma lista de números inteiros.
# # Use map e lambda para elevar ao quadrado cada número na lista.
# # Use filter e lambda para filtrar apenas os números pares da lista.
# # Armazene os números pares elevados ao quadrado em uma nova lista.

listaInt = [1, 29, 84, 88, 334, 20]
quadradoPares = list(filter(lambda x: x % 2 == 0, map(lambda x: x**2, listaInt)))
print(quadradoPares)