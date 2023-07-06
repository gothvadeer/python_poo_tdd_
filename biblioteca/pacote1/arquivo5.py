from biblioteca import libs


def adicionar_tarefa():
    while True:
            nomeTarefa = str(input('Nome da tarefa: ')).title().strip()
            statusTarefa = str(input('Status: ')).title().strip()
            with open('tarefas.txt', 'a') as arquivo:
                arquivo.writelines(f'{nomeTarefa}; {statusTarefa}\n')
                print(f'Tarefa adicionada com sucesso!')
            while True:
                mais = str(input('Deseja adicionar mais tarefas?[S/N]: ')).strip().upper()[0]
                if mais in 'SN':
                    if mais == 'S':
                        break
                    else:
                        break
                else:
                    print('ERRO! Use "S" para SIM e "N" para NÃO')
                    continue
            break


def consultar_tarefa():
    nomeBusca = str(input('Digite a tarefa para a consulta: ')).strip().title()
    tarefaExiste = False
    with open('tarefas.txt', 'r') as arquivo:
        conteudo = arquivo.readlines()
        for linha in conteudo:
            tarefa, status = linha.strip().split(';')
            if nomeBusca == tarefa:
                tarefaExiste = True
                print('~'*30)
                print(f'Tarefa: {tarefa}\nStatus: {status}')
        if not tarefaExiste:
            print(f'{nomeBusca} não existe na lista de tarefas!')


def listar_tarefas():
    with open('tarefas.txt', 'r') as a:
        arquivo = a.readlines()
        print(f'TAREFA'.rjust(10), f'STATUS'.rjust(30))
        print('~'*45)
        for linhas in arquivo:
            tarefa, status = linhas.strip().split(';')
            print(f'{tarefa}'.ljust(25), f'{status}'.rjust(20))


def editar_tarefa():
    print(f'[1] - EDITAR TAREFA\n[2] - EDITAR STATUS')
    op = libs.lerInt('Sua opção: ')
    nomeBusca = str(input('Tarefa que deseja editar: ')).strip().title()
    with open('tarefas.txt', 'r') as arquivo:
        conteudo = arquivo.readlines()
        tarefaExiste = False
        for i, linha in enumerate(conteudo):
                tarefa, status = linha.strip().split(';')
                if nomeBusca == tarefa:
                    tarefaExiste = True
                    if op == 1:
                        novaTarefa = str(input('Nova tarefa: ')).strip().title()
                        conteudo[i] = f'{novaTarefa};{status}\n'
                        print('Tarefa atualizada com sucesso!')
                    elif op == 2:
                        novoStatus = str(input('Novo status: ')).strip().title()
                        conteudo[i] = f'{tarefa};{novoStatus}\n'
                        print('Tarefa atualizada com sucesso!')
                        break
        if not tarefaExiste:
            print(f'{nomeBusca} não existe na lista!')
        else:
            with open('tarefas.txt', 'w') as a:
                a.writelines(conteudo)

def excluir_tarefa():
    nomeBusca = str(input('Digite qual tarefa excluir: ')).strip().title()
    with open('tarefas.txt', 'r') as arquivo:
        conteudo = arquivo.readlines()
    tarefaExiste = False
    for i, linha in enumerate(conteudo):
        tarefa, status = linha.strip().split(';')
        if nomeBusca == tarefa:
            tarefaExiste = True
            del conteudo[i]
            print(f'{nomeBusca} deletado com sucesso!')
            break
    if not tarefaExiste:
        print(f'{nomeBusca} não existe na lista de tarefas!')
    else:
        with open('tarefas.txt', 'w') as a:
            a.writelines(conteudo)

