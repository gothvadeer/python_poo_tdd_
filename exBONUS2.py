# Escreva uma função lambda que receba um número como argumento e
# retorne uma lista com todos os números de 1
# até o número passado como argumento que são múltiplos de 3 ou de 5.

mult = lambda n: [x for x in range(1, n+1) if x % 5 == 0 or x % 3 == 0]
print(mult(10))