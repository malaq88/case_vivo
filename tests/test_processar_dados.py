import unittest
from api.v1.leitor_log_corrida.processar_dados import processar_dados


class TestProcessarDados(unittest.TestCase):
    def test_processar_dados(self):
        # Dados de exemplo
        dados = [
            ['23:49:08.277', '038–Superman', '1', '1:02.852', '44,275'],
            ['23:49:10.858', '033–Flash', '1', '1:04.352', '43,243'],
            ['23:49:11.075', '002–Mercúrio', '1', '1:04.108', '43,408']
            # Adicione mais dados de exemplo conforme necessário
        ]

        # Resultados esperados
        resultados_esperados = {
            '038–Superman': {'nome': '038–Superman', 'quantidade_voltas': 1, 'tempo_total': 62.852, 'melhor_volta': 1,
                             'melhor_volta_tempo': 62.852},
            '033–Flash': {'nome': '033–Flash', 'quantidade_voltas': 1, 'tempo_total': 64.352, 'melhor_volta': 1,
                          'melhor_volta_tempo': 64.352},
            '002–Mercúrio': {'nome': '002–Mercúrio', 'quantidade_voltas': 1, 'tempo_total': 64.108, 'melhor_volta': 1,
                             'melhor_volta_tempo': 64.108}
            # Adicione mais resultados esperados conforme necessário
        }

        # Chamada do método
        resultados_obtidos, melhor_volta_corrida = processar_dados(dados)

        # Asserts
        self.assertEqual(resultados_obtidos, resultados_esperados)
        self.assertEqual(melhor_volta_corrida, float('inf'))
