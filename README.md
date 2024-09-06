```markdown
# Projeto Final da Disciplina de Banco de Dados

Este projeto faz parte da disciplina de Banco de Dados e tem como objetivo demonstrar o uso de PostgreSQL para criar e gerenciar um sistema de banco de dados relacional. O projeto inclui a criação de tabelas, inserção de dados e execução de consultas SQL para manipulação de informações.

## Estrutura do Projeto

- **`main.py`**: Script principal que conecta ao banco de dados, cria as tabelas e insere os registros necessários.
- **`config.py`**: Arquivo de configuração que contém as variáveis de ambiente, como URL do banco de dados e outras configurações.
- **`inserts.py`**: Script que contém as instruções SQL para inserir os dados nas tabelas.
- **`requirements.txt`**: Lista de dependências do projeto necessárias para executar o código Python.

## Tecnologias Utilizadas

- **PostgreSQL**: Sistema de gerenciamento de banco de dados relacional.
- **Python**: Linguagem de programação utilizada para conectar e manipular o banco de dados.
- **psycopg2**: Biblioteca Python para conectar e interagir com o PostgreSQL.

## Configuração e Execução

### Pré-requisitos

- Python 3.x instalado
- PostgreSQL instalado e configurado
- Biblioteca `psycopg2` instalada (pode ser instalada via `requirements.txt`)

### Passo a Passo

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure o banco de dados:

   - Certifique-se de que o PostgreSQL está rodando.
   - Crie um banco de dados conforme necessário.

4. Edite o arquivo `config.py` com as suas credenciais e URL do banco de dados.

5. Execute o script principal:

   ```bash
   python main.py
   ```

## Estrutura do Banco de Dados

O banco de dados inclui as seguintes tabelas:

- **`pais`**: Contém os países participantes.
- **`confederacao`**: Registra as confederações por país.
- **`edicao`**: Lista as edições dos eventos.
- **`modalidade`**: Tipos de modalidades esportivas.
- **`evento`**: Registra os eventos específicos.
- **`equipe`**: Registra as equipes participantes.
- **`atleta`**: Lista os atletas.
- **`medalha`**: Registra as medalhas conquistadas.
- **`historico`**: Histórico de desempenho dos atletas e equipes.
- **Outras tabelas**: Tabelas adicionais para gerenciar os eventos e participações.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Contato

- **Nome**: Guilherme Ribeiro de Macedo
- **Email**: 170162354@aluno.unb.br
- **Universidade**: Universidade de Brasília (UnB)
```
