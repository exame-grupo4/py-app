import json
import pandas as pd
import config

def calcular_afinidade(respostas):
    # Definir áreas de conhecimento e suas características
    with open(config.PATH_AREA_CONHECIMENTO, "r", encoding="utf-8") as f:
        areas_conhecimento = json.load(f)

    afinidade = {area: 0 for area in areas_conhecimento}
    for i, resposta in enumerate(respostas.values()):
        for area, caracteristicas in areas_conhecimento.items():
            if resposta in caracteristicas:
                afinidade[area] += 1
    return afinidade

def salvar_respostas_em_csv(perguntas, respostas, afinidade):
    data = {
        "Pergunta": [pergunta['question'] for pergunta in perguntas],
        "Resposta": [respostas[f"pergunta_{i}"] for i in range(len(perguntas))],
        "Afinidade": [afinidade[area] for area in afinidade]
    }
    # Ensure all arrays are of the same length
    max_length = max(len(data["Pergunta"]), len(data["Resposta"]), len(data["Afinidade"]))
    for key in data:
        while len(data[key]) < max_length:
            data[key].append("")
    df_perguntas_respostas = pd.DataFrame(data)
    df_perguntas_respostas.to_csv('respostas.csv', index=False)

def sugerir_cursos(afinidade):
    area_sorteada = sorted(afinidade.items(), key=lambda x: x[1], reverse=True)
    
    df = pd.DataFrame(
        list(area_sorteada), columns=["area_conhecimento", "pontuacao"]
    )

    df = df[df["pontuacao"] > 0]
    
    salvar_sugestao_cursos_em_csv(df)
    
    sugestoes = json.loads(df.to_json(orient="records")) 
    
    return sugestoes

def salvar_sugestao_cursos_em_csv(cursos_sugeridos):
    cursos_sugeridos.to_csv(config.PATH_CURSOS_SUGERIDOS, index=False)
    print(f"Cursos sugeridos salvos em {config.PATH_CURSOS_SUGERIDOS}")