import pandas as pd
import config

respostas_genericas = []

def perguntar_genericamente():
    perguntas_genericas = [
        "Você gosta de trabalhar com números?",
        "Você prefere atividades ao ar livre?",
        "Você gosta de resolver problemas complexos?",
        "Você prefere atividades práticas ou teóricas?",
        "Você gosta de trabalhar em equipe?",
        "Você prefere trabalhar em ambientes internos ou externos?",
        "Você se interessa por tecnologia?",
        "Você gosta de resolver problemas complexos?",
        "Você prefere atividades criativas ou analíticas?",
        "Você se interessa por ciências humanas, exatas ou biológicas?",
        "Você gosta de atividades que envolvem comunicação?",
        "Você prefere trabalhar com números ou com pessoas?",
        "Você se interessa por empreendedorismo?",
        # Adicione mais perguntas conforme necessário
    ]

    for pergunta in perguntas_genericas:
        resposta = input(pergunta + " (Sim/Não): ")
        respostas_genericas.append(resposta)


# Função para calcular afinidade com áreas de conhecimento
def calcular_afinidade(respostas):

    # Definir áreas de conhecimento e suas características
    areas_conhecimento = {
        "Engenharia": [
            "práticas",
            "tecnologia",
            "resolver problemas complexos",
            "analíticas",
            "ciências exatas",
            "números",
        ],
        "Ciências Humanas": [
            "teóricas",
            "trabalhar em equipe",
            "ciências humanas",
            "comunicação",
            "pessoas",
        ],
        "Ciências Biológicas": [
            "práticas",
            "ambientes externos",
            "ciências biológicas",
            "resolver problemas complexos",
        ],
        "Tecnologia da Informação": [
            "tecnologia",
            "resolver problemas complexos",
            "analíticas",
            "ciências exatas",
            "números",
        ],
        "Artes": ["criativas", "ciências humanas", "comunicação", "atividades criativas"],
        "Administração": [
            "trabalhar em equipe",
            "empreendedorismo",
            "ciências humanas",
            "comunicação",
            "pessoas",
        ],
    }

    afinidade = {area: 0 for area in areas_conhecimento}
    for i, resposta in enumerate(respostas):
        for area, caracteristicas in areas_conhecimento.items():
            if resposta in caracteristicas:
                afinidade[area] += 1
    return afinidade


# Exemplo de respostas de um estudante
respostas_estudante = [
    "práticas",
    "trabalhar em equipe",
    "ambientes internos",
    "tecnologia",
    "resolver problemas complexos",
    "analíticas",
    "ciências exatas",
    "comunicação",
    "números",
    "empreendedorismo",
]

# Calcular afinidade do estudante com as áreas de conhecimento
afinidade_estudante = calcular_afinidade(respostas_estudante)

# Exibir afinidade do estudante com as áreas de conhecimento
print("\nAfinidade do Estudante com as Áreas de Conhecimento:")
for area, afinidade in afinidade_estudante.items():
    print(f"{area}: {afinidade}")


def carregar_questionario(filepath):
    df = pd.read_csv(filepath)
    return df.head()


if __name__ == "__main__":
    perguntar_genericamente()
    print(carregar_questionario(config.PATH_QUESTIONARIO))
