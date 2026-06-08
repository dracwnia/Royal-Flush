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


def comparar_cartas(carta1, carta2):
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

    random.shuffle(deck)
    return deck


def posicionar_cartas(deck, nivel):
    cols, rows = GRID_NIVEIS.get(nivel, (4, 3))

    grid_larg = cols * CARTA_LARG + (cols - 1) * MARGEM_CARTA
    grid_alt  = rows * CARTA_ALT  + (rows - 1) * MARGEM_CARTA

    offset_x = (PAINEL_X - grid_larg) // 2
    offset_y = (700 - grid_alt) // 2

    cartas = []
    for idx, carta in enumerate(deck):
        col = idx % cols
        row = idx // cols
        x = offset_x + col * (CARTA_LARG + MARGEM_CARTA)
        y = offset_y + row * (CARTA_ALT  + MARGEM_CARTA)
        cartas.append({
            "valor":   carta["valor"],
            "naipe":   carta["naipe"],
            "coringa": carta["coringa"],
            "estado":  "fechada",
            "rect":    pygame.Rect(x, y, CARTA_LARG, CARTA_ALT),
        })

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
