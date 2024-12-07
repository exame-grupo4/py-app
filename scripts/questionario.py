import pandas as pd
import config
from scripts.data_preprocessing import preprocessar_cursos, carregar_dados

perguntas_avaliativas = [
    {"question": "Você gosta de trabalhar com números?", "options": ["Sim", "Não"]},
    {"question": "Você prefere atividades ao ar livre?", "options": ["Sim", "Não"]},
    {
        "question": "Você gosta de resolver problemas complexos?",
        "options": ["Sim", "Não"],
    },
    {
        "question": "Você prefere atividades práticas ou teóricas?",
        "options": ["Práticas", "Teóricas"],
    },
    {"question": "Você gosta de trabalhar em equipe?", "options": ["Sim", "Não"]},
    {
        "question": "Você prefere trabalhar em ambientes internos ou externos?",
        "options": ["Internos", "Externos"],
    },
    {"question": "Você se interessa por tecnologia?", "options": ["Sim", "Não"]},
    {
        "question": "Você prefere atividades criativas ou analíticas?",
        "options": ["Criativas", "Analíticas"],
    },
    {
        "question": "Você se interessa por ciências humanas, exatas ou biológicas?",
        "options": ["Humanas", "Exatas", "Biológicas"],
    },
    {
        "question": "Você gosta de atividades que envolvem comunicação?",
        "options": ["Sim", "Não"],
    },
    {
        "question": "Você prefere trabalhar com números ou com pessoas?",
        "options": ["Números", "Pessoas"],
    },
    {"question": "Você se interessa por empreendedorismo?", "options": ["Sim", "Não"]},
    # Adicionar mais perguntas conforme necessário ou ler de um csv
]

def calcular_afinidade(respostas):
    # Definir áreas de conhecimento e suas características
    areas_conhecimento = {
        "Programas básicos": [
            "Sim",
            "Não",
            "Sim",
            "Práticas",
            "Não",
            "Internos",
            "Sim",
            "Analíticas",
            "Exatas",
            "Não",
            "Números",
            "Sim",
        ],
        "Negócios, administração e direito": [
            "Sim",
            "Não",
            "Sim",
            "Práticas",
            "Sim",
            "Internos",
            "Sim",
            "Analíticas",
            "Humanas",
            "Sim",
            "Pessoas",
            "Sim",
        ],
        "Ciências naturais, matemática e estatística": [
            "Sim",
            "Não",
            "Sim",
            "Práticas",
            "Não",
            "Internos",
            "Sim",
            "Analíticas",
            "Exatas",
            "Não",
            "Números",
            "Sim",
        ],
        "Educação": [
            "Não",
            "Não",
            "Não",
            "Teóricas",
            "Sim",
            "Internos",
            "Não",
            "Criativas",
            "Humanas",
            "Sim",
            "Pessoas",
            "Sim",
        ],
        "Ciências sociais, comunicação e informação": [
            "Não",
            "Não",
            "Não",
            "Criativas",
            "Sim",
            "Internos",
            "Não",
            "Criativas",
            "Humanas",
            "Sim",
            "Pessoas",
            "Não",
        ],
        "Engenharia, produção e construção": [
            "Sim",
            "Não",
            "Sim",
            "Práticas",
            "Não",
            "Internos",
            "Sim",
            "Analíticas",
            "Exatas",
            "Não",
            "Números",
            "Sim",
        ],
        "Computação e Tecnologias da Informação e Comunicação (TIC)": [
            "Sim",
            "Não",
            "Sim",
            "Práticas",
            "Não",
            "Internos",
            "Sim",
            "Analíticas",
            "Exatas",
            "Não",
            "Números",
            "Sim",
        ],
        "Serviços": [
            "Sim",
            "Não",
            "Sim",
            "Práticas",
            "Sim",
            "Internos",
            "Sim",
            "Analíticas",
            "Humanas",
            "Sim",
            "Pessoas",
            "Sim",
        ],
        "Artes e humanidades": [
            "Não",
            "Não",
            "Não",
            "Criativas",
            "Sim",
            "Internos",
            "Não",
            "Criativas",
            "Humanas",
            "Sim",
            "Pessoas",
            "Não",
        ],
        "Agricultura, silvicultura, pesca e veterinária": [
            "Não",
            "Sim",
            "Sim",
            "Práticas",
            "Não",
            "Externos",
            "Não",
            "Analíticas",
            "Biológicas",
            "Não",
            "Pessoas",
            "Não",
        ],
        "Saúde e bem-estar": [
            "Não",
            "Sim",
            "Sim",
            "Práticas",
            "Sim",
            "Internos",
            "Não",
            "Analíticas",
            "Biológicas",
            "Não",
            "Pessoas",
            "Não",
        ],
    }

    afinidade = {area: 0 for area in areas_conhecimento}
    for i, resposta in enumerate(respostas):
        for area, caracteristicas in areas_conhecimento.items():
            if resposta == caracteristicas[i]:
                afinidade[area] += 1
    return afinidade

def salvar_respostas_em_csv(respostas, afinidade):
    df_perguntas_respostas = pd.DataFrame(
        {
            "pergunta": [pergunta["question"] for pergunta in perguntas_avaliativas],
            "resposta": respostas,
        }
    )

    df_afinidade = pd.DataFrame(
        list(afinidade.items()), columns=["area_conhecimento", "pontuacao"]
    )

    df_perguntas_respostas.to_csv(config.PATH_QUESTIONARIO, index=False)
    df_afinidade.to_csv(config.PATH_AFINIDADE, index=False)

    print(f"Respostas salvas em {config.PATH_QUESTIONARIO}")
    print(f"Afinidade salva em {config.PATH_AFINIDADE}")

def sugerir_cursos(afinidade):
    area_sorteada = sorted(afinidade.items(), key=lambda x: x[1], reverse=True)
    
    df = pd.DataFrame(
        list(area_sorteada), columns=["area_conhecimento", "pontuacao"]
    )

    df = df[df["pontuacao"] > 0]
    
    return df

def salvar_sugestao_cursos_em_csv(cursos_sugeridos):
    cursos_sugeridos.to_csv(config.PATH_CURSOS_SUGERIDOS, index=False)
    print(f"Cursos sugeridos salvos em {config.PATH_CURSOS_SUGERIDOS}")