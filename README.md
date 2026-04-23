```markdown
# 🧮 Calculadora While

<p align="center">
  <img src="https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python" />
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript" />
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5" />
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3" />
  <img src="https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white" alt="Pytest" />
</p>

<p align="center">
  Projeto de calculadora com foco em <strong>lógica de programação</strong>, <strong>estrutura modular</strong> e <strong>experiência básica de interface</strong>, disponível em duas versões: <strong>terminal com Python</strong> e <strong>interface web</strong>.
</p>

---

## 📖 Sobre o projeto

O **Calculadora While** é um projeto funcional desenvolvido para praticar fundamentos essenciais, como estruturas de repetição, tratamento de erros e a separação de responsabilidades entre lógica (Back-end) e visual (Front-end).

A aplicação possui uma versão robusta em **Python** e uma interface moderna em **Web**, aplicando conceitos de *Glassmorphism*.

---

## 🚀 Destaques e Funcionalidades

- ✅ Operações básicas: Adição, Subtração, Multiplicação e Divisão.
- ✅ Loop contínuo com estrutura `while`.
- ✅ Tratamento de **divisão por zero** e entradas inválidas.
- ✅ Estrutura modular (Lógica separada da execução).
- ✅ Interface Web responsiva com feedback visual.
- ✅ **Testes Automatizados** para garantir a integridade dos cálculos.

---

## 🛠️ Tecnologias Utilizadas

- **Lógica/Back-end:** Python 3.x
- **Front-end:** HTML5, CSS3 (Custom Properties), JavaScript (ES6+)
- **QA/Testes:** Pytest
- **Análise de Qualidade:** SonarCloud

---

## 📂 Estrutura do projeto

```text
calculadora-while/
├── src/
│   ├── python/
│   │   ├── __init__.py       # Inicializador do pacote Python
│   │   ├── calculadora.py    # Execução principal no terminal
│   │   └── operacoes.py      # Regras de negócio e cálculos
│   └── web/
│       ├── index.html        # Interface web
│       ├── script.js         # Comportamento da interface
│       └── style.css         # Estilização (Glassmorphism)
├── tests/
│   └── test_operacoes.py     # Testes automatizados
├── LICENSE                   # Licença MIT
├── pytest.ini                # Configurações do Pytest
├── README.md                 # Documentação
└── sonar-project.properties  # Configurações de análise de código
```

---

## ⚙️ Como executar o projeto

### 1) Instalação
```bash
# Clone o repositório
git clone [https://github.com/rafaelmaia-dev/calculadora-while.git](https://github.com/rafaelmaia-dev/calculadora-while.git)

# Acesse a pasta
cd calculadora-while
```

### 2) Executando a Versão Terminal (Python)
```bash
cd src/python
python calculadora.py
```

### 3) Executando a Versão Web
Basta abrir o arquivo `src/web/index.html` em qualquer navegador ou utilizar a extensão **Live Server** no VS Code.

---

## 🧪 Qualidade e Testes

Este projeto utiliza **Pytest** para garantir que as operações matemáticas funcionem corretamente.

Para rodar os testes, instale o pytest e execute na raiz do projeto:
```bash
pip install pytest
pytest
```

---

## 📈 Próximos Passos (Backlog)

- [x] Testes automatizados das operações básicas.
- [ ] Histórico de operações realizadas.
- [ ] Suporte a operações avançadas (porcentagem e potência).
- [ ] Implementação de Modo Escuro (Dark Mode).
- [ ] Deploy da versão web (GitHub Pages/Vercel).

---

## 👨‍💻 Autor

Desenvolvido por **Rafael Maia**.

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/rafaelmaia-dev)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/Rafael Maia/)

---

## 📄 Licença

Este projeto está sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
```
