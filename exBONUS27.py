# Crie uma função chamada soma_quadrados que recebe dois números como argumentos e retorna a soma dos quadrados
# desses números. Em seguida, crie um decorador que exibe a mensagem "Calculando a soma dos quadrados" antes da
# execução da função soma_quadrados. Por fim, crie uma terceira função chamada soma_cubos que recebe dois números
# como argumentos e retorna a soma dos cubos desses números. Decore a função soma_cubos com o mesmo decorador da função
# soma_quadrados.
# Teste as duas funções decoradas para verificar se a mensagem é exibida corretamente antes da execução das funções.

def decorando(func):
    def decorar(*args):
        if len(args) == 3:
            if args[2] == 2:
                print('A soma do quadrado é... ')
            elif args[2] == 3:
                print('A soma do cubo é...')
            else:
                print('ERRO! Use "2" para o quadrado e "3" para o cubo')
                print(f'Abaixo o resulto do calculo: ({args[0]}**{args[2]}) + ({args[1]}**{args[2]}): ')
        return func(*args)
    return decorar

@decorando
def soma_quadrado(*args):
    return (args[0] ** args[2]) + (args[1] ** args[2])

@decorando
def soma_cubo(*args):
    return (args[0] ** args[2]) + (args[1] ** args[2])


print(soma_cubo(2, 9, 2))