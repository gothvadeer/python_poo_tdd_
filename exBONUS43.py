# Imagine que você é um dono de uma loja virtual e deseja automatizar o processo de envio
# de e-mails promocionais para seus clientes. Para isso, você decide criar um programa
# em Python que agende o envio de e-mails promocionais para todos os sábados do mês.
# A cada sábado, o programa deve selecionar aleatoriamente um produto da sua loja
# e criar um e-mail promocional com informações sobre o produto, como nome,
# descrição e preço. Além disso, o programa também deve adicionar uma mensagem personalizada
# de agradecimento aos clientes e incluir um link para acessar o produto na loja virtual.
# Seu desafio é criar um programa que implemente essa ideia, gerando o conteúdo dos e-mails
# promocionais aleatoriamente e agendando o envio para os sábados do mês. Lembre-se de utilizar
# bibliotecas adequadas para enviar os e-mails.
import datetime
import locale
from random import choice
usuarios = ['Guilherme', 'Luis', 'Laura', 'Carla', 'Raquel', 'Bruna', 'Bianca', 'Joaquim']
class LojaVirtual:
    def __init__(self, produto, descProduto, preco):
        self.__produto = produto
        self.__descProduto = descProduto
        self.__preco = preco

    def email_promocoes(self):
        delta = datetime.timedelta(days=30)
        data_atual = datetime.datetime.now()
        data_final = data_atual + delta
        locale.setlocale(locale.LC_TIME, 'pt_BR.utf-8')
        while data_atual < data_final:
            if data_atual.weekday() == 5:
                print(f'OLÁ, {choice(usuarios).upper()}!\n'
                      f'Hoje é {data_atual.strftime("%A")} e também dia de oferta na nossa loja!\n'
                      f'Estamos com promoção no nosso produto {self.__produto}! Quer conhecer?!\n'
                      f'Produto: {self.__produto}\n'
                      f'Descrição: {self.__descProduto}\n'
                      f'Preço promocional: R$ {self.__preco:.2f}\n'
                      f'\033[32m*Clique aqui para acessar a loja*\033[m')
                print('~'*40)
            data_atual += datetime.timedelta(days=1)


produto = LojaVirtual('Notebook', 'Acer, 1TB, 8GB', 3450.00)
produto.email_promocoes()
