import pandas as pd
import config
from scripts.data_preprocessing import preprocessar_cursos, carregar_dados

def questionar():
    # Preprocessar cursos
    df = carregar_dados(config.PATH_MICRODADOS)
    df = preprocessar_cursos(df)
    df.to_csv(config.PATH_CURSOS_PREPROCESSADOS, index=False)
    
    # Realizar questionário
    respostas = perguntar_genericamente()
    afinidade = calcular_afinidade(respostas)
    area_sugerida = max(afinidade, key=afinidade.get)
    cursos_sugeridos = sugerir_cursos(area_sugerida)
    salvar_respostas(respostas, afinidade)
    show_questionario()
    print(f"\nCursos sugeridos para a área de {area_sugerida}:")
    for curso in cursos_sugeridos:
        print(curso)

def show_questionario():
    print("Questionário: \n")
    print(carregar_questionario(config.PATH_QUESTIONARIO))
    print("\nAfinidade: \n")
    print(carregar_afinidade(config.PATH_AFINIDADE))

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

def perguntar_genericamente():

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

def salvar_respostas(respostas, afinidade):
    df_perguntas_respostas = pd.DataFrame({
        'pergunta': perguntas_genericas,
        'resposta': respostas
    })
    
    df_afinidade = pd.DataFrame(list(afinidade.items()), columns=['area_conhecimento', 'pontuacao'])
    
    df_perguntas_respostas.to_csv(config.PATH_QUESTIONARIO, index=False)
    df_afinidade.to_csv(config.PATH_AFINIDADE, index=False)
    
    print(f"Respostas salvas em {config.PATH_QUESTIONARIO}")
    print(f"Afinidade salva em {config.PATH_AFINIDADE}")

def carregar_questionario(filepath):
    df_perguntas_respostas = pd.read_csv(filepath)
    return df_perguntas_respostas.head()

def carregar_afinidade(filepath):
    df_afinidade = pd.read_csv(filepath)
    return df_afinidade.head()

def sugerir_cursos(area_sugerida):
    df = pd.read_csv(config.PATH_CURSOS_PREPROCESSADOS, sep=';', encoding='latin1')
    cursos_disponiveis = df['NO_CINE_AREA_GERAL'].unique()
    return cursos_disponiveis

if __name__ == "__main__":
    questionar()
