# 🧮 **Calculadora com While**

### **Utilizando os quatro operadores aritméticos**

![Python](https://img.shields.io/badge/Python-3.7%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Contributions](https://img.shields.io/badge/Contribuições-Bem--vindas-brightgreen?style=for-the-badge)

*Uma calculadora simples e robusta desenvolvida em Python com foco em estruturas de repetição e tratamento de erros*

[📋 Funcionalidades](#-funcionalidades) •
[🚀 Instalação](#-instalação) •
[💻 Como Usar](#-como-usar) •
[🎯 Exemplos](#-exemplos) •
[🤝 Contribuição](#-contribuição)

---

</div>

## 📖 Sobre o Projeto

Este projeto consiste em uma **calculadora interativa** desenvolvida em Python que demonstra conceitos fundamentais de programação, incluindo estruturas de repetição (`while`), tratamento de erros (`try/except`) e validação de entrada do usuário.

A aplicação permite que o usuário realize operações matemáticas básicas de forma contínua, com tratamento robusto de erros e uma interface amigável via terminal.

## 🎯 Objetivos de Aprendizado

- ✅ **Estruturas de Repetição**: Dominar o uso do loop `while`
- ✅ **Tratamento de Erros**: Implementar `try/except` para capturar exceções
- ✅ **Lógica de Programação**: Desenvolver pensamento algorítmico
- ✅ **Validação de Entrada**: Garantir dados consistentes do usuário
- ✅ **Boas Práticas**: Código limpo e bem estruturado

## 🔧 Funcionalidades

| Operação           | Símbolo | Descrição                            |
| -------------------- | -------- | -------------------------------------- |
| ➕ Adição          | `+`    | Soma dois números                     |
| ➖ Subtração       | `-`    | Subtrai o segundo do primeiro número  |
| ✖️ Multiplicação | `*`    | Multiplica dois números               |
| ➗ Divisão          | `/`    | Divide o primeiro pelo segundo número |

### 🛡️ Recursos de Segurança

- **Tratamento de divisão por zero**
- **Validação de entrada numérica**
- **Verificação de operadores válidos**
- **Opção de saída controlada**

## 🚀 Instalação

### Pré-requisitos

- Python 3.7 ou superior
- Git (opcional)

### Passos para instalação

1. **Clone o repositório**

```bash
git clone https://github.com/rafaelmaia-dev/calculadora-while.git
```

2. **Navegue até o diretório**

```bash
cd calculadora-while
```

3. **Execute o programa**

```bash
python calculadora.py
```

## 💻 Como Usar

1. **Inicie o programa** executando o arquivo Python
2. **Digite o primeiro número** quando solicitado
3. **Digite o segundo número**
4. **Escolha o operador** (+, -, *, /)
5. **Visualize o resultado**
6. **Escolha continuar ou sair** digitando "sim" para sair

## 🎯 Exemplos

### Exemplo 1: Adição

```
Digite o primeiro número: 20
Digite o segundo número: 10
Digite o operador (+, -, *, /): +
20.0 + 10.0 = 30.0

Você deseja sair? [s]im: não
```

### Exemplo 2: Divisão

```
Digite o primeiro número: 15
Digite o segundo número: 3
Digite o operador (+, -, *, /): /
15.0 / 3.0 = 5.0

Você deseja sair? [s]im: sim
Saindo da calculadora.
```

### Exemplo 3: Tratamento de Erro

```
Digite o primeiro número: abc
Erro: Por favor, digite um número válido.
Digite o primeiro número: 10
```

## 🏗️ Estrutura do Código

```
calculadora-while/
│
├── calculadora.py          # Arquivo principal
├── README.md              # Documentação
└── LICENSE               # Licença do projeto
```

### 🔍 Componentes Principais

- **Loop Principal**: Controla o fluxo da aplicação
- **Validação de Entrada**: Verifica se os valores são numéricos
- **Operações Matemáticas**: Executa os cálculos
- **Tratamento de Erros**: Captura e trata exceções
- **Interface do Usuário**: Interação via terminal

## 🛠️ Tecnologias Utilizadas

<div align="center">

![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)

</div>

- **Python 3.7+**: Linguagem de programação principal
- **Bibliotecas nativas**: Não requer instalação de dependências externas

## 🤝 Contribuição

Contribuições são sempre bem-vindas! Siga estes passos:

1. **Fork** o projeto
2. **Crie** uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. **Push** para a branch (`git push origin feature/AmazingFeature`)
5. **Abra** um Pull Request

### 📋 Ideias para Contribuição

- [ ] Adicionar operações avançadas (potenciação, raiz quadrada)
- [ ] Implementar histórico de operações
- [ ] Criar interface gráfica
- [ ] Adicionar testes unitários
- [ ] Melhorar a documentação

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor

**Rafael Maia**

- GitHub: [@rafaelmaia-dev](https://github.com/rafaelmaia-dev)
- LinkedIn: [Rafael Maia](https://linkedin.com/in/rafaelmaia-dev)

---

<div align="center">

### ⭐ Se este projeto foi útil para você, considere dar uma estrela!

*Desenvolvido com ❤️ para fins educacionais*
