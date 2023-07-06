## Crie uma classe chamada Personagem que irá receber como construtor o
# nome completo, altura, peso e resistência (0-100) do personagem, além disso,
# também crie um método que se chame poder que conterá todos os atributos de
# instancia como privado não sendo possível alterá-los, sendo estes: magia,
# persuasão, agilidade e forca, cada um avaliada de 0 a 100, por fim, retorne
# apenas a soma de todos os pontos fornecidos. Crie 3 objetos personagens e
# imprima o nome completo e quantidade de poder total do mais forte.

class Personagem:
    def __init__(self, nomeCompleto, altura, peso, resistencia):
        self.nomeCompleto = nomeCompleto
        self.altura = altura
        self.peso = peso
        self.resistencia = resistencia

    def poder(self, magia, persuasao, agilidade, forca):
        self.__magia = magia
        self.__persuasao = persuasao
        self.__agilidade = agilidade
        self.__forca = forca
        return magia + persuasao + agilidade + forca

dict_poder = {}
superman = Personagem('Clark Kent', 2.8, 90, 12000)
dict_poder[superman.nomeCompleto] = superman.poder(200, 400, 1000, 1000)

loki = Personagem('Loki Asgard', 1.88, 70, 1000)
dict_poder[loki.nomeCompleto] = loki.poder(400, 400, 100, 200)

batman = Personagem('Bruce Wayne', 1.87, 88, 1000)
dict_poder[batman.nomeCompleto] = batman.poder(0, 1000, 200, 300)

maior = 0
nome = ''
for k, v in dict_poder.items():
    if maior < v:
        maior = v
        nome = k
print(f'O mais poderoso é {nome} com o poder de {maior}')