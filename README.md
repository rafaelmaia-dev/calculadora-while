# Calculadora While

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python badge" />
  <img src="https://img.shields.io/badge/JavaScript-ES6-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript badge" />
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML badge" />
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS badge" />
</p>

<p align="center">
  Projeto de calculadora com foco em <strong>lógica de programação</strong>, <strong>estrutura modular</strong> e <strong>experiência básica de interface</strong>, disponível em duas versões: <strong>terminal com Python</strong> e <strong>interface web</strong>.
</p>

---

## Sobre o projeto

O **Calculadora While** é um projeto simples e funcional desenvolvido para praticar fundamentos importantes de programação, como:

- estrutura de repetição com `while`
- entrada e saída de dados
- tratamento de erros
- separação de responsabilidades
- integração entre lógica e interface

A aplicação possui uma versão principal em **Python**, executada no terminal, e uma versão complementar com **HTML, CSS e JavaScript**, oferecendo uma interface mais visual para o usuário.

---

## Destaques

- ✅ Operações aritméticas básicas: adição, subtração, multiplicação e divisão  
- ✅ Loop contínuo no terminal usando `while`  
- ✅ Tratamento de **divisão por zero**  
- ✅ Validação de operador inválido  
- ✅ Estrutura modular com separação entre execução e regras de negócio  
- ✅ Interface web com seleção visual de operadores  
- ✅ Layout moderno com visual em estilo glassmorphism  

---

## 🧠 Objetivo

Este projeto foi criado com foco em aprendizado e evolução prática, servindo como exercício para reforçar conceitos essenciais de desenvolvimento.

Além de resolver um problema simples, ele demonstra boas práticas como:

- organização de arquivos
- reutilização de código
- clareza na lógica
- preocupação com a experiência de uso

---

## 🛠️ Tecnologias utilizadas

### Back-end / lógica
- **Python**

### Front-end
- **HTML5**
- **CSS3**
- **JavaScript**

---

## 📂 Estrutura do projeto

```bash
calculadora-while/
├── src/
│   ├── calculadora.py   # execução principal no terminal
│   ├── operacoes.py     # regras de negócio e operações aritméticas
│   ├── index.html       # interface web
│   ├── script.js        # comportamento da interface
│   └── style.css        # estilização da aplicação
└── README.md
```

---

## Como executar o projeto

### 1) Clonar o repositório

```bash
git clone https://github.com/rafaelmaia-dev/calculadora-while.git
```

### 2) Acessar a pasta do projeto

```bash
cd calculadora-while
```

---

## Executando a versão Python

Acesse a pasta `src` e execute o arquivo principal:

```bash
cd src
python calculadora.py
```

### Exemplo de uso no terminal

```bash
Digite um número: 10
Digite outro número: 2
Digite um dos operadores ao lado (+, -, *, /): /
10.0 / 2.0 = 5.0

Deseja sair? [s]im:
```

---

## 🌐 Executando a versão web

Abra o arquivo `src/index.html` diretamente no navegador.

Se preferir, você também pode usar uma extensão como **Live Server** no VS Code para rodar localmente com mais praticidade.

---

## 🔎 Funcionalidades

### Versão terminal
- leitura de dois números
- escolha do operador matemático
- cálculo do resultado
- repetição contínua até o usuário decidir sair

### Versão web
- campos para os dois números
- seleção de operador por botões
- exibição do resultado na tela
- mensagens de erro para entradas inválidas

---

## ⚠️ Validações e tratamento de erros

O projeto já contempla algumas validações importantes:

- operador inválido
- divisão por zero
- entradas não numéricas na interface web
- cálculo sem operador selecionado

Esses cuidados tornam a aplicação mais confiável e demonstram atenção à robustez do código, mesmo em um projeto simples.

---

## 🎨 Interface

A interface web foi construída com foco em uma apresentação mais moderna, incluindo:

- fundo com gradiente animado
- card centralizado
- destaque visual do operador selecionado
- feedback de erro em tela
- visual limpo e agradável

---

## 📈 Possíveis melhorias

Como próximos passos, este projeto pode evoluir com:

- [ ] histórico de operações
- [ ] testes automatizados
- [ ] suporte a porcentagem e potência
- [ ] modo escuro/claro
- [ ] responsividade aprimorada
- [ ] deploy da versão web

---

## 🤝 Contribuição

Contribuições são bem-vindas.

Se quiser melhorar o projeto:

1. faça um fork do repositório
2. crie uma branch para sua feature
3. faça suas alterações
4. abra um pull request


## 👨‍💻 Autor

Desenvolvido por **Rafael Maia**.

- GitHub: [rafaelmaia-dev](https://github.com/rafaelmaia-dev)
- LinkedIn: [Rafael Maia](https://www.linkedin.com/in/SEU-USUARIO/)



## 📄 Licença

Este projeto está sob a licença **MIT**.



## 💬 Observação final

Este repositório representa uma prática importante de fundamentos de programação e também uma base interessante para evolução futura. Mesmo sendo um projeto simples, ele já demonstra conceitos valorizados no mercado, como organização, clareza e tratamento de erros.
