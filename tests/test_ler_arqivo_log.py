import unittest
from api.v1.leitor_log_corrida.resultado_corrida_api import ler_arquivo_log


class TestLerArquivoLog(unittest.TestCase):
    def test_ler_arquivo_log(self):
        # Caminho para o arquivo de log de teste
        arquivo_log_teste = 'arquivo_de_log_teste.txt'

        # Chamada do método ler_arquivo_log
        resultado = ler_arquivo_log(arquivo_log_teste)

        # Verificar se o resultado não é vazio
        self.assertTrue(resultado)

        # Verificar se o resultado possui a estrutura esperada
        # (lista de tuplas com cinco elementos cada)
        for linha in resultado:
            self.assertIsInstance(linha, list)
            self.assertEqual(len(linha), 5)
