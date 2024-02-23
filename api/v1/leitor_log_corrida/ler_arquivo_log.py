def ler_arquivo_log(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()[1:]  # Ignora a primeira linha (cabeçalho)
            dados = [linha.strip().split(';') for linha in linhas]  # Separa os dados de cada linha
        return dados
    except FileNotFoundError:
        print(f'O arquivo "{nome_arquivo}" não foi encontrado.')
        return []  # Retorna uma lista vazia se o arquivo não for encontrado
    except Exception as e:
        print(f'Ocorreu um erro ao ler o arquivo "{nome_arquivo}": {e}')
        return None  # Retorna None em caso de erro para indicar falha na leitura do arquivo
