# 1 - Criar uma função recursiva (que retorne ela mesma) para armazenar N
# termos da sequência de Fibonacci em uma lista. N é definido pelo usuário. Ao
# encontrar os termos, imprimir a lista e finalizar a função.
from biblioteca import libs
listFibonacci = []
stop = 0


def fibonacci(stop, a, b, count):
    global listFibonacci
    listFibonacci.append(a)
    a, b = b, a + b
    count += 1
    if stop == count:
        print(listFibonacci)
        return 0
    else:
        return fibonacci(stop, a, b, count)


while stop < 1:
        stop = libs.lerInt('Digite a quantidade de termos: ')
        fibonacci(stop, a=1, b=1, count=0)
