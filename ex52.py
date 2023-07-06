# - Crie uma classe contendo atributos públicos e privados representando
# objetos pessoais. Após isso, crie uma propriedade pra cada atributo privado.
# Instancie um objeto e faça acesso a todos os atributos. Utilize também o setter,
# para alterar algum valor do objeto.

class Banco:

    def __init__(self, nomeProprietario, senha, limiteBancario):
        self.nomeProprietario = nomeProprietario
        self.__senha = senha
        self.__limiteBancario = limiteBancario

    @property
    def senha(self):
        return f'Sua senha é {self.__senha}'

    @senha.setter
    def senha(self, novaSenha):
        self.__senha = novaSenha
        return f'Senha alterada com sucesso! '

    @property
    def __repr__(self):
        return f'Nome da conta: {self.nomeProprietario}\n' \
               f'Limite: R$ {self.__limiteBancario:,.2f}'


pessoa1 = Banco('Omar', 'valentina123', 23_394_845)
print(pessoa1.__repr__)
pessoa1.senha = 'Olá834y7y57583$$&&'
print(pessoa1.senha)
