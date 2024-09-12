# Olimpiadas BD

Este projeto é uma aplicação de gerenciamento de dados de Olimpíadas, incluindo a criação e manipulação de um banco de dados, bem como a execução da aplicação principal (back-end) e do front-end.

## Pré-requisitos

- Python 3.10 ou superior
- Node.js e npm (para o front-end)
- Pip (gerenciador de pacotes do Python)
- Virtualenv (opcional, mas recomendado para criar um ambiente virtual)

## Configuração do Ambiente

### Configuração do Back-end

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/olimpiadas_bd.git
   cd olimpiadas_bd
   ```

2. **Crie um ambiente virtual (opcional, mas recomendado):**

   ```bash
   python -m venv venv
   ```

3. **Ative o ambiente virtual:**

   - No Windows:

     ```bash
     venv\Scripts\activate
     ```

   - No Linux/Mac:

     ```bash
     source venv/bin/activate
     ```

4. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

### Configuração do Banco de Dados

1. **Crie o banco de dados:**

   Execute o script `create_db.py` que está na pasta `scripts` para criar o banco de dados:

   ```bash
   python scripts/create_db.py
   ```

2. **Popule o banco de dados com os dados iniciais:**

   Execute o script `insert.py` que está na pasta `scripts` para popular o banco de dados:

   ```bash
   python scripts/insert.py
   ```

### Executando o Back-end

1. **Inicie o back-end:**

   Execute o arquivo principal `main.py` para rodar a aplicação:

   ```bash
   python main.py
   ```

### Configuração do Front-end

1. **Acesse o diretório do front-end:**

   ```bash
   cd olimpiadas-app
   ```

2. **Instale as dependências do front-end:**

   ```bash
   npm install
   ```

3. **Inicie o front-end:**

   ```bash
   npm start
   ```

4. **Acesse a aplicação no navegador:**

   A aplicação estará disponível no endereço:

   ```plaintext
   http://localhost:3000
   ```

## Testes

Para rodar os testes do back-end, utilize:

```bash
python -m unittest discover -s tests
```

## Estrutura de Diretórios

- **`database/`**: Contém scripts relacionados ao banco de dados.
- **`models/`**: Define os modelos utilizados na aplicação.
- **`olimpiadas-app/`**: Diretório principal da aplicação front-end.
- **`routes/`**: Define as rotas da aplicação back-end.
- **`scripts/`**: Scripts auxiliares como `create_db.py` e `insert.py`.
- **`static/`**: Arquivos estáticos (CSS, JS, imagens).
- **`tests/`**: Testes unitários e de integração.
- **`venv/`**: Ambiente virtual (não é versionado).

## Problemas Comuns

- **Erro de conexão com o banco de dados:** Verifique se o banco de dados foi criado e populado corretamente.
- **Dependências faltando:** Confirme se as bibliotecas necessárias foram instaladas corretamente com `pip install -r requirements.txt` e `npm install` para o front-end.