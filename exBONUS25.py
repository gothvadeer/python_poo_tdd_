# Crie uma função calculadora() que contenha duas funções aninhadas:
# soma(): recebe dois números e retorna a soma deles.
# subtracao(): recebe dois números e retorna a diferença entre eles.
# A função calculadora() deve receber como argumentos uma string indicando
# a operação a ser realizada ("soma" ou "subtracao") e dois números.
# Ela deve então chamar a função aninhada correspondente à operação e retornar o resultado.

def calculadora(*args):
    if args[0] == 'somar':
        def somar():
            print(f'A soma de {args[1]} + {args[2]} = {args[1]+args[2]}')
        return somar()
    elif args[0] == 'subtrair':
        def subtrair():
            print(f'A subtração de {args[1]} - {args[2]} = {args[1]-args[2]}')
        return subtrair()
    else:
        print('A função indicada não existe')


calculadora('dividir', 1, 4)