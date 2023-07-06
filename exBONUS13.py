
# Crie um arquivo de texto com várias linhas contendo valores numéricos separados por vírgula.
# Leia o arquivo e crie uma lista de listas com os valores lidos. Em seguida, utilize a função map()
# para calcular a média de cada lista de valores.
# Por fim, utilize a função filter() para filtrar as médias que são maiores do que 20.


with open('numeros.txt') as numeros:
    linha = numeros.readlines()
    listaNum = [[int(num) for num in linha.strip().split(',')] for linha in linha if linha.strip()]
    # a lista tira o espaço e transforma em inteiro
media = list(filter(lambda x: x > 20, map(lambda x: sum(x) / len(x), listaNum)))
print(listaNum)
print(media)
