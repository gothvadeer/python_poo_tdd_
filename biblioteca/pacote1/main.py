from biblioteca import libs
nomeMedia = {}


def formaDicionarioNota():
        with open('notas.txt', 'a+') as nomeNota:
            while True:
                nome = (input('Digite o nome do aluno(a): ')).strip().title()
                notas = (input('Digite os notas separadas por virgula: '))
                nomeNota.write(f'{nome}: {notas}\n')
                nomeNota.seek(0)
                libs.linha('ALUNOS E NOTAS')
                print(nomeNota.read())
                break


def media():
    global nomeMedia
    with open('notas.txt') as arquivo:
        linhas = arquivo.readlines()
        dados = [linha.strip().split(':') for linha in linhas]
        notas = [[float(nota) for nota in aluno[1].split(',')] for aluno in dados]
        media = [sum(nota) / len(nota) for nota in notas]
        libs.linha('ALUNOS E MÉDIA')
        for nota, aluno in enumerate(dados):
            nomeMedia = {aluno[0]: media[nota]}
            print(f'{aluno[0]}, média: {media[nota]:.1f}')
    return nomeMedia


def aprovadosReprovados():
    global nomeMedia
    for nome, media in nomeMedia.items():
        resultado = 'APROVADO' if media >= 6 else 'REPROVADO'
        print(f'{nome}: {resultado}!')
