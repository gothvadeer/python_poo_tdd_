# Deseja-se criar um programa que deixe a formula secreta da coca cola
# criptografada, para isso crie uma classe FormulaCocaCola com atributos
# privados: ingrediente, temperatura (Celsius), açúcar (gramas) e o nome do
# proprietário. Crie uma senha de acesso escolhida pelo usuário, instancie o
# objeto e passe o mesmo para um arquivo PICKLE. Após isso, peça a senha
# para acessar os atributos, caso esteja correta, leia o arquivo e imprima-os, se
# não imprima um aviso de acesso negado.
import pickle


class FormulaCocaCola:
    def __init__(self, ingredientes, temperatura, acucar, nomeProprietario):
        self.__ingredientes = ingredientes
        self.__temperatura = temperatura
        self.__acucar = acucar
        self.__nomeProprietario = nomeProprietario

    def __repr__(self):
        return f'Ingredientes:\n' \
               f'{self.__ingredientes}\n' \
               f'Temperatura: {self.__temperatura}\n' \
               f'Açúcar: {self.__acucar}\n' \
               f'Proprietário: {self.__nomeProprietario}'


formula = FormulaCocaCola('Água, Dióxito de carbono, Aciculantes, Aromatizantes, '
                          'Corantes, Cafeína', '20c','300g', 'James Quincey')

with open('formula.pickle', 'wb') as arq:
    pickle.dump(formula,arq)

senha = input('Digite a senha: ')
if senha == 'aB3x8R':
    with open('formula.pickle', 'rb') as arq:
        formula = pickle.load(arq)
        print(formula.__repr__)
else:
    print('Senha errada! Acesso negado.')
