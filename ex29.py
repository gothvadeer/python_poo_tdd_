# 1) Aplique o procedimento Try/Except/Else/Finally no seguinte código que
# realiza um cadastro de formulário para uma pessoa realizar uma viagem:
from biblioteca import libs

while True:
    try:
        opcoes_viagem = {1: 'EUA', 2: 'Franca', 3: 'Japao', 4: 'Brasil'}
        nome = input('Digite seu nome: ').strip().title()
    except:
        print('Erro! Digite algo válido!')
    else:
        idade = libs.lerInt('Digite sua idade: ')
        lugar = libs.lerInt("Digite o numero para escolha do lugar: \n 1 - EUA "
                            "\n 2 - Franca \n 3 - Japao \n 4 - Brasil \nOpção: ")
        pais = opcoes_viagem[lugar]
    finally:
        print('Cadastro finalizado!')
        break
