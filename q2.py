#PY

def string(s):
    if not s:
        return ""  

    resultado = ""
    contador = 1  

    for i in range(1, len(s)):  
        if s[i] == s[i - 1]:  
            contador += 1
        else:
            resultado += s[i - 1] + (str(contador) if contador > 1 else "")
            contador = 1  

    
    resultado += s[-1] + (str(contador) if contador > 1 else "")

    return resultado


entrada = "VVvIIiiCcCTOoOOOoRR"
print(string(entrada))  