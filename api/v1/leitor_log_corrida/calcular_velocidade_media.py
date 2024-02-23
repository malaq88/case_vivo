def calcular_velocidade_media(resultados):
    for codigo_heroi, info in resultados.items():
        tempo_total = info['tempo_total']
        quantidade_voltas = info['quantidade_voltas']
        info['velocidade_media'] = (quantidade_voltas * 400) / tempo_total  # 400 é a distância da pista em metros

    return resultados
