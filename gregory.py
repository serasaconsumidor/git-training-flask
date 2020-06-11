from flask import Flask, jsonify
app = Flask(__name__)

from datetime import date, datetime

nome = 'Gregory Torres'
numero_de_consultas = 3
score_maximo = 1000
score_minimo = 0

@app.route('/score/gregory/<int:idade>', methods=['GET'])
def calcula_score_gregory(idade):
    fator_risco = calcular_risco(idade)
    if isinstance(fator_risco, str):
        return jsonify(fator_risco)

    dividas = []
    gerar_divida(23, '15/4/2020', dividas)
    gerar_divida(50, '25/5/2020', dividas)

    score = calcular_score(fator_risco, numero_de_consultas, dividas)

    response = {
        "nome": nome,
        "score": score,
        "variaveis": {
            "idade": idade,
            "consultado": numero_de_consultas > 0,
            "dividas": dividas
        }
    }
    return jsonify(response)

def calcular_risco(idade):
    if 18 <= idade <= 19:
        return 3.0
    elif 20 <= idade <= 21:
        return 2.0
    elif idade >= 22:
        return 1.5
    else:
        return 'Idade insuficiente!'

def gerar_divida(valor, str_data, dividas):
    data = gerar_data(str_data)
    dias_atrasado   = calcular_dias_atrasado(data)
    valor_com_juros = calcular_juros(valor, dias_atrasado)
    dividas.append({
        "valor_original": valor,
        "dias_atraso": dias_atrasado,
        "valor_atual": valor_com_juros
    })

def gerar_data(str_data):
    separator = str_data[2]
    data = str_data.split(separator)
    ano = int(data[2])
    mes = int(data[1])
    dia = int(data[0])

    return date(ano, mes, dia)

def calcular_dias_atrasado(data_divida):
    data_atual = date.today()
    resultado = max(0, (data_atual - data_divida).days)
    print(resultado)
    return resultado

def calcular_juros(valor_original, dias_atrasado):
    return valor_original + dias_atrasado

def calcular_score(risco, qtd_consultas, dividas):
    total_dias_atrasados = 0
    for divida in dividas:
        total_dias_atrasados += divida.get('dias_atraso')
    score = (score_maximo / risco) - 50 * qtd_consultas - total_dias_atrasados
    resultado = score_behaviour(score)
    return resultado

def score_behaviour(score):
    score = int(score)
    score = max(score_minimo, score)
    score = min(score_maximo, score)
    return score

def score_limite():
    limites = {
        'max': score_maximo,
        'min': score_minimo
    }
    return limites


if __name__ == "__main__":
    app.run(debug=True, port='8000')