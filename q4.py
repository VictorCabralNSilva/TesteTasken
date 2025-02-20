#PY

def contar_vogais_consoantes(linha):
    vogais = "aeiouAEIOU"
    consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    num_vogais = sum(1 for char in linha if char in vogais)
    num_consoantes = sum(1 for char in linha if char in consoantes)

    return num_vogais, num_consoantes


def analisar_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arquivo:
            linhas = arquivo.readlines()

        if not linhas:
            print("O arquivo está vazio.")
            return

        max_vogais = 0
        linha_mais_vogais = ""
        max_consoantes = 0
        linha_mais_consoantes = ""

        for linha in linhas:
            num_vogais, num_consoantes = contar_vogais_consoantes(linha)

            if num_vogais > max_vogais:
                max_vogais = num_vogais
                linha_mais_vogais = linha.strip()

            if num_consoantes > max_consoantes:
                max_consoantes = num_consoantes
                linha_mais_consoantes = linha.strip()

        print(f"Linha com mais vogais ({max_vogais} vogais): {linha_mais_vogais}")
        print(f"Linha com mais consoantes ({max_consoantes} consoantes): {linha_mais_consoantes}")

    except FileNotFoundError:
        print("Erro: O arquivo não foi encontrado.")
    except Exception as e:
        print(f"Erro inesperado: {e}")


nome_arquivo = input("Digite o nome do arquivo .txt: ")
analisar_arquivo(nome_arquivo)
