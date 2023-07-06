# Tarefa 2: Concatenar duas listas e filtrar elementos que aparecem em ambas
#
# Crie duas listas com elementos em comum.
# Use zip para combinar as duas listas em uma lista de tuplas.
# Use map e lambda para concatenar os elementos de cada tupla em uma única string.
# Use filter e lambda para filtrar os elementos que aparecem em ambas as listas.
# Armazene os elementos filtrados em uma nova lista.

lista1 = ['Laura', 'Bruna', 'Raquel', 'João']
lista2 = ['João', 'Laura', 'Bruna', 'Umberto']
listaTupla = tuple(zip(lista1, lista2))
concatenando = list(map(lambda x: x[0] and x[1], listaTupla))
filtrando = list(filter(lambda x: x in lista1 and x in lista2, concatenando))
print(filtrando)

