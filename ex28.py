# Crie 3 listas: uma com o nome de 3 companhias aéreas, e as outras duas
# representando o número de passageiros por companhia em dois voos: voo1 e
# voo2. Utilize zip(), lambda e map() para obter o valor máximo de passageiros
# por companhia nos dois voos e associar estes valores com o nome das
# companhias, formando uma lista de tuplas. Por fim, utilizar filter() e lambda
# para determinar a classificação da companhia, conforme indicado nos dados
# abaixo.
# Dados:
# 0 < Passageiros <= 100: 1 estrela.
# 100 < Passageiros <= 200: 2 estrelas.
# 200 < Passageiros <= 300: 3 estrelas.
companhias = ['Gol', 'Azul', 'Tam']
voo1 = [36, 30, 233]
voo2 = [124, 99, 54]
voo1e2 = zip(voo1, voo2)
maxPass = list(map(lambda voos: max(voos), voo1e2))
compMax = list(zip(companhias, maxPass))
umaEstrela = list(filter(lambda pMax: pMax[1] < 100, compMax))
duasEstrelas = list(filter(lambda pMax: 100 < pMax[1] <= 200, compMax))
tresEstrelas = list(filter(lambda pMax: 200 < pMax[1] <= 400, compMax))
estrela = '\u2605'
print(f'{estrela} {umaEstrela[0][0]} => MÁXIMO DE PASSAGEIROS: {umaEstrela[0][1]}')
print(f'{estrela*2} {duasEstrelas[0][0]} => MÁXIMO DE PASSAGEIROS: {duasEstrelas[0][1]}')
print(f'{estrela*3} {tresEstrelas[0][0]} => MÁXIMO DE PASSAGEIROS: {tresEstrelas[0][1]}')



