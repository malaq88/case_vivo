## Documentação da API de Processamento de Log de Corrida de Super-Heróis

Esta API processa um arquivo de log contendo informações sobre uma corrida de super-heróis e retorna diversas estatísticas relevantes sobre a corrida e seus participantes.

### Rotas

#### `/resultado-corrida`

- **Método:** GET
- **Descrição:** Processa o arquivo de log fornecido e retorna as estatísticas da corrida em formato JSON.
- **Parâmetros:**
  - `<arquivo>`: Nome do arquivo de log a ser processado.
- **Retorno:**
  - Lista de dicionários contendo as seguintes informações para cada super-herói:
    - Posição de Chegada: Posição final do super-herói na corrida.
    - Código do Super-herói: Código identificador único do super-herói.
    - Nome Super-herói: Nome do super-herói.
    - Quantidade de Voltas Completadas: Número total de voltas completadas pelo super-herói.
    - Tempo Total de Prova: Tempo total gasto pelo super-herói na corrida.

### Exemplo de Uso

#### Requisição

```
GET /resultado-corrida
```

#### Resposta

```json
[
    {
        "Posição de Chegada": 1,
        "Código do Super-herói": "Superman",
        "Nome Super-herói": "Superman",
        "Quantidade de Voltas Completadas": 4,
        "Tempo Total de Prova": "00:08:15.068"
    },
    {
        "Posição de Chegada": 2,
        "Código do Super-herói": "Flash",
        "Nome Super-herói": "Flash",
        "Quantidade de Voltas Completadas": 4,
        "Tempo Total de Prova": "00:08:16.086"
    },
    ...
]
```

### Notas Adicionais

- A primeira linha do arquivo de log é ignorada, assumindo que seja um cabeçalho.
- A corrida termina quando o primeiro colocado completa 4 voltas.
- Além das estatísticas básicas, a API também pode fornecer informações adicionais, como a melhor volta de cada super-herói, a melhor volta da corrida e a velocidade média de cada super-herói durante toda a corrida.

Esta é a documentação básica da API de Processamento de Log de Corrida de Super-Heróis. Ela fornece uma visão geral das rotas disponíveis, seus parâmetros e o formato das respostas esperadas.