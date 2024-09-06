import unittest
from config import SessionLocal
from crud.pais import criar_pais, ler_pais, atualizar_pais, deletar_pais

class TestPaisCRUD(unittest.TestCase):

    def setUp(self):
        self.db = SessionLocal()
        # Adicione setup inicial

    def tearDown(self):
        # Adicione teardown
        pass

    def test_criar_pais(self):
        pais = criar_pais(self.db, "Brasil", "BR")
        self.assertEqual(pais.nome, "Brasil")
        self.assertEqual(pais.sigla, "BR")

    def test_ler_pais(self):
        pais = ler_pais(self.db, 1)
        self.assertIsNotNone(pais)

    def test_atualizar_pais(self):
        atualizar_pais(self.db, 1, "Brasil Atualizado", "BRU")
        pais = ler_pais(self.db, 1)
        self.assertEqual(pais.nome, "Brasil Atualizado")
        self.assertEqual(pais.sigla, "BRU")

    def test_deletar_pais(self):
        deletar_pais(self.db, 1)
        pais = ler_pais(self.db, 1)
        self.assertIsNone(pais)

if __name__ == '__main__':
    unittest.main()
