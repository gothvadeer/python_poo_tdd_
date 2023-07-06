# Crie uma função chamada "ordena_numeros" que recebe uma lista de números como parâmetro
# e retorna uma nova lista com os mesmos números, mas ordenados do menor para o maior.
# A função deve utilizar o algoritmo de ordenação chamado "bubble sort".
from biblioteca import libs
def numerosOrdenados(numeros):
    n = len(numeros)
    for i in range(n):
        for j in range(0, n-i-1):
            if numeros[j] > numeros[j+1]:
                numeros[j], numeros[j+1] = numeros[j+1], numeros[j]
    return numeros


num = input('Digite números separados por espaço: ').split()
transInt = list(map(int, num)) # transforma str em int
print(numerosOrdenados(transInt))

