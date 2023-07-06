# - Um escritor de livros pretende escrever e lançar edições para atingir a
# quantia de 1 milhão de reais. Simplesmente por este motivo, crie uma classe
# que receberá em seu método construtor o nome do livro e o número de
# páginas. Além disso, também deve ser criado um atributo no construtor para a
# edição do livro, que será atualizado em uma unidade a cada livro que for
# publicado. Por fim, utilize randint() para gerar um valor entre 0 e 500 mil,
# representando a arrecadação das vendas, o último atributo do construtor.
# Crie o método mágico __repr__ para representar o nome do livro e a edição.
# Ainda, utilize __len__ para determinar o número de páginas de cada livro. Por
# fim, verifique se o valor total de arrecadações atingiu 1 milhão de reais.
from random import randint as r
class Livro:

    def __init__(self, nomeLivro, paginas, edicao, vendas):
        self.nomeLivro = nomeLivro
        self.paginas = paginas
        self.edicao = edicao
        self.vendas = vendas

    def __repr__(self):
        return f'{self.nomeLivro}, ed. {self.edicao}'

    #def __str__(self):
        #return f'{self.nomeLivro}'

    #def __del__(self):
        #print('Objeto livro deletado')

    def __len__(self):
        return self.paginas


livro1 = Livro('O Retrato de Dorian Gray', 189, 5, r(0, 500000))
livro2 = Livro('O Quarto de Giovanni', 234, 10, r(0, 500000))
livro3 = Livro('Me Chame Pelo Seu Nome', 333, 2, r(0, 500000))
print(livro1)
print(f'Livro 1: {len(livro1)} páginas')
print(livro2)
print(f'Livro 2: {len(livro2)} páginas')
print(livro3)
print(f'Livro 3: {len(livro3)} páginas')


totalVendas = livro1.vendas + livro2.vendas + livro3.vendas
if totalVendas >= 1000000:
    print(f'Parabéns! Você conseguiu! Agora você é um milionário, arrecadou ao total R$ {totalVendas}')
else:
    print(f'Ainda não foi dessa vez, seu total de vendas é R$ {totalVendas}')


