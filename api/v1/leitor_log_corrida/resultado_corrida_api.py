from flask import Flask, jsonify

from api.v1.leitor_log_corrida.calcular_velocidade_media import calcular_velocidade_media
from api.v1.leitor_log_corrida.ler_arquivo_log import ler_arquivo_log
from api.v1.leitor_log_corrida.processar_dados import processar_dados

app = Flask(__name__)

LOG_FILE = '../../../log_corrida.txt'


@app.route('/resultado-corrida')
def resultado_corrida():
    try:
        dados = ler_arquivo_log(LOG_FILE)
        if not dados:
            return jsonify({'error': 'Nenhum dado encontrado no arquivo de log'}), 500

        resultados, melhor_volta_corrida = processar_dados(dados)
        if not resultados:
            return jsonify({'error': 'Erro ao processar os dados'}), 500

        resultados = calcular_velocidade_media(resultados)

        resultado_final = []
        posicao = 1
        for info in sorted(resultados.values(), key=lambda x: x['tempo_total']):
            resultado_final.append({
                'posicao_chegada': posicao,
                'codigo_heroi': info['nome'],
                'quantidade_voltas': info['quantidade_voltas'],
                'tempo_total_prova': info['tempo_total'],
                'velocidade_media': info['velocidade_media'],
                'melhor_volta': info['melhor_volta'],
                'melhor_volta_tempo': info['melhor_volta_tempo']
            })
            posicao += 1

        return jsonify({
            'resultado_final': resultado_final,
            'melhor_volta_corrida': melhor_volta_corrida
        })

    except Exception as e:
        return jsonify({'error': f'Ocorreu um erro inesperado: {str(e)}'}), 500


if __name__ == '__main__':
    app.run(debug=True)
