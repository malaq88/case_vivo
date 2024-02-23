from flask import Flask, request, jsonify

app = Flask(__name__)


def contar_elementos(vetor_a):
    contagem = {i: 0 for i in range(16)}

    for elemento in vetor_a:
        if elemento in contagem:  # Adiciona verificação para garantir que o elemento esteja dentro do intervalo esperado
            contagem[elemento] += 1
        else:
            return jsonify({
                               "error": "Elemento fora do intervalo esperado"})  # Retorna um erro se o elemento estiver fora do intervalo

    return contagem


@app.route('/contar-elementos', methods=['POST'])
def contar_elementos_api():
    data = request.json
    vetor_a = data.get('vetor_a', [])

    if not isinstance(vetor_a, list):  # Verifica se vetor_a é uma lista
        return jsonify({"error": "Vetor_A deve ser uma lista"})

    contagem = contar_elementos(vetor_a)

    return jsonify(contagem)


if __name__ == '__main__':
    app.run(debug=True)
