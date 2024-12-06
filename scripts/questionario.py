import pandas as pd
import config

def questionar():
    respostas = perguntar_genericamente()
    afinidade = calcular_afinidade(respostas)
    sugerir_area_conhecimento(afinidade)
    print(carregar_questionario(config.PATH_QUESTIONARIO))

def perguntar_genericamente():
    perguntas_genericas = [
        "Você gosta de trabalhar com números?",
        "Você prefere atividades ao ar livre?",
        "Você gosta de resolver problemas complexos?",
        "Você prefere atividades práticas ou teóricas?",
        "Você gosta de trabalhar em equipe?",
        "Você prefere trabalhar em ambientes internos ou externos?",
        "Você se interessa por tecnologia?",
        "Você prefere atividades criativas ou analíticas?",
        "Você se interessa por ciências humanas, exatas ou biológicas?",
        "Você gosta de atividades que envolvem comunicação?",
        "Você prefere trabalhar com números ou com pessoas?",
        "Você se interessa por empreendedorismo?",
        # Adicione mais perguntas conforme necessário
    ]

    respostas = []
    for pergunta in perguntas_genericas:
        resposta = "Sim" #input(pergunta + " (Sim/Não): ")
        respostas.append(resposta)
    
    return respostas

def calcular_afinidade(respostas):
    # Definir áreas de conhecimento e suas características
    areas_conhecimento = {
        "Engenharia": [
            "Sim", "Não", "Sim", "Práticas", "Não", "Internos", "Sim", "Analíticas", "Exatas", "Não", "Números", "Sim"
        ],
        "Ciências Humanas": [
            "Não", "Não", "Não", "Teóricas", "Sim", "Internos", "Não", "Criativas", "Humanas", "Sim", "Pessoas", "Sim"
        ],
        "Ciências Biológicas": [
            "Não", "Sim", "Sim", "Práticas", "Não", "Externos", "Não", "Analíticas", "Biológicas", "Não", "Pessoas", "Não"
        ],
        "Tecnologia da Informação": [
            "Sim", "Não", "Sim", "Práticas", "Não", "Internos", "Sim", "Analíticas", "Exatas", "Não", "Números", "Sim"
        ],
        "Artes": [
            "Não", "Não", "Não", "Criativas", "Sim", "Internos", "Não", "Criativas", "Humanas", "Sim", "Pessoas", "Não"
        ],
        "Administração": [
            "Sim", "Não", "Sim", "Práticas", "Sim", "Internos", "Sim", "Analíticas", "Humanas", "Sim", "Pessoas", "Sim"
        ],
    }

    afinidade = {area: 0 for area in areas_conhecimento}
    for i, resposta in enumerate(respostas):
        for area, caracteristicas in areas_conhecimento.items():
            if resposta == caracteristicas[i]:
                afinidade[area] += 1
    return afinidade

def sugerir_area_conhecimento(afinidade):
    area_sugerida = max(afinidade, key=afinidade.get)
    print(f"\nÁrea de conhecimento sugerida: {area_sugerida}")

def carregar_questionario(filepath):
    df = pd.read_csv(filepath)
    return df.head()

if __name__ == "__main__":
    questionar()
