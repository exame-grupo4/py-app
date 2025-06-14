from flask import render_template, request, redirect, url_for
import pandas as pd
import config
import logging
from app import app
from scripts.questionario import (
    perguntas_avaliativas,
    calcular_afinidade,
    salvar_respostas_em_csv,
    salvar_sugestao_cursos_em_csv,
    sugerir_cursos,
)

logging.basicConfig(level=logging.INFO)


@app.route("/cursos")
def index():
    logging.info("Rota / acessada")
    try:
        df = pd.read_csv(config.PATH_CURSOS_PREPROCESSADOS)
        logging.info("Dados carregados com sucesso")
        data = df[["NO_CINE_AREA_GERAL"]].to_html()

        return render_template("cursos.html", data=data)
    except Exception as e:
        logging.error(f"Erro ao carregar dados: {e}")
        return f"Erro ao carregar dados: {e}", 500


@app.route("/", methods=["GET", "POST"])
def questionario():
    if request.method == "GET":
        return render_template(
            "questionario.html", perguntas=perguntas_avaliativas, enumerate=enumerate
        )
    else:
        respostas = [
            request.form.get(f"pergunta_{i}") for i in range(len(perguntas_avaliativas))
        ]

        afinidade = calcular_afinidade(respostas)

        salvar_respostas_em_csv(respostas, afinidade)

        cursos_sugeridos = sugerir_cursos(afinidade)

        salvar_sugestao_cursos_em_csv(cursos_sugeridos)

        return redirect(url_for("resultado"))


@app.route("/resultado")
def resultado():
    try:
        df_questionario = pd.read_csv(config.PATH_QUESTIONARIO)
        df_cursos_sugeridos = pd.read_csv(config.PATH_CURSOS_SUGERIDOS)

        questionario_html = df_questionario.to_html()
        df_cursos_sugeridos_html = df_cursos_sugeridos.to_html()

        return render_template(
            "resultado.html",
            questionario=questionario_html,
            cursos_sugeridos=df_cursos_sugeridos_html,
        )
    except Exception as e:
        logging.error(f"Erro ao carregar resultados do questionário: {e}")
        return f"Erro ao carregar resultados do questionário: {e}", 500
