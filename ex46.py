class Flor:
    flores = 'do campo'
    @classmethod
    def conta_flores(cls):
        print(f'O nome da classe é {cls} e a mãe quer  flores: {cls.flores}')

    def __init__(self, cor, nome):
        self.cor = cor
        self.nome = nome

    def floricultura(self, quantidade, buque):
        self.quantidade = quantidade
        self.buque = buque

    def __presentes(self):
        return f'a {self.nome} é {self.cor}, a quantidade é {self.quantidade}'

    def cria_atributo(self):
        self.preco = 3004

    def buque_ou_nao(self):
        if self.buque == True:
            self.buque = False
        else:
            self.buque = True

FloresMae = Flor('Vermelha', 'Tulipa')
Rosas = Flor('Azuis', 'Rosas do deserto')
FloresMae.cria_atributo()
print(FloresMae.preco)
Rosas.cria_atributo()
print(f'O preço da Rosa é R$ {Rosas.preco:.2f}')
FloresMae.floricultura(12, False)
print(FloresMae.nome)
print(FloresMae.quantidade)
print(FloresMae.buque)
FloresMae.buque_ou_nao()
print(FloresMae.buque)
Flor.conta_flores()
print(FloresMae._Flor__presentes())



