# 1 - Calcule o fatorial de n utilizando loop for, e depois utilizando reduce. O
# resultado é o mesmo?
# 2 - Realizar o cálculo do IMC através de uma função utilizando map com os
# dados fornecidos abaixo sobre peso e altura, e salvar os resultados em outra
# lista. Apó isso, aplicar o filter para separar pessoas obesas (IMC > 25).
# Dados:
# índice 0 das tuplas: peso (kg)
# índice 1 das tuplas: altura (m)
# listaAmostras = [(62, 1.73), (90, 1.86), (76, 2.12), (54, 1.56), (69, 1.76), (112,
# 1.63), (98, 1.59)]
from functools import reduce
# resultado exercicio 1 com for
numero = 9  # int(input('Digite um número: '))
result = 1
for n in range(1, numero + 1):
    result *= n
print(result)
# resultado exercicio 1 com reduce
result2 = reduce(lambda x, y: x * y, range(1, numero + 1))
print(result2)

# exercicio 2

listaAmostras = [(62, 1.73), (90, 1.86), (76, 2.12), (54, 1.56), (69, 1.76), (112,
                                                                              1.63), (98, 1.59)]
resultado = list(map(lambda amostra: amostra[0] / amostra[1]**2, listaAmostras))
arrendondado = [round(imc, 2) for imc in resultado] # aqui arredonda os imc
print(f'Todos os IMC: {arrendondado}')
gordos = list(filter(lambda obesos: obesos > 25, arrendondado))
print(f'Obesos: {gordos}')
