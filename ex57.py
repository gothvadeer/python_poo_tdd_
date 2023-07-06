# 1) Um time de futsal formado pelo arquivo atletas.csv, que contém nome,
# altura(cm) e peso(kg) de cada esportista, deseja fazer uma pesquisa e saber
# quais atletas tem altura superior a 170 cm e que possui peso menor que 80 kg,
# imprima o nome deles. Dois reforços entraram para o time no início da
# temporada, Roberto, 175, 77kg e Adriana, 165, 60kg. Atualize o arquivo
# adicionando os jogadores e leia-o novamente.

from csv import reader
from csv import writer

with open('atletas.csv', encoding='utf-8') as arq:
    leitura = reader(arq)
    next(leitura)
    print(f'Os jogadores que são maiores de 1,70cm e pesam menos que 80kg\n'
          f'são: ')
    for linha in leitura:
        altura = int(linha[1])
        peso = int(linha[2])
        if altura > 170 and peso < 80:
            print(f'{linha[0]} com {altura} cm e {peso} kg')
print('=*'*40)
with open('atletas.csv', 'a+', newline='') as arq:
    escrita = writer(arq)
    escrita.writerow(['Roberto', '175','77'])
    escrita.writerow(['Adriana', '165', '60'])
    arq.seek(0)
    leitura = reader(arq)
    next(leitura)
    for linha in leitura:
        print(linha)


