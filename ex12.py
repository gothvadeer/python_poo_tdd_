# 1 - A partir da lista apresentada, criar um Generator contendo apenas animais
# que comecem com 'C' ou 'A' e que o tamanho de seu nome seja maior que 5.
# Por fim, itere e imprima o Generator.
# listaAnimais = ['Cachorro', 'Avestruz', 'Alce', 'Cavalo', 'Baleia', 'Gato', 'Urso',
# 'Abelha',
# 'Carneiro', 'Cabra', 'Cobra', 'Coelho', 'Mosquito', 'Peixe', 'Macaco', 'Aranha']

listaAnimais = ['Cachorro', 'Avestruz', 'Alce', 'Cavalo', 'Baleia', 'Gato', 'Urso',
                'Abelha', 'Carneiro', 'Cabra', 'Cobra', 'Coelho', 'Mosquito', 'Peixe', 'Macaco', 'Aranha']

tuplaAnimais = (animal for animal in listaAnimais if animal[0] == 'C' or animal[0] == 'A' and len(animal) > 5)
for i in tuplaAnimais:
    print('=> ', i)

