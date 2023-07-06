# Crie duas classes (uma para um personagem no video game e outra para o
# controle do console). O controle deve ser capaz de fazer o personagem pular,
# abaixar, desviar para esquerda e desviar para direita, sendo comandado,
# respectivamente, pelas teclas W, A, S e D. Use a dica e a função choice()
# para determinar por onde virá o obstáculo ('Cima', 'Baixo', 'Esquerda' ou
# 'Direita'), e o tempo para o próximo obstáculo, que deve decair com o aumento
# dos pontos. Cada obstáculo passado gera +1 ponto. Ainda, crie um loop infinito
# do jogo até a pessoa perder. Por fim, apresente a pontuação final.
# Dica:
# import time
# time.sleep(3) # O programa 'para' por 3 segundos
from time import sleep
from random import choice


class PersonagemVideoGame:

    pontuacao = 0

    def __init__(self, nome):
        self.nome = nome
        self.pontuacao = PersonagemVideoGame.pontuacao

    def pular(self):
        print(f'{self.nome} pulou para a esquerda!')
        PersonagemVideoGame.pontuacao += 1

    def abaixar(self):
        print(f'{self.nome} abaixou!')
        self.pontuacao += 1

    def desviar_esquerda(self):
        print(f'{self.nome} desviou para a esquerda!')
        self.pontuacao += 1

    def desviar_direita(self):
        print(f'{self.nome} desviou para a direita!')
        self.pontuacao += 1

class Controle:
    def __init__(self, personagem):
        self.personagem = personagem

    def jogar(self):
        print('Iniciando o jogo... ')
        while True:
            obstaculo = choice(['Cima', 'Baixo', 'Esquerda', 'Direita'])
            tempo = 3 / (self.personagem.pontuacao + 1)
            print(f'Proximo obstaculo: {obstaculo}')
            sleep(tempo)
            tecla = input('Digite as teclas "W , A, S e D" para controlar o personagem: ').upper()[0]
            if tecla == 'W':
                self.personagem.pular()
                if obstaculo != 'Cima':
                    print(f'Jogador errou! Pontuação final: {self.personagem.pontuacao}')
                    break
            elif tecla == 'A':
                self.personagem.abaixar()
                if obstaculo != 'Baixo':
                    print(f'Jogador errou! Pontuação final: {self.personagem.pontuacao}')
                    break
            elif tecla == 'S':
                self.personagem.desviar_esquerda()
                if obstaculo != 'Esquerda':
                    print(f'Jogador errou! Pontuação final: {self.personagem.pontuacao}')
                    break
            elif tecla == 'D':
                self.personagem.desviar_direita()
                if obstaculo != 'Direita':
                    print(f'Jogador errou! Pontuação final: {self.personagem.pontuacao}')
                    break
            else:
                print('Tecla inválida')


personagem1 = PersonagemVideoGame('Jogador 1')
controle = Controle(personagem1)
controle.jogar()