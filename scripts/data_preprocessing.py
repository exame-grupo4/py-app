import pandas as pd
import logging
import config

# Configuração do logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def carregar_dados(caminho_arquivo):
    try:
        # Carregar os dados do CSV
        df = pd.read_csv(caminho_arquivo, sep=";", encoding="latin1")
        logging.info(f"Dados carregados com sucesso de {caminho_arquivo}")
        return df
    except Exception as e:
        logging.error(f"Erro ao carregar dados: {e}")
        return None


def preprocessar_dados(df):
    try:
        # Realizar pré-processamento necessário
        df = df.dropna()  # Exemplo de pré-processamento
        logging.info("Pré-processamento concluído com sucesso")
        return df
    except Exception as e:
        logging.error(f"Erro no pré-processamento dos dados: {e}")
        return None


def preprocessar_cursos(df):
    try:
        # Realizar pré-processamento necessário
        df = df[
            [
                "CO_CURSO",
                "NO_CURSO",
                "NO_CINE_ROTULO",
                "CO_CINE_ROTULO",
                "CO_CINE_AREA_GERAL",
                "NO_CINE_AREA_GERAL",
                "CO_CINE_AREA_ESPECIFICA",
                "NO_CINE_AREA_ESPECIFICA",
                "CO_CINE_AREA_DETALHADA",
                "NO_CINE_AREA_DETALHADA",
            ]
        ]
        # df = df.dropna()  # Exemplo de pré-processamento
        df = df.drop_duplicates()
        logging.info("Pré-processamento concluído com sucesso")
        return df
    except Exception as e:
        logging.error(f"Erro no pré-processamento dos dados: {e}")
        return None


""" if __name__ == "__main__":
    filepath = 'data/raw_data.csv'
    df = carregar_dados(filepath)
    if df is not None:
        df = preprocessar_dados(df)
        if df is not None:
            output_filepath = config.PATH_DADOS_PREPROCESSADOS
            df.to_csv(output_filepath, index=False)
            logging.info(f'Dados pré-processados salvos em {output_filepath}') """
