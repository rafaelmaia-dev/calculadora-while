# Calculadora com While

Calculadora com **Python** (terminal) e **JavaScript** (interface web). O núcleo do projeto é o código Python; a parte web complementa com interface e histórico.

## Estrutura

```
calculadora-while/
├── src/
│   ├── calculadora.py   # Entrada principal Python — loop e I/O
│   ├── operacoes.py     # Lógica de cálculo (Python)
│   ├── index.html       # Interface web
│   ├── script.js        # Função de formatação (JS)
│   └── style.css        # Estilos
└── README.md
```

## Como rodar

**Terminal (Python — principal)**  
Na pasta `src`:

```bash
python calculadora.py
```

**Interface web**  
Abra `src/index.html` no navegador.

## Operações

Adição (+), subtração (−), multiplicação (×), divisão (÷). Divisão por zero é tratada no Python e no JS.

## Licença

MIT.
