import unittest
from ex65 import Mulher


class Ex65_testes(unittest.TestCase):
    def setUp(self):
        print('Inicializando teste')
        self.bianca = Mulher('Bianca', 60, 747484849, 15, 1500)
        self.joana = Mulher('Joana', 60, 74749339543, 10, 1500)
        self.laura = Mulher('Laura', 50, 74848922849, 10, 1500)

    def test_aposentadoria_passou(self):
        self.assertEqual(self.bianca.aposentadoria(), 'Você poderá se aposentar!')

    def test_aposentadoria_falhou_tempo_trabalho(self):
        self.assertEqual(self.joana.aposentadoria(),
                         'Tem idade para se aposentar, mas não tem tempo de trabalho suficiente!')

    def test_aposentadoria_falhou_idade(self):
        self.assertEqual(self.laura.aposentadoria(), 'Faltam 10 anos para você se aposentar!')

    def test_salario_passou(self):
        self.assertEqual(self.bianca.salario_aposentadoria(), 'R$ 1500.00')

    def test_salario_falhou(self):
        self.assertEqual(self.laura.salario_aposentadoria(), 'Ainda não tem os requisitos para se aponsentar')

    def tearDown(self):
        print('Teste finalizado')


if __name__ == '__main__':
    unittest.main()