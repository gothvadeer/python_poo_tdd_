# 1 - Faça um programa utilizando um arquivo chamado 'NotasEscola.txt' para
# gerenciar as notas de alunos de uma classe. O main deve conter um menu
# com as seguintes opções: a) Inserir alunos e notas b) Exibir os alunos e média
# final c) Alunos aprovados e reprovados d) Sair. Produza uma função para cada
# opção.
from biblioteca.pacote1 import main
from biblioteca import libs
while True:
    libs.montaMenu('[1] INSERIR ALUNO E NOTA\n[2] EXIBIR ALUNO E MÉDIA\n[3] ALUNOS REPROVADOS E APROVADOS\n'
                   '[4] SAIR')
    escolha = libs.lerInt('Digite uma opção: ')
    if escolha == 1:
        main.formaDicionarioNota()
    elif escolha == 2:
        main.media()
    elif escolha == 3:
        main.aprovadosReprovados()
    elif escolha == 4:
        print('Saindo...')
        break

    else:
        print('Erro! Digite uma opção do MENU!')


