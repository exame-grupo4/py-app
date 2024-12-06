from flask import render_template_string, render_template
import pandas as pd
import config
import logging
from app import app

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
