# Um estudante do Curso Programando Ideias acabou de assistir a aula de
# diferença entre iteráveis e iteradores, para praticar mais, criou um programa
# que realiza o processo de um for, porém sem utilizar a ferramenta for
# diretamente, segue o código desenvolvido:
# O estudante percebeu que o código estava apresentando o seguinte erro:
# TypeError: 'list' object is not an iterator
# Porém, não sabe como corrigir. Altere o programa do estudante para fazer
# funcionar corretamente e explique o que aconteceu.

def desmembra_iteravel(iteravel):
    iterador = iter(iteravel) # foi criado um iter
    while True:
        try:
            print(next(iterador)) # foi trocado pela variável que contem o iter 
        except StopIteration:
            print('Chegamos ao ultimo elemento')
            break


desmembra_iteravel([1, 2, 3, 4, 5, 6, 7, 8])

# usando iterator next e iter
interavel = [1, 43, 88, 59, 22, 11, 39]
interador = iter(interavel)
while True:
    try:
        elemento = next(interador)
        #print(elemento, end=' => ')
    except StopIteration:
        #print('Fim')
        break
