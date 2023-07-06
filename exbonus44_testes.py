import unittest
from exBONUS44 import ContaCorrente


class ExBONUS44_testes(unittest.TestCase):
    def setUp(self):
        print('Inicializando o teste')
        self.kevin = ContaCorrente('Kevin', 100.0)
        self.bruno = ContaCorrente('Bruno', -19.0)

    def test_conta_corrente_saldo_negativo(self):
        self.assertEqual(self.bruno.verificar_cheque_especial(), 'Cheque especial utilizado')

    def test_conta_corrente_saldo_positivo(self):
        self.assertEqual(self.kevin.verificar_cheque_especial(), 'Saldo positivo')

    def tearDown(self):
        print('Teste finalizado')
