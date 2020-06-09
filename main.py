from flask import Flask, render_template
from src.score import calcular

app = Flask(__name__)


@app.route("/score/<nome>/<int:idade>")
def resumo_score(nome=None, idade=0):
    return calcular(nome, idade)


if __name__ == "__main__":
    app.run(debug=True)
