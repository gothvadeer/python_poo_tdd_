# 1) Para cada número par em um range de 1 a 9, adicione esse número elevado
# ao quadrado no conjunto, se o número for ímpar adicione 2 elementos, 1 por vez:
# ‘Sou’, ’Impar’. Qual foi a resposta? Por que ‘Sou’, ‘Impar’ só apareceu uma vez?

conjunto = {numero ** 2 if numero % 2 == 0 else 'sou' if num == 0 else
'impar' for num in range(0,2) for numero in range(1,10)}
print(conjunto)

#Na linha acima estamos fazendo para cada numero dentro do intervalo
# de 1 a 10 faça:
#Se o resto da divisão de numero por 2 for zero faça: adicione numero
# elevado ao quadrado
#Caso contrário, para cada num dentro do intervalo de 0 a 1 faça:
#Se num é igual a zero adicione 'Sou' ao conjunto, caso contrário
# adicione 'impar' 