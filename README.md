# 🧮 Calculadora com While

## Utilizando os quatro operadores aritméticos

![Python](https://img.shields.io/badge/Python-3.7%2B-blue?style=flat-square&logo=python)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow?style=flat-square&logo=javascript)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Contributions](https://img.shields.io/badge/Contribuições-Bem--vindas-orange?style=flat-square)

Uma calculadora **dual-language** desenvolvida em **Python** (terminal) e **JavaScript** (interface web), com foco em estruturas de repetição, tratamento de erros e boas práticas de programação.

[Funcionalidades](#-funcionalidades) · [Instalação](#-instalação) · [Como Usar](#-como-usar) · [Novidades](#-novidades) · [Contribuição](#-contribuição)

---

## 📖 Sobre o Projeto

Este projeto consiste em uma **calculadora interativa dual-language**: o núcleo de cálculo é desenvolvido em **Python** (terminal), com módulos reutilizáveis, enquanto a camada visual é construída em **HTML + CSS + JavaScript**, demonstrando como duas linguagens podem coexistir e se complementar em um mesmo projeto.

A aplicação Python permite realizar operações matemáticas de forma contínua via terminal, com tratamento robusto de erros. A interface web oferece a mesma experiência de forma visual, agora com **histórico de operações** em tempo real.

---

## 🎯 Objetivos de Aprendizado

- ✅ **Estruturas de Repetição**: Dominar o uso do loop `while`
- ✅ **Tratamento de Erros**: Implementar `try/except` para capturar exceções
- ✅ **Módulos Python**: Separar responsabilidades com `import`
- ✅ **Lógica de Programação**: Desenvolver pensamento algorítmico
- ✅ **Validação de Entrada**: Garantir dados consistentes do usuário
- ✅ **Boas Práticas**: Código limpo, bem estruturado e comentado
- ✅ **JavaScript DOM**: Manipulação de interface e histórico dinâmico

---

## 🔧 Funcionalidades

### Núcleo Python (Terminal)

| Operação       | Símbolo | Descrição                            |
|----------------|---------|--------------------------------------|
| Adição         | `+`     | Soma dois números                    |
| Subtração      | `-`     | Subtrai o segundo do primeiro número |
| Multiplicação  | `*`     | Multiplica dois números              |
| Divisão        | `/`     | Divide o primeiro pelo segundo       |

### Interface Web (JavaScript)

| Feature                   | Descrição                                           |
|---------------------------|-----------------------------------------------------|
| `selecionarOperador()`    | Seleciona o operador e destaca o botão ativo        |
| `calcular()`              | Realiza o cálculo com validação completa            |
| `adicionarAoHistorico()`  | ✨ **NOVO** — Registra cada operação no histórico   |
| `renderizarHistorico()`   | ✨ **NOVO** — Re-renderiza a lista de histórico     |
| `limparHistorico()`       | ✨ **NOVO** — Apaga todas as entradas do histórico  |

### Recursos de Segurança

- ✔ Tratamento de divisão por zero
- ✔ Validação de entrada numérica
- ✔ Verificação de operadores válidos
- ✔ Opção de saída controlada (terminal)

---

## ✨ Novidades

### v1.1 — Histórico de Cálculos (JavaScript)

> **Arquivo afetado:** `src/index.html` — bloco `<script>`

Foram adicionadas **3 novas funções JavaScript** ao projeto, sem alterar nenhuma linha do código Python:

#### `adicionarAoHistorico(n1, operador, n2, resultado)`
Registra uma operação no array interno `historicoCalculos`. Mantém no máximo **10 entradas**, inserindo sempre a mais recente no topo (LIFO). Inclui a expressão, o resultado e o **horário** da operação.

```js
// Chamada automática após cada cálculo bem-sucedido em calcular()
adicionarAoHistorico(n1, operadorAtual, n2, valor);
```

#### `renderizarHistorico()`
Re-renderiza toda a lista `#lista-historico` com animação de entrada. Oculta automaticamente a seção quando o histórico está vazio.

#### `limparHistorico()`
Esvazia o array `historicoCalculos` e atualiza a UI, escondendo a seção de histórico.

**Comportamento visual:**
- 📋 A seção aparece na primeira operação realizada
- 🕐 Cada item exibe a expressão completa, o resultado e o horário
- 🔄 Máximo de 10 operações exibidas (a mais antiga é removida)
- 🗑️ Botão "Limpar" apaga todo o histórico

---

## 🗂️ Estrutura do Projeto

```
calculadora-while/
├── src/
│   ├── calculadora.py    # 🐍 Entrypoint Python — loop while + I/O
│   ├── operacoes.py      # 🐍 Módulo Python — lógica de cálculo pura
│   ├── index.html        # 🌐 Interface web — HTML + JS (histórico ✨)
│   └── style.css         # 🎨 Estilos — glassmorphism + animações
├── .gitignore
├── LICENSE
└── README.md
```

### Responsabilidades por Linguagem

| Linguagem      | Arquivo(s)              | Responsabilidade                          |
|----------------|-------------------------|-------------------------------------------|
| **Python**     | `calculadora.py`        | Loop principal, I/O, fluxo do programa    |
| **Python**     | `operacoes.py`          | Lógica de cálculo modularizada            |
| **JavaScript** | `index.html` (inline)   | Interface, validação front-end, histórico |
| **CSS**        | `style.css`             | Visual, animações, responsividade         |

---

## 🚀 Instalação

### Pré-requisitos

- Python 3.7 ou superior
- Navegador moderno (para a interface web)
- Git (opcional)

### Passos

```bash
# 1. Clone o repositório
git clone https://github.com/rafaelmaia-dev/calculadora-while.git

# 2. Navegue até o diretório
cd calculadora-while/src

# 3. Execute o programa Python (terminal)
python calculadora.py

# 4. Ou abra a interface web
# Abra src/index.html diretamente no navegador
```

---

## 📟 Como Usar

### Via Terminal (Python)
1. Execute `python calculadora.py`
2. Digite o primeiro número
3. Digite o segundo número
4. Escolha o operador (`+`, `-`, `*`, `/`)
5. Visualize o resultado
6. Digite `s` ou `sim` para sair

### Via Interface Web (JavaScript)
1. Abra `src/index.html` no navegador
2. Preencha os dois campos numéricos
3. Clique no operador desejado (+, −, ×, ÷)
4. Clique em **Calcular**
5. O resultado aparece e é adicionado automaticamente ao **Histórico** ✨

---

## 💻 Exemplos

### Python — Terminal

```
Digite um número: 20
Digite outro número: 10
Digite um dos operadores ao lado (+, -, *, /): +
20.0 + 10.0 = 30.0
Deseja sair? [s]im: não
```

```
Digite um número: 15
Digite outro número: 0
Digite um dos operadores ao lado (+, -, *, /): /
Erro: Divisão por zero não é permitida.
```

### JavaScript — Interface Web

```
[Entrada]  Primeiro número: 8   Segundo número: 4   Operador: ×
[Saída]    Resultado: 8 × 4 = 32

📋 Histórico
  8 × 4 = 32    14:32:05
```

---

## 🛣️ Roadmap — Features Futuras

> Funcionalidades planejadas para as próximas versões:

### 🐍 Python
- [ ] **Operações avançadas** — potenciação (`**`) e raiz quadrada (`math.sqrt`)
- [ ] **Testes unitários** — cobertura com `unittest` para `operacoes.py`
- [ ] **Exportar histórico** — salvar sessão em arquivo `.txt` ou `.csv`
- [ ] **Calculadora científica CLI** — modo avançado com mais funções matemáticas

### 🌐 JavaScript / Interface Web
- [ ] **Persistência de histórico** — salvar no `localStorage` entre sessões
- [ ] **Tema claro/escuro** — toggle de tema com preferência do sistema
- [ ] **Modo científico** — botões para potência, raiz, porcentagem
- [ ] **Suporte a teclado** — atalhos de teclado para operadores e Enter para calcular
- [ ] **Animação no resultado** — efeito visual ao exibir novo resultado

### 🔗 Integração Python ↔ JS
- [ ] **API Flask/FastAPI** — servir o backend Python como REST API para a interface web
- [ ] **WebAssembly (Pyodide)** — rodar Python direto no navegador

---

## 🤝 Contribuição

Contribuições são sempre bem-vindas! Siga estes passos:

1. **Fork** o projeto
2. **Crie** uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. **Commit** suas mudanças (`git commit -m 'feat: adiciona MinhaFeature'`)
4. **Push** para a branch (`git push origin feature/MinhaFeature`)
5. **Abra** um Pull Request

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👤 Autor

**Rafael Maia**

- GitHub: [@rafaelmaia-dev](https://github.com/rafaelmaia-dev)
- LinkedIn: [Rafael Maia](https://linkedin.com/in/rafaelmaia-dev)

---

### ⭐ Se este projeto foi útil para você, considere dar uma estrela!

_Desenvolvido com ❤️ para fins educacionais_
