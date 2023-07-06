# 1 - A partir da lista apresentada, utilizar List Comprehension para criar outra
# lista apenas com
# animais que comecem com 'C' e que o tamanho de seu nome seja menor ou
# igual a 7. Por fim, imprima
# a nova lista.
# animais = ['Cachorro', 'Cavalo', 'Baleia', 'Gato', 'Urso', 'Carneiro', 'Cabra',
# 'Cobra', 'Coelho',
# 'Mosquito', 'Peixe', 'Macaco']

animais = ['Cachorro', 'Cavalo', 'Baleia', 'Gato', 'Urso', 'Carneiro', 'Cabra',
           'Cobra', 'Coelho', 'Mosquito', 'Peixe', 'Macaco']

# com uma variável
novos_animais = [a for a in animais if a[0] == 'C' and len(a) <= 7]
print(novos_animais)

# Dentro do print
print([a for a in animais if a[0] == 'C' and len(a) <= 7])
