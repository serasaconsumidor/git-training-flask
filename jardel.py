# IDADE:
# TEM DIVIDA: SIM (30 reais no dia 10/05/2020)
# CONSULTA NOS ÚLTIMOS 3 MESES: SIM (3) 

# from datetime import date
import datetime, json
from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/score/jardel', methods=['GET'])
def calcula_score_jardel():
    nome = request.args.get('name', default=None, type=str)
    idade = request.args.get('age', default=None, type= int)
    score = 1000

    dividas = []
    valor_original = 30
    data = '2020-05-10'
    consultado = 3
    dias = get_dias(data)
    valor_atual = valor_original + dias
    score -= dias

    if(consultado):
        consulta = True
        for consult in range(consultado):
            score -= 50
    else:
        consulta= False
        
    score = return_risco(idade, score)

    dividas.append({
            "valor_original": valor_original,
            "dias_atraso": dias,
            "valor_atual": valor_atual
    })

    resumo = {
        "nome": nome,
        "score": score,
        "variaveis": {
            "idade": idade,
            "consultado": consulta,
            "dividas": dividas
        }
    }
    
    if request.method == 'GET':
        return jsonify(resumo)
    else:
        return json.dumps(resumo)

def get_dias(data):
    dt_atual = datetime.date.today()
    dt_divida = datetime.datetime.strptime(data, '%Y-%m-%d').date()
    dias_divida = (dt_atual- dt_divida).days
    return dias_divida

def return_risco(idade, score):
    if(idade < 20):
        return score / 3
    elif(idade < 22):
        return score / 2
    return score / 1.5

if __name__ == '__main__':
    app.run(debug=True, port=8000)