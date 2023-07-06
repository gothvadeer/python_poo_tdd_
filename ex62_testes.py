from ex62 import acordar_cedo, tempo_exercicio, tem_exercicio
import unittest


class Ex62(unittest.TestCase):
    def setUp(self):
        print('Iniciando teste')
        
    def test_acordar_cedo(self):
        self.assertIs(type(acordar_cedo()), str, 'Não é um numero inteiro')

    def test_tempo_exercicio_concluido(self):
        self.assertEqual(tempo_exercicio(3, 66), 65)

    def test_tempo_exercicio_falha(self):
        self.assertEqual(self, 3, 66)

    def test_tem_exercicio_False(self):
        self.assertFalse(tem_exercicio(), 'Descanso')

    def test_tem_exercicio_True(self):
        self.assertTrue(tem_exercicio(), 'Treino: Natação')

    def tearDown(self):
        print('Teste finalizado')

if __name__ == '__main__':
    unittest.main()

