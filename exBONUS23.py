# Exercício para gerenciamento de uma lista de contatos:
# 1 - Faça um programa para gerenciar uma lista de contatos.
# Cada contato deve ter os seguintes campos: nome, telefone e email.
# O programa deve ter um menu com as seguintes opções:
# a) Adicionar contato: o usuário deverá informar o nome, telefone e email do contato.
# Essas informações devem ser armazenadas em um arquivo chamado "contatos.txt".
# b) Consultar contato: o usuário deverá informar o nome do contato e o programa deverá exibir
# o telefone e o email correspondentes.
# c) Listar contatos: o programa deverá exibir a lista de todos os contatos cadastrados,
# juntamente com seus telefones e emails.
# d) Editar contato: o usuário deverá informar o nome do contato e o programa deverá permitir
# a edição do telefone e/ou email correspondentes.
# e) Excluir contato: o usuário deverá informar o nome do contato e o programa deverá excluir
# o contato da lista.
# f) Sair: encerra o programa.

from biblioteca import libs
from biblioteca.pacote1 import arquivo4

while True:
    libs.linha('\n[1] - ADICIONAR CONTATO\n[2] - CONSULTAR CONTATO\n[3] - LISTAR CONTATOS\n'
               '[4] - EDITAR CONTATO\n[5] - EXCLUIR CONTATO\n[6] - SAIR')
    op = libs.lerInt('Sua opção: ')
    if op == 1:
        arquivo4.adicionar_contato()
    elif op == 2:
        arquivo4.consultar_contato()
    elif op == 3:
        arquivo4.listar_contato()
    elif op == 4:
        arquivo4.editar_contato()
    elif op == 5:
        arquivo4.deletar_contato()
    elif op == 6:
        print('Tenha um bom dia!')
        break
