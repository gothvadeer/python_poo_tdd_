# 1) Faça um programa que calcule a média dos 5 primeiros números primos da
# sequencia Fibonacci.

def is_prime(n):
    if n <= 1:  # Função para verificar se o número é primo
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# sequência Fibonnacci
a, b = 0, 1
sum_primes = 0
count_primes = 0
while count_primes < 5:
    c = a + b
    a = b
    b = c
    if is_prime(c):
        sum_primes += c
        count_primes += 1
if count_primes == 5:
    avg_primes = sum_primes / count_primes
    print(f'A média dos 5 primeiros números primos da sequência fibonacci é: {avg_primes}')
else:
    print('Não foram encontrados números primos na sequência fibonacci')