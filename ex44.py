'''def aprovados(func):
    def wrapper(**kwargs):
        aprovados = {chave: (f'nota: {dado}, APROVADO (A)' if dado >= 6 else f'nota: {dado}, REPROVADO (A)')
                     for chave, dado in kwargs.items()}
        return func(**aprovados)
    return wrapper

@aprovados
def alunos(**notas):
    for aluno, nota in notas.items():
        print(f'{aluno}: {nota}')



alunos(Laura=2, Camila=3, Raquel=8, Bruna=10, Kevin=6, Nick=9, Julian=5)'''

