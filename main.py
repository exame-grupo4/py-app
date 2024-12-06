from scripts.data_preprocessing import carregar_dados, preprocessar_dados
from scripts.questionario import questionar
from app import app
import config

if __name__ == "__main__":
    # Pré-processar dados
    df = carregar_dados(config.PATH_MICRODADOS)
    df = preprocessar_dados(df)
    df.to_csv(config.PATH_DADOS_PREPROCESSADOS, index=False)
    
    # Executar questionário
    questionar()
    
    # Iniciar aplicação Flask
    app.run(debug=True)