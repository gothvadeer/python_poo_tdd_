# Desenvolva o sistema de controle de iluminação em uma casa.
# Crie uma classe principal chamada Casa e suas subclasses LuzPrincipal,
# LuzQuarto e LuzCozinha. Cada classe deve ser responsável por controlar o estado de uma luz específica na casa.
# A classe Casa deve conter métodos para controlar as luzes, como acender_luz_principal(),
# apagar_luz_principal(), acender_luz_quarto(), apagar_luz_quarto(), acender_luz_cozinha(), apagar_luz_cozinha(),
# entre outros, de acordo com a necessidade.
# Utilize propriedades para garantir o acesso controlado aos estados das luzes.
# Por exemplo, a propriedade estado em cada classe de luz poderia retornar "ligada" ou "desligada".
# Crie um programa principal para testar o funcionamento do sistema, realizando operações como acender,
# apagar e verificar o estado das luzes em diferentes partes da casa.

class Casa:
    def __init__(self):
        self.__ligado = False

    @property
    def acender_apagar_luzes(self):
        if self.__ligado:
            self.__ligado = True
            print('Ligando luz...')
        else:
            self.__ligado = False
            print('Desligando luz...')
        return self.__ligado

    @acender_apagar_luzes.setter
    def acender_apagar_luzes(self, value):
        self.__ligado = value


class LuzPrincipal(Casa):
    def __init__(self, status_luz):
        super().__init__()
        self.__status_luz = status_luz

    @property
    def status_luz_principal(self):
        print(f'A luz principal está {self.__status_luz}')


class LuzQuarto(Casa):
    def __init__(self, status_luz):
        super().__init__()
        self.__status_luz = status_luz

    @property
    def status_luz_quarto(self):
        print(f'A luz do quarto está {self.__status_luz}')


class LuzCozinha(Casa):
    def __init__(self, status_luz):
        super().__init__()
        self.__status_luz = status_luz

    @property
    def status_luz_cozinha(self):
        return f'A luz da cozinha está {self.__status_luz}'


controle = LuzPrincipal('Desligada')
controle.
controle.status_luz_principal