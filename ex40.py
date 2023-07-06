# ) Teste se um arquivo chamado livros.txt não exista pela abertura x, caso o
# arquivo já exista abra como w+, utilize Try/Except nessa manipulação. Imprima
# na tela qual foi o modo de abertura, escreva no bloco o nome dos três melhores
# livros que você já leu (um em cada linha) adicionando ao arquivo, feche-o.
# Abrao novamente e adicione mais um livro ao final do arquivo sem apaga-lo, por fim,
# leia a versão final.
try:
    with open('livros.txt', 'x') as livros:
        print('Este arquivo foi feito com "x"')
except FileExistsError:
    with open('livros.txt', 'w+') as livros:
        print('Este arquivo foi feito com "w+"')
        livros.write('Uma vida pequena\n')
        livros.write('Morro dos ventos uivantes\n')
        livros.write('Demian\n')
with open('livros.txt', 'a+') as livros:
    livros.write('Me chame pelo seu nome\n')
    livros.seek(0)
    print(livros.read())

