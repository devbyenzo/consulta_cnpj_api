# 🔍 Consulta CPF & CNPJ com Python

Aplicação desenvolvida em Python para realizar consultas de **CPF** e **CNPJ** utilizando APIs externas e interface gráfica moderna com **CustomTkinter**.

---

# 📌 Tecnologias Utilizadas

* Python 3
* CustomTkinter
* Requests

---

# 📂 Estrutura do Projeto

```bash
consulta-cpf-cnpj/
│
├── main.py
├── requirements.txt
└── README.md
```

---

# 🚀 Funcionalidades

* Consulta de CPF
* Consulta de CNPJ
* Interface gráfica moderna
* Tratamento de erros com `try` e `except`
* Verificação automática de conexão
* Limpeza automática de caracteres inválidos
* Feedback visual de status

---

# 🖥️ Pré-requisitos

Antes de executar o projeto, instale:

* Python 3.10 ou superior

Download oficial:

https://www.python.org

---

# ⚙️ Instalação

## 1. Clone o repositório

```bash
git clone https://github.com/seuusuario/consulta-cpf-cnpj.git
```

## 2. Acesse a pasta do projeto

```bash
cd consulta-cpf-cnpj
```

## 3. Crie um ambiente virtual (Opcional)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# 📦 Instalação das Dependências

## Instale manualmente

```bash
pip install customtkinter requests
```

## Ou utilize o requirements.txt

```txt
customtkinter
requests
```

Depois execute:

```bash
pip install -r requirements.txt
```

---

# ▶️ Como Executar

Execute o arquivo principal:

```bash
python main.py
```

---

# 🧠 Explicação do Código

## Importação das Bibliotecas

```python
import customtkinter as ctk
import requests
```

* `customtkinter` → interface gráfica moderna
* `requests` → requisições HTTP para APIs

---

## Configuração Visual

```python
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
```

Define:

* Tema escuro
* Tema verde da interface

---

## Função Principal

```python
def consultar():
```

Responsável por:

1. Capturar o documento digitado
2. Identificar se é CPF ou CNPJ
3. Realizar requisição para API
4. Processar os dados
5. Exibir informações na tela
6. Tratar possíveis erros

---

## Limpeza dos Dados

```python
documento = "".join(filter(str.isdigit, entrada_dados.get()))
```

Remove:

* pontos
* traços
* barras
* caracteres inválidos

Mantendo apenas números.

---

## Consulta de CPF

```python
url = f"https://api.cpfhub.io/cpf/{documento}"
```

Utiliza API externa para buscar:

* Nome
* Data de nascimento

---

## Consulta de CNPJ

```python
url = f"https://api.opencnpj.org/{documento}?dataset=receita"
```

Busca informações como:

* Razão social
* Situação cadastral
* Data de início das atividades

---

# ⚠️ Tratamento de Erros

O sistema utiliza tratamento de exceções com:

```python
try:
```

e:

```python
except:
```

---

## Erros Tratados

### Erro de SSL

```python
except requests.exceptions.SSLError:
```

### Falha de conexão

```python
except requests.exceptions.ConnectionError:
```

### Erros gerais

```python
except Exception as e:
```

---

# 💡 Melhorias Futuras

* Histórico de consultas
* Exportação para PDF
* Sistema de login
* Tema dinâmico
* Consulta de CEP
* Consulta de telefone
* Barra de carregamento
* Salvamento local

---

# ✅ Boas Práticas Aplicadas

* Tratamento de exceções
* Interface amigável
* Organização simples
* Separação da lógica em função
* Feedback visual para o usuário

---

# 🔒 Observações

* Algumas APIs podem possuir limite de requisições.
* O funcionamento depende da disponibilidade das APIs externas.
* Utilize apenas para fins educacionais e pessoais.

---

# 📸 Interface da Aplicação

```text
+----------------------------------+
|       Consulta CPF/CNPJ          |
|                                  |
|     [ CPF ▼ ]                    |
|                                  |
| [ Digite o documento         ]   |
|                                  |
|         [ Consultar ]            |
|                                  |
| Nome: João da Silva              |
| Nascimento: 01/01/2000           |
+----------------------------------+
```

---

# 👨‍💻 Autor

Projeto desenvolvido para estudos de:

* Python
* APIs
* Interface gráfica
* Requisições HTTP
* Tratamento de erros

---

# ⭐ Contribuição

Contribuições são bem-vindas.

Faça um fork do projeto e envie um pull request.

---

# 📄 Licença

Este projeto está sob a licença MIT.
