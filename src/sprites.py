import pygame

from src.config import (
    CARTA_LARG, CARTA_ALT,
    BRANCO, PRETO, AZUL_CARTA, DOURADO, VERMELHO,
    AMARELO, SIMBOLOS_NAIPE, CORES_NAIPE,
)


def desenhar_carta(superficie, carta):
    if carta["estado"] == "fechada":
        _desenhar_verso(superficie, carta["rect"])
    elif carta["estado"] == "fixada":
        _desenhar_frente(superficie, carta, fixada=True)
    else:
        if carta["coringa"]:
            _desenhar_coringa(superficie, carta["rect"])
        else:
            _desenhar_frente(superficie, carta, fixada=False)


def _desenhar_verso(sup, rect):
    pygame.draw.rect(sup, AZUL_CARTA, rect, border_radius=8)
    pygame.draw.rect(sup, DOURADO, rect, width=2, border_radius=8)

    cx, cy = rect.center
    pontos = [(cx, cy - 18), (cx + 12, cy), (cx, cy + 18), (cx - 12, cy)]
    pygame.draw.polygon(sup, DOURADO, pontos)
    pontos2 = [(cx, cy - 10), (cx + 7, cy), (cx, cy + 10), (cx - 7, cy)]
    pygame.draw.polygon(sup, AZUL_CARTA, pontos2)


def _desenhar_frente(sup, carta, fixada):
    rect = carta["rect"]
    x, y = rect.topleft

    cor_fundo = (220, 245, 220) if fixada else (245, 245, 235)
    cor_borda = DOURADO if fixada else (180, 180, 180)

    pygame.draw.rect(sup, cor_fundo, rect, border_radius=8)
    pygame.draw.rect(sup, cor_borda, rect, width=2, border_radius=8)

    cor_naipe = CORES_NAIPE.get(carta["naipe"], PRETO)
    simbolo   = SIMBOLOS_NAIPE.get(carta["naipe"], "?")

    fonte_val = pygame.font.SysFont("segoeuisymbol,dejavusans", 16, bold=True)
    fonte_sim = pygame.font.SysFont("segoeuisymbol,dejavusans", 30)

    txt_val = fonte_val.render(carta["valor"], True, cor_naipe)
    sup.blit(txt_val, (x + 6, y + 5))
    txt_sim_peq = fonte_val.render(simbolo, True, cor_naipe)
    sup.blit(txt_sim_peq, (x + 6, y + 5 + txt_val.get_height()))

    txt_sim = fonte_sim.render(simbolo, True, cor_naipe)
    cx = x + CARTA_LARG // 2 - txt_sim.get_width() // 2
    cy = y + CARTA_ALT  // 2 - txt_sim.get_height() // 2
    sup.blit(txt_sim, (cx, cy))

    txt_val2 = fonte_val.render(carta["valor"], True, cor_naipe)
    sup.blit(txt_val2, (x + CARTA_LARG - txt_val2.get_width() - 6,
                        y + CARTA_ALT  - txt_val2.get_height() - 5))


def _desenhar_coringa(sup, rect):
    pygame.draw.rect(sup, (30, 20, 50), rect, border_radius=8)
    pygame.draw.rect(sup, AMARELO, rect, width=3, border_radius=8)

    x, y = rect.topleft

    fonte_g = pygame.font.SysFont("segoeuisymbol,dejavusans", 36)
    fonte_p = pygame.font.SysFont("arial", 12, bold=True)

    txt_joker = fonte_g.render("JOKER", True, AMARELO)
    cx = x + CARTA_LARG // 2 - txt_joker.get_width() // 2
    cy = y + CARTA_ALT  // 2 - txt_joker.get_height() // 2 - 8
    sup.blit(txt_joker, (cx, cy))

    txt_label = fonte_p.render("CORINGA", True, AMARELO)
    cx2 = x + CARTA_LARG // 2 - txt_label.get_width() // 2
    sup.blit(txt_label, (cx2, y + CARTA_ALT - 24))


def desenhar_painel(tela, vidas, nivel, fonte_titulo, fonte_info):
    from src.config import PAINEL_X, PAINEL_LARG, ALTURA_TELA, DOURADO, BRANCO, VERMELHO

    painel = pygame.Rect(PAINEL_X, 0, PAINEL_LARG, ALTURA_TELA)
    pygame.draw.rect(tela, (15, 35, 20), painel)
    pygame.draw.line(tela, DOURADO, (PAINEL_X, 0), (PAINEL_X, ALTURA_TELA), 3)

    t1 = fonte_titulo.render("ROYAL", True, DOURADO)
    t2 = fonte_titulo.render("FLUSH", True, DOURADO)
    cx = PAINEL_X + PAINEL_LARG // 2
    tela.blit(t1, (cx - t1.get_width() // 2, 20))
    tela.blit(t2, (cx - t2.get_width() // 2, 20 + t1.get_height()))

    y = 20 + t1.get_height() * 2 + 20
    pygame.draw.line(tela, DOURADO, (PAINEL_X + 10, y), (PAINEL_X + PAINEL_LARG - 10, y), 1)

    y += 15
    txt_nivel = fonte_info.render(f"Nivel: {nivel}", True, DOURADO)
    tela.blit(txt_nivel, (cx - txt_nivel.get_width() // 2, y))

    y += txt_nivel.get_height() + 25
    pygame.draw.line(tela, DOURADO, (PAINEL_X + 10, y), (PAINEL_X + PAINEL_LARG - 10, y), 1)
    y += 12
    txt_vidas = fonte_info.render("Vidas:", True, BRANCO)
    tela.blit(txt_vidas, (cx - txt_vidas.get_width() // 2, y))
    y += txt_vidas.get_height() + 8

    for i in range(3):
        cor = VERMELHO if i < vidas else (60, 60, 60)
        hx = PAINEL_X + 25 + i * 50
        hy = y + 12
        r = 12
        pygame.draw.circle(tela, cor, (hx - r // 2, hy - r // 4), r // 2)
        pygame.draw.circle(tela, cor, (hx + r // 2, hy - r // 4), r // 2)
        pygame.draw.polygon(tela, cor, [(hx - r, hy - r // 4 + 2), (hx, hy + r), (hx + r, hy - r // 4 + 2)])