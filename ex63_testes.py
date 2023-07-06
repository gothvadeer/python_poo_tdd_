import unittest
from ex63 import Tatu


class ex63_testes(unittest.TestCase):
    def setUp(self):
        print('Iniciando o teste')
        self.bola = Tatu('Bola')
        self.napoleao = Tatu('Napoleão')

    def test_comer(self):
        self.assertEqual(self.bola.comer(), 'Sou o Bola e estou comendo pizza')

    def test_beber(self):
        self.assertEqual(self.bola.beber(), 'Sou o Bola e estou bebendo suco')

    def test_cavar(self):
        self.assertEqual(self.bola.cavar(), 'Sou o Bola e estou cavando sua grama')

    def test_acasalar(self):
        self.assertEqual(self.bola.acasalar(), 'Sou o Bola e quero um filhote.')

    def tearDown(self):
        print('Teste finalizado')


if __name__ == '__main__':
    unittest.main()