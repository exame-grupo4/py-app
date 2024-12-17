import streamlit as st
import pandas as pd

def resultado(respostas, cursos_sugeridos, afinidade):
    st.title("Resultados do Questionário")
    
    st.header("Cursos Sugeridos")
    df_cursos = pd.DataFrame(cursos_sugeridos)
    st.table(df_cursos)
    
    st.header("Questionário")
    df_respostas = pd.DataFrame(list(respostas.items()), columns=["Pergunta", "Resposta"])
    st.table(df_respostas)
    
    st.header("Afinidade por Área de Conhecimento")
    df_afinidade = pd.DataFrame(list(afinidade.items()), columns=["Área de Conhecimento", "Pontuação"])
    st.bar_chart(df_afinidade.set_index("Área de Conhecimento"))
    
if __name__ == "__main__":
    resultado()