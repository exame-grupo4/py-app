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
        # df = df.dropna()  # Exemplo de pré-processamento
        logging.info("Pré-processamento concluído com sucesso")
        return df
    except Exception as e:
        logging.error(f"Erro no pré-processamento dos dados: {e}")
        return None


def preprocessar_cursos(df):
    try:
        df = df[["NO_CINE_AREA_GERAL", "CO_CINE_AREA_GERAL"]]
        df = df.drop_duplicates(subset="CO_CINE_AREA_GERAL")
        logging.info("Pré-processamento de cursos concluído com sucesso")
        return df[["NO_CINE_AREA_GERAL"]]
    except Exception as e:
        logging.error(f"Erro no pré-processamento dos cursos: {e}")
        return None
