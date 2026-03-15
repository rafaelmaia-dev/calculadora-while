var operadorAtual = null;

function selecionarOperador(btn, op) {
  operadorAtual = op;
  var labels = { '+': 'Adição (+)', '-': 'Subtração (−)', '*': 'Multiplicação (×)', '/': 'Divisão (÷)' };
  document.getElementById('operador-selecionado').textContent = 'Operador: ' + labels[op];
  document.querySelectorAll('.botoes-operacao button').forEach(function(b) { b.classList.remove('ativo'); });
  btn.classList.add('ativo');
}

function calcular() {
  var n1 = parseFloat(document.getElementById('numero1').value);
  var n2 = parseFloat(document.getElementById('numero2').value);
  var el = document.getElementById('resultado');

  if (isNaN(n1) || isNaN(n2)) {
    el.textContent = 'Erro: Digite dois números válidos.';
    el.className = 'erro';
    return;
  }
  if (operadorAtual === null) {
    el.textContent = 'Erro: Selecione um operador.';
    el.className = 'erro';
    return;
  }

  var sim = { '+': '+', '-': '−', '*': '×', '/': '÷' };
  var valor;
  if (operadorAtual === '+') valor = n1 + n2;
  else if (operadorAtual === '-') valor = n1 - n2;
  else if (operadorAtual === '*') valor = n1 * n2;
  else if (operadorAtual === '/') {
    if (n2 === 0) {
      el.textContent = 'Erro: Divisão por zero não permitida.';
      el.className = 'erro';
      return;
    }
    valor = n1 / n2;
  }

  el.textContent = 'Resultado: ' + n1 + ' ' + sim[operadorAtual] + ' ' + n2 + ' = ' + valor;
  el.className = '';
}
