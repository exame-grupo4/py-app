from flask import render_template_string, render_template, request, redirect, url_for
import pandas as pd
import config
import logging
from app import app
from scripts.questionario import perguntas_genericas, calcular_afinidade, salvar_respostas, sugerir_cursos

logging.basicConfig(level=logging.INFO)

@app.route("/cursos")
def index():
    logging.info('Rota / acessada')
    try:
        df = pd.read_csv(config.PATH_CURSOS_PREPROCESSADOS)
        logging.info('Dados carregados com sucesso')
        data = df[['NO_CINE_AREA_GERAL']].to_html()
        
        return render_template('cursos.html', data=data)
    except Exception as e:
        logging.error(f'Erro ao carregar dados: {e}')
        return f"Erro ao carregar dados: {e}", 500

@app.route("/", methods=["GET", "POST"])
def questionario():
    if request.method == "POST":
        respostas = [request.form.get(f"pergunta_{i}") for i in range(len(perguntas_genericas))]
        afinidade = calcular_afinidade(respostas)
        salvar_respostas(respostas, afinidade)
        return redirect(url_for('resultado'))
    
    return render_template('questionario.html', perguntas=perguntas_genericas, enumerate=enumerate)

@app.route("/resultado")
def resultado():
    try:
        df_questionario = pd.read_csv(config.PATH_QUESTIONARIO)
        df_afinidade = pd.read_csv(config.PATH_AFINIDADE)
        
        questionario_html = df_questionario.to_html()
        afinidade_html = df_afinidade.to_html()
        
        df_cursos = pd.read_csv(config.PATH_CURSOS_PREPROCESSADOS)
        cursos_sugeridos = df_cursos['NO_CINE_AREA_GERAL'].unique()
        
        cursos_html = "<ul>"
        for curso in cursos_sugeridos:
            cursos_html += f"<li>{curso}</li>"
        cursos_html += "</ul>"
        
        return render_template('resultado.html', questionario=questionario_html, afinidade=afinidade_html, cursos=cursos_html)
    except Exception as e:
        logging.error(f'Erro ao carregar resultados do questionário: {e}')
        return f"Erro ao carregar resultados do questionário: {e}", 500
