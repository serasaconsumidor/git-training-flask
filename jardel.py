from datetime import date
     
def calcula_score_jardel(idade):
    score = 1000
    dividas = []

    valor_original = 30;
    consultado = 3

    dias = getDias()
    valor_atual = valor_original + dias
    score -= dias
    if(consultado):
        for i in range(consultado):
            score -= 50
    score = score / returnRisco(idade)


    dividas.append({
            "valor_original": valor_original,
            "dias_atraso": dias,
            "valor_atual": valor_atual
    })

    if(consultado is None):
        consulta = False
    else:
        consulta= True


    resumo = {
        "nome": "Jardel",
        "score": score,
        "variaveis": {
            "idade": idade,
            "consultado": consulta,
            "dividas": dividas
        }
    }
    return resumo
def getDias():
    dt_atual = date.today()
    dt_divida = date(2020,5,10)
    dias_divida = (dt_atual-dt_divida).days
    return dias_divida

def returnRisco(idade):
    if(idade < 20):
        return 3
    elif(idade <22):
        return 2
    return 1.5