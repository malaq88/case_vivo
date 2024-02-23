MAX_VOLTAS = 4  # Número máximo de voltas permitidas


def processar_dados(dados):
    resultados = {}
    melhor_volta_corrida = float('inf')

    for linha in dados:
        hora, codigo_heroi, volta, tempo_volta, _ = linha
        codigo_heroi = codigo_heroi.split('-')[0]
        volta = int(volta)

        # Converte tempo para segundos
        tempo_volta = sum(x * float(t) for x, t in zip([60, 1, 1 / 60], tempo_volta.split(':')))

        if volta > MAX_VOLTAS:
            break  # Termina a corrida quando o primeiro colocado completa o número máximo de voltas

        if codigo_heroi not in resultados:
            resultados[codigo_heroi] = {
                'nome': codigo_heroi,
                'quantidade_voltas': 0,
                'tempo_total': 0,
                'melhor_volta': float('inf'),
                'melhor_volta_tempo': float('inf')
            }

        resultados[codigo_heroi]['quantidade_voltas'] = volta
        resultados[codigo_heroi]['tempo_total'] += tempo_volta

        if tempo_volta < resultados[codigo_heroi]['melhor_volta_tempo']:
            resultados[codigo_heroi]['melhor_volta_tempo'] = tempo_volta
            resultados[codigo_heroi]['melhor_volta'] = volta

        if volta == MAX_VOLTAS and tempo_volta < melhor_volta_corrida:
            melhor_volta_corrida = tempo_volta

    return resultados, melhor_volta_corrida
