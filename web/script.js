let operadorAtual = null;
let historico = JSON.parse(localStorage.getItem("historicoCalculadora")) || [];

const numero1 = document.getElementById("numero1");
const numero2 = document.getElementById("numero2");
const resultado = document.getElementById("resultado");
const operadorInfo = document.getElementById("operador-selecionado");
const listaHistorico = document.getElementById("lista-historico");
const btnCalcular = document.getElementById("btn-calcular");
const btnLimparHistorico = document.getElementById("limpar-historico");
const botoesOperacao = document.querySelectorAll(".botoes-operacao button");

const labels = {
  "+": "Adição (+)",
  "-": "Subtração (−)",
  "*": "Multiplicação (×)",
  "/": "Divisão (÷)"
};

const simbolos = {
  "+": "+",
  "-": "−",
  "*": "×",
  "/": "÷"
};

function calcularOperacao(n1, n2, operador) {
  switch (operador) {
    case "+":
      return n1 + n2;
    case "-":
      return n1 - n2;
    case "*":
      return n1 * n2;
    case "/":
      if (n2 === 0) {
        throw new Error("Divisão por zero não é permitida.");
      }
      return n1 / n2;
    default:
      throw new Error("Operador inválido.");
  }
}

function selecionarOperador(botao) {
  operadorAtual = botao.dataset.operador;
  operadorInfo.textContent = `Operador: ${labels[operadorAtual]}`;

  botoesOperacao.forEach((b) => b.classList.remove("ativo"));
  botao.classList.add("ativo");
}

function salvarHistorico() {
  localStorage.setItem("historicoCalculadora", JSON.stringify(historico));
}

function renderizarHistorico() {
  listaHistorico.innerHTML = "";

  if (historico.length === 0) {
    listaHistorico.innerHTML = "<li class='historico-item'>Nenhuma operação ainda.</li>";
    return;
  }

  historico
    .slice()
    .reverse()
    .forEach((item) => {
      const li = document.createElement("li");
      li.className = "historico-item";
      li.textContent = item;
      listaHistorico.appendChild(li);
    });
}

function calcular() {
  const n1 = Number.parseFloat(numero1.value);
  const n2 = Number.parseFloat(numero2.value);

  if (isNaN(n1) || isNaN(n2)) {
    resultado.textContent = "Erro: digite dois números válidos.";
    resultado.className = "erro";
    return;
  }

  if (!operadorAtual) {
    resultado.textContent = "Erro: selecione um operador.";
    resultado.className = "erro";
    return;
  }

  try {
    const valor = calcularOperacao(n1, n2, operadorAtual);
    const texto = `${n1} ${simbolos[operadorAtual]} ${n2} = ${valor}`;

    resultado.textContent = `Resultado: ${texto}`;
    resultado.className = "sucesso";

    historico.push(texto);
    salvarHistorico();
    renderizarHistorico();
  } catch (erro) {
    resultado.textContent = `Erro: ${erro.message}`;
    resultado.className = "erro";
  }
}

function limparHistorico() {
  historico = [];
  salvarHistorico();
  renderizarHistorico();
}

botoesOperacao.forEach((botao) => {
  botao.addEventListener("click", () => selecionarOperador(botao));
});

btnCalcular.addEventListener("click", calcular);
btnLimparHistorico.addEventListener("click", limparHistorico);

[numero1, numero2].forEach((input) => {
  input.addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
      calcular();
    }
  });
});

renderizarHistorico();
