# 1 - Desenvolva o sistema de um controle universal para uma casa. O controle deve
# ser a Classe-Mãe, que contém o método liga/desliga e é herdada por outras três
# classes (equipamentos controlados): ar-condicionado, micro-ondas e televisão, que
# controlam, respectivamente, temperatura, tempo e volume em métodos dentro das
# classes. Além disso, os métodos construtores das Classes Filhas recebem a variável
# controlada em seu valor atual, por exemplo 'temperaturaAtual'.
# Obs.: Utilize também propriedades para realizar o acesso aos atributos.



class ControleUniversal:
    def __init__(self):
        self.__ligado = False

    def ligarDesligar(self):
        if self.__ligado:
            self.__ligado = False
            self.__ligado = 'Desligando...'

        else:
            self.__ligado = True
            self.__ligado = 'Ligando...'
    @property
    def ligado(self):
        return self.__ligado

    @ligado.setter
    def ligado(self, value):
        self._ligado = value


class ArCondicionado(ControleUniversal):
    def __init__(self, temperatura_atual):
        super().__init__()
        self.__temperatura_atual = temperatura_atual
    @property
    def temperatura(self):
        return f' A temperatura atual é de: {self.__temperatura_atual}'


class Microondas(ControleUniversal):
    def __init__(self, tempo_atual):
        super().__init__()
        self.__tempo_atual = tempo_atual

    @property
    def tempo_atual(self):
        return f' O tempo atual é de: {self.__tempo_atual()}'

    @tempo_atual.setter
    def tempo_atual(self, novoTempo):
        if self.ligado:
            self.__tempo_atual = novoTempo
            print(f'Temperatura atualizada para {self.__tempo_atual} ')
        else:
            print('O microondas está desligado, ligue-o')


class Televisao(ControleUniversal):
    def __init__(self, volume_atual):
        super().__init__()
        self.__volume_atual = volume_atual

    @property
    def volume_atual(self):
        return f'O volume atual é de: {self.__volume_atual}'

    @volume_atual.setter
    def volume_atual(self, novoVolume):
        if self.ligado:
            self.__volume_atual = novoVolume
            print(f'Volume da televisão atualizado para: {self.__volume_atual} ')
        else:
            print('A televisão precisa ser ligada')


tv = Televisao(23)
print(tv.volume_atual)
tv.ligarDesligar()
tv.volume_atual = 55



