def string(s):
    if not s:
        return ""  # Retorna vazio se a string estiver vazia

    resultado = ""
    contador = 1  # Começa contando o primeiro caractere

    for i in range(1, len(s)):  # Percorre do segundo caractere até o final
        if s[i] == s[i - 1]:  # Se for igual ao anterior, aumenta o contador
            contador += 1
        else:
            resultado += s[i - 1] + (str(contador) if contador > 1 else "")
            contador = 1  # Reinicia o contador para o novo caractere

    # Adiciona o último caractere ao resultado
    resultado += s[-1] + (str(contador) if contador > 1 else "")

    return resultado

# Teste
entrada = "VVvIIiiCcCTOoOOOoRR"
print(string(entrada))  