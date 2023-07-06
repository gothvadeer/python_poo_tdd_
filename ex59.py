# 1) Crie dois arquivos: um CSV e um JSONPICKLE. Escreva os lucros de uma
# empresa em um balanço trimestral, apresentando o mês e o lucro em milhões
# no CSV, e as despesas nos mesmos meses em JSONPICKLE a partir dos
# objetos criados com uma classe chamada Empresa. Após isso, troque seus
# conteúdos, ou seja, armazene os valores dos lucros no JSONPICKLE e os
# valores de despesa no CSV.

from csv import writer, reader
import jsonpickle

class Empresa:
    def __init__(self, mes, lucro, despesas):
        self.__mes = mes
        self.__lucro = lucro
        self.__despesas = despesas

    @property
    def mes(self):
        return self.__mes
    @property
    def lucro(self):
        return self.__lucro
    @property
    def despesas(self):
        return self.__despesas
    @despesas.setter
    def despesas(self, value):
        self.__despesas = value

dados_trimestrais = [
Empresa('Janeiro', 8, 10),
Empresa('Fevereiro', 10, 14),
Empresa('Março', 8, 9)]

with open('lucros.csv', 'w', newline='', encoding='utf-8') as arq:
    escrita = writer(arq, delimiter=':')
    escrita.writerow(['Mes', 'Lucro (milhões)'])
    for empresa in dados_trimestrais:
        escrita.writerow([empresa.mes, empresa.lucro])

with open('despesas.json', 'w') as jsonfile:
    jsonfile.write(jsonpickle.encode(dados_trimestrais))

novos_dados = []
with open('lucros.csv', 'r', encoding='utf-8') as arq:
    leitura = reader(arq, delimiter=':')
    next(leitura)
    for row in leitura:
        mes,lucro = row
        novos_dados.append(Empresa(mes, float(lucro), 0))


with open('despesas.json', 'r') as jsonfile:
    dados_antigos = jsonpickle.decode(jsonfile.read())

for i, empresa in enumerate(novos_dados):
    empresa.despesas = dados_antigos[i].despesas

with open('lucros.csv', 'w', newline='', encoding='utf-8') as arq:
    escrever = writer(arq, delimiter=':')
    escrever.writerow(['Mês', 'Despesas (Milhões)'])
    for empresa in novos_dados:
        escrever.writerow([empresa.mes, empresa.despesas])

with open('despesas.json', 'w') as jsonfile:
    jsonfile.write(jsonpickle.encode(novos_dados))
