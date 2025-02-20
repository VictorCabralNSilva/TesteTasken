function analisarNumeros() {
  let numeros = [];
  let numero;

  
  do {
    numero = parseFloat(prompt("Digite um número positivo (ou 0 para encerrar):")); 
    if (isNaN(numero) || numero < 0) {
      alert("Por favor, digite um número positivo ou 0.");
      continue; 
    }
    if (numero !== 0) {
      numeros.push(numero);
    }
  } while (numero !== 0);

  // a) Quantidade de números lidos
  const quantidade = numeros.length;
  console.log(`Quantidade de números lidos: ${quantidade}`);

  if (quantidade === 0) {
    console.log("Nenhum número foi digitado além do zero.");
    return; 
  }

  // b) Maior número lido
  const maior = Math.max(...numeros); 
  console.log(`Maior número lido: ${maior}`);

  // c) Média dos números lidos
  const soma = numeros.reduce((acc, val) => acc + val, 0);
  const media = soma / quantidade;
  console.log(`Média dos números lidos: ${media}`);

  // d) Menor número ímpar lido
  let impares = numeros.filter(num => num % 2 !== 0); 
  let menorImpar = impares.length > 0 ? Math.min(...impares) : null;

  if (menorImpar !== null) {
    console.log(`Menor número ímpar lido: ${menorImpar}`);
  } else {
    console.log("Nenhum número ímpar foi digitado.");
  }

  // e) Quantidade de vezes que cada número ocorreu
  let contagemNumeros = {};
  for (let num of numeros) {
    contagemNumeros[num] = (contagemNumeros[num] || 0) + 1; 
  }

  console.log("Contagem de ocorrências:");
  for (let num in contagemNumeros) {
    console.log(`O número ${num} ocorreu ${contagemNumeros[num]} vezes.`);
  }
}

analisarNumeros();