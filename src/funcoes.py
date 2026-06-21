import random
import pygame

from src.config import (
    NAIPES, VALORES, GRID_NIVEIS,
    CARTA_LARG, CARTA_ALT, MARGEM_CARTA, PAINEL_X,
)


def tomar_dano(vida_atual, dano):
    return vida_atual - dano


def jogador_perdeu(vidas):
    return vidas <= 0


def ganhar_pontos(pontos, multiplicador):
    pontos = pontos + 100 * multiplicador
    multiplicador = multiplicador * 2
    return pontos, multiplicador


def comparar_cartas(carta1, carta2):
    """Compara duas cartas e retorna o tipo de resultado.

    Retorna uma das strings: 'par_perfeito', 'par_naipe', 'par_valor', 'errado'.
    Esta funcao nao modifica pontos nem multiplicador; a atualizacao deve
    ser feita pela camada de apresentacao/controle (por exemplo, `jogo.py`).
    """
    mesmo_naipe = carta1["naipe"] == carta2["naipe"]
    mesmo_valor = carta1["valor"] == carta2["valor"]

    if mesmo_naipe and mesmo_valor:
        return "par_perfeito"
    elif mesmo_naipe:
        return "par_naipe"
    elif mesmo_valor:
        return "par_valor"
    else:
        return "errado"


def criar_deck(nivel):
    """
    Cria o baralho embaralhado para o nivel informado.

    O tabuleiro tem `total = cols * rows` cartas, sendo uma delas sempre
    o Coringa. As demais (total - 1) posicoes sao preenchidas com pares
    perfeitos (mesmo naipe e mesmo valor). Quando (total - 1) e impar,
    sobra uma posicao que nao caberia em nenhum par; essa posicao e
    preenchida com uma carta avulsa extra, para garantir que o tabuleiro
    nunca fique com espacos vazios.
    """
    cols, rows = GRID_NIVEIS.get(nivel, (4, 3))
    total = cols * rows

    todas = []
    for naipe in NAIPES:
        for valor in VALORES:
            todas.append({"valor": valor, "naipe": naipe, "coringa": False})

    random.shuffle(todas)

  
    n_pares = (total - 1) // 2
    deck = []
    usadas = set()

    for carta in todas:
        chave = (carta["valor"], carta["naipe"])
        if chave not in usadas and len(deck) // 2 < n_pares:
            usadas.add(chave)
            deck.append({"valor": carta["valor"], "naipe": carta["naipe"], "coringa": False})
            deck.append({"valor": carta["valor"], "naipe": carta["naipe"], "coringa": False})

    deck.append({"valor": "CORINGA", "naipe": "coringa", "coringa": True})

    if len(deck) < total:
        for carta in todas:
            chave = (carta["valor"], carta["naipe"])
            if chave not in usadas:
                usadas.add(chave)
                deck.append({"valor": carta["valor"], "naipe": carta["naipe"], "coringa": False})
                break

    random.shuffle(deck)
    return deck


def posicionar_cartas(cartas, nivel):
    from src.config import (
        GRID_NIVEIS, CARTA_LARG, CARTA_ALT, MARGEM_CARTA,
        PAINEL_X, ALTURA_TELA
    )

    cols, linhas = GRID_NIVEIS[nivel]

    grid_w = cols * CARTA_LARG + (cols - 1) * MARGEM_CARTA
    grid_h = linhas * CARTA_ALT + (linhas - 1) * MARGEM_CARTA

    area_w = PAINEL_X
    inicio_x = (area_w - grid_w) // 2
    inicio_y = (ALTURA_TELA - grid_h) // 2

    for i, carta in enumerate(cartas):
        col = i % cols
        lin = i // cols
        x = inicio_x + col * (CARTA_LARG + MARGEM_CARTA)
        y = inicio_y + lin * (CARTA_ALT  + MARGEM_CARTA)
        carta["estado"] = "fechada"
        carta["rect"] = pygame.Rect(x, y, CARTA_LARG, CARTA_ALT)

    return cartas


def carta_clicada(cartas, pos):
    for i, carta in enumerate(cartas):
        if carta["rect"].collidepoint(pos) and carta["estado"] == "fechada":
            return i
    return -1


def todas_fixadas(cartas):
    for carta in cartas:
        if not carta["coringa"] and carta["estado"] != "fixada":
            return False
    return True