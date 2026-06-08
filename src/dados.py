def salvar_ranking(caminho_arquivo, nivel):
    with open(caminho_arquivo, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"Nivel: {nivel}\n")
