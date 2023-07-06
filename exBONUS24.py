# Exercício para gerenciamento de uma lista de tarefas:
# 1 - Faça um programa para gerenciar uma lista de tarefas.
# Cada tarefa deve ter um título e um status (concluída ou não).
# O programa deve ter um menu com as seguintes opções:
# a) Adicionar tarefa: o usuário deverá informar o título da tarefa e o status (concluída ou não).
# Essas informações devem ser armazenadas em um arquivo chamado "tarefas.txt".
# b) Consultar tarefa: o usuário deverá informar o título da tarefa e o programa deverá exibir
# o status correspondente (concluída ou não).
# c) Listar tarefas: o programa deverá exibir a lista de todas as tarefas cadastradas,
# juntamente com seus status.
# d) Editar tarefa: o usuário deverá informar o título da tarefa e o programa deverá permitir
# a edição do status correspondente (concluída ou não).
# e) Excluir tarefa: o usuário deverá informar o título da tarefa e o programa deverá excluir
# a tarefa da lista.
# f) Sair: encerra o programa.

from biblioteca import libs
from biblioteca.pacote1 import arquivo5

while True:
    libs.linha('\n[1] - ADICIONAR TAREFA\n[2] - CONSULTAR TAREFA\n[3] - LISTAR TAREFAS\n'
               '[4] - EDITAR TAREFAS\n[5] - EXCLUIR TAREFAS\n[6] - SAIR DO PROGRAMA')
    op = libs.lerInt('Sua opção: ')
    if op == 1:
        arquivo5.adicionar_tarefa()
    elif op == 2:
        arquivo5.consultar_tarefa()
    elif op == 3:
        arquivo5.listar_tarefas()
    elif op == 4:
        arquivo5.editar_tarefa()
    elif op == 5:
        arquivo5.excluir_tarefa()
    elif op == 6:
        print('Tenha um bom dia!')
        break
