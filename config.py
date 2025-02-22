import os

BASE_PATH = os.path.expanduser('~/Repos/gabrielcruzg3/college/py-app/')

PATH_MICRODADOS = os.path.join('/home/g3/Repos/gabrielcruzg3/college/project/microdados_censo_da_educacao_superior_2023/dados/MICRODADOS_CADASTRO_CURSOS_2023.CSV')
PATH_CURSOS_PREPROCESSADOS = os.path.join(BASE_PATH, 'data/cursos_preprocessados.csv')

PATH_QUESTIONARIO = os.path.join(BASE_PATH, 'data/questionario.json')
PATH_AREA_CONHECIMENTO = os.path.join(BASE_PATH, 'data/area_conhecimento.json')
PATH_AFINIDADE = os.path.join(BASE_PATH, 'data/afinidade.csv')
PATH_CURSOS_SUGERIDOS = os.path.join(BASE_PATH, 'data/cursos_sugeridos.csv')
