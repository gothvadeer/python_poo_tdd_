# Crie um programa em Python que leia um arquivo de texto contendo
# números separados por vírgula e exiba na tela apenas
# os números que são múltiplos de 3.

with open('numeros.txt') as numeros:
    linhas = numeros.readlines()
    separados = [[int(numeros) for numeros in nums.split(',')] for nums in linhas if nums.strip]
    multiplos = [num for nums in separados for num in nums if num % 3 == 0]

print(separados)
print(multiplos)