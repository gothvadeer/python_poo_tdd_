#Crie um programa que encontre e imprima as raízes de uma equação do
#segundo grau, utilizando o método de Bhaskara.

from math import sqrt
a = float(input('Digite o coeficiente de A: '))
b = float(input('Digite o coeficiente de B: '))
c = float(input('Digite o coeficiente de C: '))
delta = b**2 - 4*a*c
if delta < 0:
    print('A equação possui raízes reais')
else:
    x1 = (-b + sqrt(delta)) / (2*a)
    x2 = (-b - sqrt(delta)) / (2*a)
    print(f'\033[1mAs raízes da equação são x1={x1:.2f} e x2={x2:.2f}')
