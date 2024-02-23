import unittest
from api.v1.leitor_log_corrida.calcular_velocidade_media import calcular_velocidade_media

class TestCalcularVelocidadeMedia(unittest.TestCase):
    def test_calcular_velocidade_media(self):
        # Dados de entrada para o teste
        resultados = {
            '038': {'tempo_total': 250, 'quantidade_voltas': 4},
            '033': {'tempo_total': 260, 'quantidade_voltas': 4},
            '002': {'tempo_total': 270, 'quantidade_voltas': 4}
        }

        # Executando o método
        resultados_com_velocidade_media = calcular_velocidade_media(resultados)

        # Verificando se os resultados foram calculados corretamente
        self.assertEqual(resultados_com_velocidade_media['038']['velocidade_media'], 6.4)
        self.assertEqual(resultados_com_velocidade_media['033']['velocidade_media'], 6.153846153846154)
        self.assertEqual(resultados_com_velocidade_media['002']['velocidade_media'], 5.925925925925926)
