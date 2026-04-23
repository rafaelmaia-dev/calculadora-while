# Calculadora While

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.13" />
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5" />
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3" />
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=000" alt="JavaScript" />
  <img src="https://img.shields.io/badge/Pytest-Testes-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white" alt="Pytest" />
</p>

## 📌 Sobre o projeto

O **Calculadora While** é um projeto educacional que implementa uma calculadora simples com os quatro operadores aritméticos básicos:

- Soma
- Subtração
- Multiplicação
- Divisão

O projeto possui **duas formas de uso**:

- **CLI em Python**, com repetição usando `while`
- **Interface Web**, feita com HTML, CSS e JavaScript

Além disso, o repositório conta com **testes automatizados**, **cobertura de código** e **integração contínua com GitHub Actions + SonarCloud**.

---

## ✨ Funcionalidades

- Operações aritméticas básicas (`+`, `-`, `*`, `/`)
- Tratamento de operador inválido
- Tratamento de divisão por zero
- Execução contínua no terminal com `while`
- Interface web responsiva e visual moderno
- Histórico de operações no navegador com `localStorage`
- Testes unitários com `pytest`
- Pipeline de CI para validação automática

---

## 🗂️ Estrutura do projeto

```bash
calculadora-while/
├── .github/
│   └── workflows/
│       └── ci.yml
├── src/
│   └── python/
│       ├── __init__.py
│       ├── calculadora.py
│       └── operacoes.py
├── tests/
│   └── test_operacoes.py
├── web/
│   ├── index.html
│   ├── script.js
│   └── style.css
├── .gitignore
├── LICENSE
├── pytest.ini
├── README.md
└── sonar-project.properties
```

---

## 🧠 Organização do código

### `src/python/calculadora.py`
Arquivo principal da versão em terminal. Responsável por:

- receber os valores digitados pelo usuário
- solicitar o operador
- chamar a função de cálculo
- repetir a execução até o usuário escolher sair

### `src/python/operacoes.py`
Contém a regra de negócio da calculadora:

- soma
- subtração
- multiplicação
- divisão
- validação de operador
- tratamento de divisão por zero

### `tests/test_operacoes.py`
Arquivo de testes unitários da função principal de operações.

### `web/index.html`
Estrutura da interface web.

### `web/script.js`
Lógica da calculadora no navegador, incluindo:

- cálculo das operações
- seleção de operador
- mensagens de erro
- histórico persistido com `localStorage`

### `web/style.css`
Responsável pela aparência da interface, com layout responsivo e visual moderno.

---

## 🚀 Como executar o projeto

### 1) Clonar o repositório

```bash
git clone https://github.com/rafaelmaia-dev/calculadora-while.git
cd calculadora-while
```

---

## ▶️ Executando a versão Python

### Pré-requisitos

- Python 3.13+ recomendado

### Rodando no terminal

```bash
python src/python/calculadora.py
```

---

## 🌐 Executando a versão Web

Você pode abrir diretamente o arquivo:

```bash
web/index.html
```

Ou subir um servidor local simples:

```bash
cd web
python -m http.server 8000
```

Depois, acesse no navegador:

```bash
http://localhost:8000
```

---

## 🧪 Executando os testes

Instale as dependências de teste:

```bash
pip install pytest pytest-cov
```

Depois execute:

```bash
pytest
```

Se quiser ver cobertura:

```bash
pytest --cov=src/python --cov-report=term-missing
```

---

## ⚙️ Integração contínua

O projeto possui uma pipeline configurada com **GitHub Actions** para:

- executar testes automaticamente
- gerar cobertura
- integrar análise com **SonarCloud**

Isso ajuda a manter a qualidade do código e facilita evolução do projeto.

---

## 💡 Possíveis melhorias

- Adicionar `requirements.txt`
- Criar deploy da versão web
- Exibir badges dinâmicas de build e cobertura
- Melhorar documentação de instalação
- Adicionar testes para a interface web
- Separar melhor lógica e apresentação na versão front-end

---

## 👨‍💻 Autor

Desenvolvido por **Rafael Maia**  
GitHub: [@rafaelmaia-dev](https://github.com/rafaelmaia-dev)

---

## 📄 Licença

Este projeto está sob a licença MIT.
Consulte o arquivo [LICENSE](LICENSE) para mais informações.
```

---
