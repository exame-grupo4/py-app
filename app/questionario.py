import streamlit as st
import requests

st.title("Questionário")

perguntas = [
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

respostas = {}


for i, pergunta in enumerate(perguntas):
    respostas[f"pergunta_{i}"] = st.selectbox(pergunta['question'], pergunta['options'])

if st.button("Enviar"):
    response = requests.post("http://localhost:5000/", data=respostas)
    if response.status_code == 200:
        st.write("Respostas enviadas com sucesso!")
    else:
        st.write("Falha ao enviar respostas.")


st.table(respostas)