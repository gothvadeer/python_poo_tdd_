# Crie uma função que receba como parâmetros um valor numérico e uma lista de valores numéricos.
# A função deve retornar uma nova lista com os valores da lista original multiplicados pelo valor passado
# como primeiro parâmetro. Além disso, a função deve fazer tratamento de exceção para garantir
# que o primeiro parâmetro é um número e que a lista é composta apenas por valores numéricos


def lista_numerica(*args):
    def multiplicar():
        try:
            if all(isinstance(x, (int, float)) for x in args[1]):
                numero = int(args[0])
                lista = list(map(lambda x: numero * x, args[1]))
                print(lista)
            else:
                print('Apenas números são permitidos')
        except ValueError:
            print('Apenas numeros são permitidos')

    return multiplicar()


lista_numerica(4, [9, 9, 4, 5])
