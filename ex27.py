# 1 - Está acontecendo uma gincana na Escola e você foi escolhido(a) para
# realizar o controle da pontuação! Para isso, crie 4 listas (A primeira com nome
# das pessoas que participam da gincana. As outras 3 (cada uma representando
# uma prova) armazenam valores de 0 a 100, ou seja, as notas que cada
# participante obteve. Por fim, utilize zip() para retornar um dicionário
# com o nome de cada aluno como chave e o somatório de suas notas em cada
# prova como valor. Após isso, imprima o participante vencedor


pessoas = ['Adam', 'Ronan', 'Grego', 'Archer']
natacao = [98.8, 99.9, 87.2, 77.9]
atletismo = [88.2, 76.6, 66.3, 55.2]
boxer = [44.9, 100, 87.3, 47.8]
listaNotas = []
vencedor = placar = 0
tabela = zip(natacao, atletismo, boxer)
for notas in tabela:
    listaNotas.append(sum(notas))
tabelaFinal = dict(zip(pessoas, listaNotas))
for participante, pontos in tabelaFinal.items():
    if pontos > placar:
        placar = pontos
        vencedor = participante
print(tabelaFinal)
print(f'O vencedor da gingancana foi: {vencedor} com {placar} pontos')