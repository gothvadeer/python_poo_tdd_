# 1 Criar duas listas de mesmo tamanho preenchidas com números inteiros e
# retornar outra lista com a soma das duas listas sendo uma delas invertida
# (indice 0 com indice 9 para uma lista de tamanho 10, por exemplo), utilizando
# lambda e comprehensions para iterar em ambas
from random import randint

# lista1 = [randint(1, 20) for _ in range(10)]
# lista2 = lista1[::-1]
# lista3 = lambda x, y: print(sum(x+y))
# print(f'{lista1}\n{lista2}')
# lista3(lista1, lista2)

list1 = [30, 40, 50, 20, 10, 90, 233]
list2 = [743, 45, 53, 22, 12, 444, 324]
list3 = []
list2.reverse()
soma = lambda list1, list2: [list1[ind] + list2[ind] for ind in range(0,7)]
list3.append(soma(list1, list2))
print(list3)