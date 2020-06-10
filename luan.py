from flask import Flask, request, jsonify
from datetime import date

app = Flask(__name__)
@app.route('/score/luan', methods = ['GET'])

def calcula_score_luan():
    nome = request.args.get('nome', default=None, type=str)
    idade = request.args.get('idade', default=None, type=int)
    score = 1000
    consulta = 1
    dividas = []
    valor_original = 45.00

    dias_atraso = calcular_dias_atraso()
    valor_atual = valor_original + dias_atraso
    score -= dias_atraso

    if (consulta):
        for consultas in range(consulta):
            score -= 50

    score = calcular_risco(score, idade)

    dividas.append({
        "valor_original": valor_original,
        "dias_atraso": dias_atraso,
        "valor_atual": valor_atual
    })

    resumo = {
        "nome": nome,
        "score": score,
        "variaveis": {
            "idade": idade,
            "consultado": True,
            "dividas": dividas
        }
    }
    return jsonify(resumo)

def calcular_dias_atraso():
    hoje = date.today()
    data_divida = date(2019, 12, 5)
    dias_atraso = (hoje - data_divida).days
    return dias_atraso.__abs__()

def calcular_risco(score, idade):
    if idade < 18:
        score = 0
    elif idade >= 18 and idade <= 19:
        score /= 3
    elif idade >= 20 and idade <= 21:
        score /= 2
    else:
        score /= 1.5
    return score

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)