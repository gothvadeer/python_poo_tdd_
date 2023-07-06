#Crie um decorador que registre o tempo de execução de uma função.
# O decorador deve imprimir o tempo de execução da função em segundos após a execução da função.
#Certifique-se de que a função decorada possa receber parâmetros.
#O tempo de execução deve ser calculado usando a biblioteca time do Python.
#Dica: use a função time() para obter o tempo atual em segundos antes e depois da execução da função.
# Subtraia o tempo final do tempo inicial para obter o tempo de execução.
import time

def decorador(func):
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = func(*args, **kwargs)
        fim = time.perf_counter()
        print(f'O tempo da {func.__name__} foi {fim - inicio}')
        return resultado
    return wrapper

@decorador
def somar(n1, n2):
    print(n1 + n2)

@decorador
def subtrair(n1, n2):
    if n1 < n2:
        n1, n2 = n2, n1
    print(n1 - n2)

@decorador
def multiplicar(n1, n2):
    print(n1 * n2)

multiplicar(5,7)
subtrair(6, 9)