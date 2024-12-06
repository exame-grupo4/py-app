# Projeto de Educação Superior

Este projeto contém dados sobre instituições de ensino superior no Brasil, incluindo informações sobre localização, organização acadêmica, funcionários técnico-administrativos e docentes.

## Instalação

Para instalar as bibliotecas necessárias, siga os passos abaixo:

1. Clone o repositório:
    ```bash
    git clone https://github.com/gabrielcruzg3/college/project.git
    cd project
    ```

2. Crie um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

Para utilizar o projeto, siga os passos abaixo:

1. Ative o ambiente virtual:
    ```bash
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

2. Execute o script principal:
    ```bash
    python main.py
    ```

## Estrutura do Projeto

- `dicionário_dados_educação_superior.xlsx`: Arquivo Excel contendo o dicionário de dados.
- `cadastro_ies.csv`: Arquivo CSV com os dados das instituições de ensino superior.
- `requirements.txt`: Arquivo com as bibliotecas necessárias para o projeto.
- `main.py`: Script principal para execução do projeto.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).