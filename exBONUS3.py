lista1 = [1, 4, 10, 34, 22, 11]
lista2 = list(map(lambda x: x * 2, lista1))

print(lista2)

um = input('Digite a primeira lista de números, separada por espaços: ').split()
dois = input('Digite a segunda lista de números, separada por espaços: ').split()
umLista = list(map(int, um))
doisLista = list(map(int, dois))
listaEmComum = list(filter(lambda x: x[0] == x[1], zip(umLista, doisLista)))
print(listaEmComum)
