import pygame

from src.config import (
    CARTA_LARG, CARTA_ALT,
    BRANCO, PRETO, AZUL_CARTA, DOURADO, VERMELHO,
    AMARELO, SIMBOLOS_NAIPE, CORES_NAIPE,
    VIDAS_INICIAIS,
)

_cache_imagens = {}

def _carregar_imagem(path, w, h):
    chave = (path, w, h)
    if chave not in _cache_imagens:
        img = pygame.image.load(path).convert_alpha()
        _cache_imagens[chave] = pygame.transform.scale(img, (w, h))
    return _cache_imagens[chave]


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
    try:
        import os
        pasta_atual = os.path.dirname(__file__)
        caminho_real = os.path.abspath(os.path.join(pasta_atual, "..", "assets", "imagens", "joker.png"))
        
        img = _carregar_imagem(caminho_real, rect.width, rect.height)
        sup.blit(img, rect.topleft)
        print("joker carregado ok")
    except Exception as e:
        print(f"erro joker: {e}")
        pygame.draw.rect(sup, (30, 20, 50), rect, border_radius=8)

#agr precisa da variavel pontos
def desenhar_painel(tela, vidas, nivel, pontos, fonte_titulo, fonte_info):
    from src.config import PAINEL_X, PAINEL_LARG, ALTURA_TELA, DOURADO, BRANCO, VERMELHO

    _GOLD     = (212, 175,  55)
    _GOLD_DIM = (140, 110,  30)

    painel = pygame.Rect(PAINEL_X, 0, PAINEL_LARG, ALTURA_TELA)
    pygame.draw.rect(tela, (10, 22, 14), painel)
    pygame.draw.line(tela, _GOLD,     (PAINEL_X,     0), (PAINEL_X,     ALTURA_TELA), 2)
    pygame.draw.line(tela, _GOLD_DIM, (PAINEL_X + 3, 0), (PAINEL_X + 3, ALTURA_TELA), 1)

    cx = PAINEL_X + PAINEL_LARG // 2

    t1 = fonte_titulo.render("ROYAL", True, _GOLD)
    t2 = fonte_titulo.render("FLUSH", True, _GOLD)
    tela.blit(t1, (cx - t1.get_width() // 2, 22))
    tela.blit(t2, (cx - t2.get_width() // 2, 22 + t1.get_height()))

    y = 22 + t1.get_height() * 2 + 18
    pygame.draw.line(tela, _GOLD,     (PAINEL_X + 14, y),     (PAINEL_X + PAINEL_LARG - 14, y),     1)
    pygame.draw.line(tela, _GOLD_DIM, (PAINEL_X + 14, y + 3), (PAINEL_X + PAINEL_LARG - 14, y + 3), 1)

    y += 18
    fonte_label = pygame.font.SysFont("arial", 11)
    lbl = fonte_label.render("N I V E L", True, _GOLD_DIM)
    tela.blit(lbl, (cx - lbl.get_width() // 2, y))
    y += lbl.get_height() + 4

    fonte_num = pygame.font.SysFont("georgia,timesnewroman", 36, bold=True)
    txt_nivel = fonte_num.render(str(nivel), True, _GOLD)
    tela.blit(txt_nivel, (cx - txt_nivel.get_width() // 2, y))
    y += txt_nivel.get_height() + 14

    pygame.draw.line(tela, _GOLD_DIM, (PAINEL_X + 14, y),     (PAINEL_X + PAINEL_LARG - 14, y),     1)
    pygame.draw.line(tela, _GOLD,     (PAINEL_X + 14, y + 3), (PAINEL_X + PAINEL_LARG - 14, y + 3), 1)

    y += 20
    lbl_v = fonte_label.render("V I D A S", True, _GOLD_DIM)
    tela.blit(lbl_v, (cx - lbl_v.get_width() // 2, y))
    y += lbl_v.get_height() + 10

    max_vidas = 5 if nivel == 3 else 3
    
    start_x = cx - (max_vidas * 28) // 2 + 8
    for i in range(max_vidas):
        cor = (200, 30, 30) if i < vidas else (55, 30, 30)
        hx = start_x + i * 28
        hy = y + 14
        r  = 10
        pygame.draw.circle(tela, cor, (hx - r // 2, hy - r // 4), r // 2 + 1)
        pygame.draw.circle(tela, cor, (hx + r // 2, hy - r // 4), r // 2 + 1)
        pygame.draw.polygon(tela, cor, [
            (hx - r, hy - r // 4 + 2),
            (hx, hy + r + 1),
            (hx + r, hy - r // 4 + 2)
        ])
        if i < vidas:
            pygame.draw.circle(tela, (255, 100, 100), (hx - r // 2 - 1, hy - r // 4 - 1), 2)

    y += 40
    pygame.draw.line(tela, DOURADO, (PAINEL_X + 10, y), (PAINEL_X + PAINEL_LARG - 10, y), 1)
    txt_pontos = fonte_info.render(f"Pontos: {pontos}", True, DOURADO)
    y += txt_pontos.get_height()
    tela.blit(txt_pontos, (cx - txt_pontos.get_width() // 2, y))