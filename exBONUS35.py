# Crie uma hierarquia de classes de veículos, com uma classe base chamada Veiculo.
# Essa classe deve ter os métodos ligar, desligar e andar.
# A partir da classe base Veiculo, crie duas classes derivadas: Carro e Moto.
# Ambas as classes devem adicionar métodos específicos e substituir os métodos da classe base, se necessário.
# A classe Carro deve ter um método adicional chamado abrir_portas,
# que imprime uma mensagem informando que as portas estão sendo abertas.
# Além disso, ela deve substituir o método andar para imprimir uma mensagem específica para o carro.
# A classe Moto deve ter um método adicional chamado acelerar,
# que imprime uma mensagem informando que a moto está acelerando.
# Além disso, ela deve substituir o método ligar para imprimir uma mensagem específica para a moto.
# Crie objetos das classes Carro e Moto e chame os métodos para verificar o comportamento correto de cada veículo.
# Lembre-se de utilizar a herança e os conceitos de polimorfismo para garantir a estrutura correta
# das classes e a execução adequada dos métodos.

class Veiculo:
    def __init__(self, veiculo):
        self.__veiculo = veiculo

    def ligar(self):
        if isinstance(self, Moto):
            artigo = 'uma'
        else:
            artigo = 'um'
        print(f'Sou {artigo} {self.__veiculo} e estou ligando...')

    def desligar(self):
        if isinstance(self, Moto):
            artigo = 'uma'
        else:
            artigo = 'um'
        print(f'Sou {artigo} {self.__veiculo} e estou desligando...')

    def andar(self):
        if isinstance(self, Moto):
            artigo = 'uma'
        else:
            artigo = 'um'
        print(f'Sou {artigo} {self.__veiculo} e estou andando...')

    @property
    def veiculo(self):
        return self.__veiculo


class Carro(Veiculo):
    def __init__(self, veiculo):
        super().__init__(veiculo)

    def abrir_portas(self):
        print(f'Eu sou um {self.veiculo} e estou abrindo as portas')


class Moto(Veiculo):
    def __init__(self, veiculo):
        super().__init__(veiculo)

    def acelerar(self):
        print(f'Sou uma {self.veiculo} e estou acelerando...')


carro = Carro('Porche')
carro.abrir_portas()
carro.ligar()
carro.desligar()
carro.andar()
moto = Moto('Suzuki')
moto.ligar()
moto.acelerar()
moto.desligar()
