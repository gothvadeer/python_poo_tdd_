# Escreva um programa Python que leia um arquivo de texto contendo números inteiros,
# um por linha, e calcule a soma de todos os números pares presentes no arquivo.
with open('17.txt') as numeros:
    listaNum = [int(num.strip()) for num in numeros]
    pares = list(filter(lambda x: x % 2 == 0, listaNum))
print(listaNum)
if pares:
    print(f'Os números pares são: {pares}')
    print(f'A soma dos números pares é: {sum(pares)}')
else:
    print(f'Não há números pares na lista')