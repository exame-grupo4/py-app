import streamlit as st

def resultado(respostas, cursos_sugeridos):
    st.title("Resultados do Questionário")
    st.header("Cursos Sugeridos")
    st.write(cursos_sugeridos)
    st.header("Questionário")
    st.write(respostas)
    
if __name__ == "__main__":
    resultado()