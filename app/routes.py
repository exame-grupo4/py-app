from flask import render_template_string, render_template, request, redirect, url_for
import pandas as pd
import config
import logging
from app import app
from scripts.questionario import perguntas_genericas, calcular_afinidade, salvar_respostas

logging.basicConfig(level=logging.INFO)

@app.route("/")
def index():
    logging.info('Rota / acessada')
    try:
        df = pd.read_csv(config.PATH_DADOS_PREPROCESSADOS)
        logging.info('Dados carregados com sucesso')
        data = df.head().to_html()
        
        html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Visualização de Dados</title>
        </head>
        <body>
            <h1>Dados das Instituições de Ensino Superior</h1>
            <div>{data}</div>
        </body>
        </html>
        """
        
        return render_template_string(html)
    except Exception as e:
        logging.error(f'Erro ao carregar dados: {e}')
        return f"Erro ao carregar dados: {e}", 500

@app.route("/questionario", methods=["GET", "POST"])
def questionario():
    if request.method == "POST":
        respostas = [request.form.get(f"pergunta_{i}") for i in range(len(perguntas_genericas))]
        afinidade = calcular_afinidade(respostas)
        salvar_respostas(respostas, afinidade)
        return redirect(url_for('resultado'))
    
    # html = """
    # <!DOCTYPE html>
    # <html lang="en">
    # <head>
    #     <meta charset="UTF-8">
    #     <title>Questionário</title>
    # </head>
    # <body>
    #     <h1>Questionário</h1>
    #     <form method="post">
    #         {% for i, pergunta in enumerate(perguntas) %}
    #             <div>
    #                 <label for="pergunta_{{ i }}">{{ pergunta }}</label>
    #                 <select name="pergunta_{{ i }}" id="pergunta_{{ i }}">
    #                     <option value="Sim">Sim</option>
    #                     <option value="Não">Não</option>
    #                 </select>
    #             </div>
    #         {% endfor %}
    #         <button type="submit">Enviar</button>
    #     </form>
    # </body>
    # </html>
    # """
    return render_template('questionario.html', perguntas=perguntas_genericas)

@app.route("/resultado")
def resultado():
    try:
        df_questionario = pd.read_csv(config.PATH_QUESTIONARIO)
        df_afinidade = pd.read_csv(config.PATH_AFINIDADE)
        
        questionario_html = df_questionario.to_html()
        afinidade_html = df_afinidade.to_html()
        
        html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Resultados do Questionário</title>
        </head>
        <body>
            <h1>Resultados do Questionário</h1>
            <div>{questionario_html}</div>
            <h2>Afinidade</h2>
            <div>{afinidade_html}</div>
        </body>
        </html>
        """
        
        return render_template_string(html)
    except Exception as e:
        logging.error(f'Erro ao carregar resultados do questionário: {e}')
        return f"Erro ao carregar resultados do questionário: {e}", 500
