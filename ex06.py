# Faça um programa que calcule o maior palíndromo resultado do produto de
# dois números de 3 dígitos.
# Palíndromo são números que lendo da esquerda para a direita resulta no
# mesmo número caso leia da direita para esquerda. Ex: 52625
# Ex: O maior palíndromo resultado
# do produto de dois números é 91*99 = 9009

n1 = 999
res = 0
while n1 >= 100: # versão longa
    n2 = n1
    while n2 >= 100:
        numero = str(n1 * n2)
        inverte_numero = numero[::-1]
        if inverte_numero == numero:
            num = int(numero)
            if res < num:
                res = num
            n2 -= 1
        else:
            n2 -= 1
    n1 -= 1
print(res)
# Versão curta e melhor
n1 = 999
res = 0
while n1 != 99:
    n2 = n1
    while n2 != 99:
        numero = str(n1 * n2)
        if numero == numero[::-1]:
            res = max(res, int(numero))
        n2 -= 1
        n1 -= 1
print(res)
