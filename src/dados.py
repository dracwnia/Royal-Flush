import os
def salvar_ranking(caminho_arquivo, nivel):
    print(os.getcwd())
    if os.path.isfile(caminho_arquivo):
        with open(caminho_arquivo, "a", encoding="utf-8") as arquivo:
            arquivo.write(f"Nivel: {nivel}\n")
    else:
        with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(f"Nivel: {nivel}\n")