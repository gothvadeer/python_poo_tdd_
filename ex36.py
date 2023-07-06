#  Maria e Joao estão jogando bingo em família. Cada um possui uma cartela
# e cada cartela possui 7 números entre 1 e 30, que serão sorteados por uma
# função, utilizando choice(), contida em um módulo customizado, sendo
# acessada apenas se o módulo for importado. Os números das cartelas devem
# ser definidos utilizando comprehensions e choice() no programa principal. O
# primeiro a ter seus 7 números chamados vence. Crie um sistema para
# representar o jogo, como os numeros sorteados e a conferência das cartelas.
# No final apresente o vencedor, os números da cartela do vencedor e os
# números sorteados.
from random import choice as ch
from biblioteca.pacote1 import arquivo2 as arq
numeros = 7
max = 30
sorteador = [num for num in range(1, max+1)]
cartelaM = [sorteador.pop(sorteador.index(ch(sorteador))) for num in range(numeros)]
cartelaJ = [sorteador.pop(sorteador.index(ch(sorteador))) for num in range(numeros)]

arq.sorteio(cartelaM, cartelaJ, max)


