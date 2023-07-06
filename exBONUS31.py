# Crie uma classe chamada Veiculo que represente um veículo. O construtor da classe
# deve receber o modelo e a cor do veículo. A classe deve ter um método chamado
# acelerar, que imprime uma mensagem informando que o veículo está acelerando.
# Crie três objetos da classe Veiculo, cada um representando um veículo diferente.
# Em seguida, chame o método acelerar para cada um dos veículos criados, exibindo
# a mensagem de aceleração para cada um deles.

class Veiculo:
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor

    def acelerar(self, boolean):
        if boolean == True:
            print(f'{self.modelo} está acelerando...')
        else:
            print(f'{self.modelo} está desligando...')


veiculo1 = Veiculo('Ford Mustang', 'Amarelo')
veiculo1.acelerar(True)
veiculo1.acelerar(False)
veiculo2 = Veiculo('Chevrolet Camaro', 'Vermelho')
veiculo2.acelerar(True)
veiculo3 = Veiculo('BMW M3', 'Preto')
veiculo3.acelerar(True)
veiculo3.acelerar(False)
