//JS

function numero(n) {
  if (n <= 0) {
    console.log("Erro: O valor de entrada deve ser maior que 0");
    return;
  }

  // Geração da primeira linha
  let atual = n * n;
  let resultado = [atual];
  let diferenca = 2 * n - 1;

  // Laço de repetição
  while (diferenca > 0) {
    atual -= diferenca;
    if (atual >= 1) {
      resultado.push(atual);
    } else {
      break;
    }
    diferenca -= 2;
  }

  // Impressão das linhas:
  for (let i = 0; i < resultado.length; i++) {
    console.log(resultado.slice(i).join(" "));
  }
}

numero(5);