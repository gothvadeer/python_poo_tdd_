# ) Faça uma função que calcule a diferença entre dois números, decore-a com
# outra função a partir das Mensagens: ‘Inicio do Programa’ e ‘Decorando a
# funcao’. Após isso faça com que o decorador permita que apenas seja calculada
# a diferença positiva entre os dois números, independente da ordem de entrada.
# Imprima o resultado.

def decorando(fun):
    def subtracao(n1, n2):
        print('~*'*20)
        print('Inicio do programa...'.center(40))
        print('~*' * 20)
        if n1 < n2:
            n1, n2 = n2, n1
            print(n1 - n2)
        else:
            print(n1 - n2)
    return subtracao


@decorando
def subtracao(n1, n2):
    pass


subtracao(4, 40)
