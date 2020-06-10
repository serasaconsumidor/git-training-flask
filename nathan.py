from datetime import datetime as dt
from flask import Flask, request, jsonify
import json
# IDADE:
# TEM DIVIDA: SIM (38 reais no dia 09/11/2019)
# CONSULTA NOS ÚLTIMOS 3 MESES: SIM (1)
app = Flask(__name__)

def calcular_divida():
    valor = 0
    data_atual = dt.today()
    data_divida = dt(day=9, month=11, year=2019)
    dias_atraso = (data_atual - data_divida).days
    valor = dias_atraso + 38.00
    return valor

def consulta_cpf(consultado, n_consulta):
    score = 0
    if consultado == True:
        score -= 50 * n_consulta
        return score

def risco(idade):
    try:
        if idade == 18 or idade == 19:
            return 3
        elif idade == 20 or idade == 21:
            return 2
        elif idade >= 22:
            return 1.5
        else:
            print("Você ainda não possui idade para utulizar esse aplicativo")
    except:
        print('')

@app.route('/score/nathan', methods = ['GET'])
def score_nathan():
    nome = request.args.get('nome', default=None, type=str)
    idade = request.args.get('idade', default=None, type=int)
    score = 1000
    consultado = True
    n_consulta = 3

    dias_atraso = calcular_divida()
    score -= dias_atraso
    score -= consulta_cpf(consultado, n_consulta)
    score /= risco(idade)

    score = int(score)

    valor_atual = dias_atraso + 38.00

    resposta = {
        "nome": nome,
        "score": score,
        "variaveis": {
            "idade": idade,
            "consultado": consultado,
            "qtd_consulta": n_consulta,
            "dividas": [{
                "valor_original": 38.00,
                "dias_atraso": dias_atraso,
                "valor_atual": valor_atual
            }]
        }
    }
    if request.method == 'GET':
        return jsonify(resposta)
    else:
        return json.dumps(resposta)

if __name__ == '__main__':
    app.run(debug=True, port=8000)