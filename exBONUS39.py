# Você foi contratado para desenvolver um sistema de gerenciamento de livros em uma biblioteca.
# Crie uma classe chamada Livro com os seguintes atributos: titulo, autor, ano_publicacao e disponivel
# (um valor booleano que indica se o livro está disponível para empréstimo ou não).
# Em seguida, crie uma classe chamada Biblioteca que será responsável por armazenar e gerenciar uma lista
# de objetos da classe Livro. Essa classe deve ter os seguintes métodos:
# adicionar_livro: recebe um objeto Livro como parâmetro e adiciona-o à lista de livros da biblioteca.
# listar_livros: exibe na tela os títulos de todos os livros da biblioteca.
# buscar_livro: recebe o título de um livro como parâmetro e verifica se o livro está disponível na biblioteca.
# Se estiver disponível, exibe uma mensagem informando que o livro está disponível para empréstimo.
# Caso contrário, exibe uma mensagem informando que o livro não está disponível.
# emprestar_livro: recebe o título de um livro como parâmetro e verifica se o livro está disponível
# na biblioteca. Se estiver disponível, altera o atributo disponivel para False e exibe uma mensagem
# informando que o livro foi emprestado com sucesso. Caso contrário, exibe uma mensagem informando que
# o livro não está disponível para empréstimo.
# devolver_livro: recebe o título de um livro como parâmetro e verifica se o livro está presente na
# lista de livros da biblioteca. Se estiver presente, altera o atributo disponivel para True e exibe uma
# mensagem informando que o livro foi devolvido com sucesso. Caso contrário, exibe uma mensagem informando
# que o livro não pertence à biblioteca.
# Além disso, adicione as seguintes funcionalidades:
# Ao iniciar a biblioteca, verifique se existe um arquivo chamado "biblioteca.pickle"
# que contém os livros previamente cadastrados. Se o arquivo existir, carregue os dados do arquivo
# e inicialize a biblioteca com esses livros. Caso contrário, crie uma nova biblioteca vazia.
# Adicione um método chamado salvar_biblioteca que salva a lista de livros em um arquivo
# "biblioteca.pickle" para que os dados sejam persistidos.
# Crie um objeto da classe Biblioteca e teste os diferentes métodos para adicionar
# livros, listar livros, buscar livros, emprestar livros e devolver livros.
# Certifique-se de que os dados da biblioteca são salvos e recuperados corretamente usando Pickle.
import pickle
livros = []
class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano_publicacao = ano_publicacao
        self.__disponivel = True

    @property
    def titulo(self):
        return self.__titulo
    @property
    def autor(self):
        return self.__autor
    @property
    def ano_publicacao(self):
        return self.__ano_publicacao
    @property
    def disponivel(self):
        return self.__disponivel
    @disponivel.setter
    def disponivel(self, value):
        self.__disponivel = value

class Biblioteca:
    def adicionar_livro(self, titulo):
        livros.append(titulo)

    def listar_livros(self):
        for livro in livros:
            print(livro.titulo)

    def buscar_livro(self, titulo):
        for livro in livros:
            if livro.titulo == titulo.title():
                print(f'O livro {titulo} está disponível para emprestímo')
            else:
                print(f'Não há registro do livro {titulo} na biblioteca')

    def emprestar_livro(self, titulo):
        livro_encontrado = False
        for livro in livros:
            if livro.titulo == titulo:
                livro_encontrado = True
                if livro.disponivel:
                    livro.disponivel = False
                    print(f'Parabéns, o livro {titulo} emprestado com sucesso!')
                    return
        if livro_encontrado:
            print(f'O livro {titulo} está indisponível para emprestímo no momento')
            return
        else:
            print(f'Não há registro do livro {titulo} na biblioteca')

    def devolver_livro(self, titulo):
        livro_encontrado = False
        for livro in livros:
            if livro.titulo == titulo:
                livro_encontrado = True
                if not livro.disponivel:
                    livro.disponivel = True
                    print(f'Obrigado! Livro {titulo} devolvido com sucesso')
                    return
        if livro_encontrado:
            print(f'O livro {titulo} já foi devolvido anteriormente')
            return
        else:
            print(f'Não existe registro do livro {titulo} na biblioteca')

    def salvar_biblioteca(self):
        with open('biblioteca.pickle', 'wb') as arq:
            pickle.dump(livros, arq)

biblioteca = Biblioteca()
livro1 = Livro('Romeu e Julieta', 'Shakespeare', 1517)
livro2 = Livro('Maus', 'Art Spiegelman', 1980)
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.listar_livros()
biblioteca.emprestar_livro('Maus')
biblioteca.emprestar_livro('Maus')
biblioteca.devolver_livro('Maus')
biblioteca.devolver_livro('Maus')

