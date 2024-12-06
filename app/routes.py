from flask import Flask, render_template
import pandas as pd
import config

app = Flask(__name__)

@app.route('/')
def index():
    df = pd.read_csv(config.PATH_DADOS_PREPROCESSADOS)
    # Exemplo de visualização simples
    data = df.head().to_html()
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)