# ) Crie uma classe Robo para controlar o objeto R2D2 com os seguintes
# métodos:
#  - Construtor: Recebe como atributo a bateria que varia entre 0 e 100 e cria um
# atributo de instancia chamado estado que apresenta se o robô está ligado ou
# desligado.
# - liga_desliga: Quando esse método é chamado o robô passa a ser ligado caso
# esteja desligado e vice-versa.
# - movimento: Recebe como atributo uma string, que representa qual o lado que
# o robô irá andar e decresce o atributo bateria em 10 para cada execução desse
# método.
# - controle_energia: Imprime os atributos estado e bateria atualizados do Robo.
# Crie uma interface de menu para o Usuário decidir o que irá fazer com o Robo,
# ou seja, qual método irá acessar. Faça tratamento de erros com
# Try/Except/Else/Finally. Trate também as condições especiais como bateria
# zerada o que irá acontecer com o seu R2D2? Dentre outros, fica a cargo de
# cada programador.
from biblioteca import libs

class Robo:
    def __init__(self, bateria, estado):
        self.bateria = bateria
        self.estado = estado.title()

    def liga_desliga(self):
        if self.estado == 'Desligado':
            self.estado = 'Ligado'
            print('Ligando o robô...')
        else:
            self.estado = 'Ligado'
            print('Desligando o robô...')

    def movimento(self, string):
        if self.bateria >= 10:
            self.string = string
            self.bateria -= 10
            print(f'{self.string} e com o movimento perdeu 10 pts')
        elif self.bateria <= 0:
            self.bateria = 0
            self.estado = 'Ligado'
            print('R2D2 está sem bateria! Recarregue imediatamente!')
            self.liga_desliga()

    def controle_energia(self):
        while True:
            libs.montaMenu('[1] - ESTADO DA BATERIA\n'
                           '[2] - RECARREGAR BATERIA\n'
                           '[3] - SAIR')
            op = libs.lerInt('Qual sua opção?: ')
            if op == 1:
                print(f'Sua bateria é de: {self.bateria} %')
            elif op == 2:
                qtd = libs.lerInt('Quanto deseja recarregar? (Só números inteiros): ')
                self.bateria += qtd
                print(f'Sua bateria agora é de {self.bateria} %')
            elif op == 3:
                print('Saindo do programa...')
                break
            else:
                print('Opção inválida!')


r2d2 = Robo(30, 'Ligado')
r2d2.movimento('Ir para direita')
r2d2.movimento('Ir para esquerda')
r2d2.movimento('Ir para frente')
r2d2.movimento('Ir para trás')


