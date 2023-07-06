# 1 - Criar uma lista e uma tupla com diversos valores, separar os valores máximos e
# mínimos de cada uma em um conjunto. Por fim, verificar se os 4 valores separados
# são verdadeiros ou falsos utilizando o any e o all.

tupla = (10, 22, 845, 2938, 193, 14, 49, False)
lista = [91838, 444, 394, 93, 183, 10, 1, True]

print(max(tupla)) # 2938
print(max(lista)) # 91838
print(min(tupla)) # False
print(min(lista)) # 1
print(any(tupla)) # True
print(any(lista)) # True
print(all(tupla)) # False
print(all(lista)) # True