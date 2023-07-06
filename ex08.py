# Crie duas listas, uma para o carrinho do supermercado que irá receber
# produtos comprados e outra para os preços dos produtos. Utilizando um loop,
# preencha as listas com 5 produtos e 5 preços, recebendo estes dados do
# usuário (input). Por fim, some os preços, imprima o valor total e os produtos do
# carrinho.
def linha(text):
    print('~*' * len(text))
    print(f'{text}'.center(len(text) + 20))
    print('~*' * len(text))
    return


linha('SUPERMERCADO BOM DE PREÇO')
lista_produtos = []
lista_precos = []
for c in range(1, 6):
    try:
        lista_produtos.append(str(input(f'{c}ª Produto: ')).strip().capitalize())
        lista_precos.append(float(input('Preço: ')))
    except ValueError:
        print('Inválido! Tente novamente')
linha('PRODUTO            PREÇO')
for compras, precos in zip(lista_produtos, lista_precos):
    print(f'{compras}'.rjust(15),  f'R$ {precos:.2f}'.rjust(20))
print('~'*40)
print(f'Quantidade: {len(lista_produtos)}, Total: R$ {sum(lista_precos):.2f}')
