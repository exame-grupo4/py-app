import streamlit as st
import config
import json
from respostas import resultado

from scripts.questionario import (
    calcular_afinidade,
    salvar_respostas_em_csv,
    sugerir_cursos,
)

def questionario():
    st.title("Questionário")
    with open(config.PATH_QUESTIONARIO, 'r', encoding='utf-8') as f:
        perguntas = json.load(f)
    respostas = {}
    for i, pergunta in enumerate(perguntas):
        respostas[f"pergunta_{i}"] = st.selectbox(pergunta['question'], pergunta['options'])
    if st.button("Enviar"):
        afinidade = calcular_afinidade(respostas)

        salvar_respostas_em_csv(perguntas,respostas, afinidade)

        cursos_sugeridos = sugerir_cursos(afinidade)

        resultado(respostas, cursos_sugeridos)

if __name__ == "__main__":
    questionario()
