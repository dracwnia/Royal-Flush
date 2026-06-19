import pygame
import math
import time
 
from src.config import (
    LARGURA_TELA, ALTURA_TELA, FPS, TITULO_JOGO,
    VERDE_MESA, VERDE_ESCURO, DOURADO, BRANCO,
    VERMELHO, AMARELO, CINZA,
    PAINEL_X, CAMINHO_RANKING,
)
from src.funcoes import (
    tomar_dano,
    jogador_perdeu,
    ganhar_pontos,
    comparar_cartas,
    criar_deck,
    posicionar_cartas,
    carta_clicada,
    todas_fixadas,
)
from src.sprites import (
    desenhar_carta,
    desenhar_painel,
)
from src.dados import salvar_ranking
 
 
MAX_NIVEL = 3
 
_GOLD     = (212, 175,  55)
_GOLD_DIM = (140, 110,  30)
_CREAM    = (255, 245, 200)
 
 
def tela_menu(tela, fonte_titulo, fonte_btn, relogio):
    frames      = _carregar_gif("./assets/imagens/tela_inicial.gif", LARGURA_TELA, ALTURA_TELA)
    frame_idx   = 0
    frame_timer = 0
    FRAME_DELAY = 80
 
    cx = LARGURA_TELA  // 2
    cy = ALTURA_TELA   // 2
 
    btn_w, btn_h = 220, 52
    btn_jogar = pygame.Rect(cx - btn_w // 2, cy + 60,  btn_w, btn_h)
    btn_sair  = pygame.Rect(cx - btn_w // 2, cy + 125, btn_w, btn_h)
    sub_fonte = pygame.font.SysFont("arial", 14)
 
    t = 0
 
    while True:
        dt = relogio.tick(FPS)
        t += 1
 
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                pygame.quit()
                raise SystemExit
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if btn_jogar.collidepoint(evento.pos):
                    return
                if btn_sair.collidepoint(evento.pos):
                    pygame.quit()
                    raise SystemExit
 
        frame_timer += dt
        if frame_timer >= FRAME_DELAY:
            frame_timer = 0
            frame_idx   = (frame_idx + 1) % len(frames)
 
        tela.blit(frames[frame_idx], (0, 0))
 
        overlay = pygame.Surface((LARGURA_TELA, ALTURA_TELA), pygame.SRCALPHA)
        pygame.draw.rect(overlay, (0, 0, 0, 120),
                         (cx - 170, cy - 130, 340, 310), border_radius=4)
        tela.blit(overlay, (0, 0))
 
        pulse    = int(15 * math.sin(t * 0.06))
        gold_now = (min(255, _GOLD[0] + pulse), _GOLD[1], _GOLD[2])
 
        for line, oy in [("ROYAL", cy - 105), ("FLUSH", cy - 55)]:
            sombra = fonte_titulo.render(line, True, (80, 5, 10))
            tela.blit(sombra, sombra.get_rect(center=(cx + 2, oy + 2)))
            img = fonte_titulo.render(line, True, gold_now)
            tela.blit(img, img.get_rect(center=(cx, oy)))
 
        sep_y = cy - 10
        pygame.draw.line(tela, _GOLD_DIM, (cx - 130, sep_y), (cx + 130, sep_y), 1)
 
        sub = sub_fonte.render("SALVE SUA ALMA", True, _GOLD_DIM)
        tela.blit(sub, sub.get_rect(center=(cx, sep_y + 16)))
 
        mx, my = pygame.mouse.get_pos()
        _botao(tela, fonte_btn, "JOGAR", btn_jogar, mx, my, cor_base=(40, 10, 10))
        _botao(tela, fonte_btn, "SAIR",  btn_sair,  mx, my, cor_base=(15,  5, 30))
 
        pygame.display.flip()
 
 
def tela_game_over(tela, fonte_titulo, fonte_btn, nivel, relogio):
    btn_reiniciar = pygame.Rect(0, 0, 220, 50)
    btn_menu      = pygame.Rect(0, 0, 220, 50)
 
    while True:
        relogio.tick(FPS)
 
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                pygame.quit()
                raise SystemExit
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if btn_reiniciar.collidepoint(evento.pos):
                    return "reiniciar"
                if btn_menu.collidepoint(evento.pos):
                    return "menu"
 
        tela.fill((25, 10, 10))
        cx = LARGURA_TELA // 2
 
        t1 = fonte_titulo.render("GAME OVER", True, VERMELHO)
        tela.blit(t1, (cx - t1.get_width() // 2, 140))
 
        ts = fonte_btn.render(f"Nivel atingido: {nivel}", True, DOURADO)
        tela.blit(ts, (cx - ts.get_width() // 2, 300))
 
        btn_reiniciar = pygame.Rect(cx - 110, 400, 220, 50)
        btn_menu      = pygame.Rect(cx - 110, 465, 220, 50)
 
        _desenhar_botao(tela, "JOGAR NOVAMENTE", btn_reiniciar, fonte_btn)
        _desenhar_botao(tela, "MENU PRINCIPAL",  btn_menu,      fonte_btn, cor_fundo=(40, 40, 80))
 
        pygame.display.flip()
 
 
def tela_vitoria_nivel(tela, fonte_titulo, fonte_btn, nivel, ultimo, relogio):
    btn_continuar = pygame.Rect(0, 0, 240, 50)
 
    while True:
        relogio.tick(FPS)
 
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if btn_continuar.collidepoint(evento.pos):
                    return
 
        tela.fill((10, 30, 15))
        cx = LARGURA_TELA // 2
 
        texto = "VOCE VENCEU!" if ultimo else f"NIVEL {nivel - 1} COMPLETO!"
        t1 = fonte_titulo.render(texto, True, DOURADO)
        tela.blit(t1, (cx - t1.get_width() // 2, 200))
 
        label_btn = "MENU" if ultimo else "PROXIMO NIVEL"
        btn_continuar = pygame.Rect(cx - 120, 360, 240, 50)
        _desenhar_botao(tela, label_btn, btn_continuar, fonte_btn)
 
        pygame.display.flip()
 
 
def _botao(surf, fonte, texto, rect, mx, my, cor_base):
    hover = rect.collidepoint(mx, my)
    cor   = tuple(min(255, c + 35) for c in cor_base) if hover else cor_base
    borda = _GOLD if hover else _GOLD_DIM
    pygame.draw.rect(surf, cor,   rect, border_radius=4)
    pygame.draw.rect(surf, borda, rect, 2, border_radius=4)
    txt = fonte.render(texto, True, _GOLD if hover else _CREAM)
    surf.blit(txt, txt.get_rect(center=rect.center))
 
 
def _desenhar_botao(tela, texto, rect, fonte, cor_fundo=(30, 60, 130)):
    hover = rect.collidepoint(pygame.mouse.get_pos())
    cor   = tuple(min(255, c + 30) for c in cor_fundo) if hover else cor_fundo
    pygame.draw.rect(tela, cor, rect, border_radius=8)
    pygame.draw.rect(tela, DOURADO, rect, width=2, border_radius=8)
    txt = fonte.render(texto, True, BRANCO)
    tela.blit(txt, (rect.centerx - txt.get_width() // 2, rect.centery - txt.get_height() // 2))
 
 
def _desenhar_fundo(tela):
    tela.fill(VERDE_MESA)
    for x in range(0, PAINEL_X, 40):
        pygame.draw.line(tela, VERDE_ESCURO, (x, 0), (x, ALTURA_TELA), 1)
    for y in range(0, ALTURA_TELA, 40):
        pygame.draw.line(tela, VERDE_ESCURO, (0, y), (PAINEL_X, y), 1)
 
 
def _resetar_jogo(nivel, vidas):
    cartas        = posicionar_cartas(criar_deck(nivel), nivel)
    selecionadas  = []
    coringa_usado = False
    return cartas, selecionadas, coringa_usado
 
 
def _carregar_gif(path, w, h):
    try:
        from PIL import Image, ImageSequence
        gif    = Image.open(path)
        frames = []
        for frame in ImageSequence.Iterator(gif):
            rgba = frame.convert("RGBA").resize((w, h), Image.LANCZOS)
            surf = pygame.image.fromstring(rgba.tobytes(), rgba.size, "RGBA")
            frames.append(surf.convert())
        return frames or [_surface_preta(w, h)]
    except Exception as e:
        print(f"[menu] {e}")
        return [_surface_preta(w, h)]
 
 
def _surface_preta(w, h):
    s = pygame.Surface((w, h))
    s.fill((10, 3, 8))
    return s
 
 
def executar_jogo():
    pygame.init()
 
    tela    = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)
    relogio = pygame.time.Clock()
 
    fonte_titulo = pygame.font.SysFont("georgia,timesnewroman", 48, bold=True)
    fonte_info   = pygame.font.SysFont("arial", 15)
    fonte_btn    = pygame.font.SysFont("arial", 18, bold=True)
    fonte_msg    = pygame.font.SysFont("georgia,timesnewroman", 24, bold=True)
 
    tela_menu(tela, fonte_titulo, fonte_btn, relogio)
 
    nivel = 1
    vidas = 3
    pontos = 0
    multiplicador = 1
 
    cartas, selecionadas, coringa_usado = _resetar_jogo(nivel, vidas)
 
    aguardando_fechar = False
    tempo_fechar      = 0
    DELAY_FECHAR      = 1.2
 
    mensagem       = ""
    cor_mensagem   = BRANCO
    tempo_mensagem = 0
    DURACAO_MSG    = 1.8
 
    rodando = True
 
    while rodando:
        relogio.tick(FPS)
        agora = time.time()
 
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                rodando = False
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if aguardando_fechar:
                    continue
                idx = carta_clicada(cartas, evento.pos)
                if idx == -1:
                    continue
                carta = cartas[idx]
 
                if carta["coringa"]:
                    carta["estado"] = "aberta"
                    if coringa_usado:
                        salvar_ranking(CAMINHO_RANKING, nivel)
                        resultado = tela_game_over(tela, fonte_titulo, fonte_btn, nivel, relogio)
                        nivel = 1
                        vidas = 3
                        pontos = 0
                        multiplicador = 1
                        if resultado == "menu":
                            tela_menu(tela, fonte_titulo, fonte_btn, relogio)
                        cartas, selecionadas, coringa_usado = _resetar_jogo(nivel, vidas)
                        aguardando_fechar = False
                        mensagem = ""
                    else:
                        coringa_usado = True
                    for c in cartas:
                        if c["estado"] in ("fixada", "aberta") and not c["coringa"]:
                            c["estado"] = "fechada"
                        selecionadas      = []
                        mensagem          = "CORINGA! Cartas desviradas!"
                        cor_mensagem      = AMARELO
                        tempo_mensagem    = agora
                        aguardando_fechar = True
                        tempo_fechar      = agora + DELAY_FECHAR
                    continue
 
                carta["estado"] = "aberta"
                selecionadas.append(idx)
 
                if len(selecionadas) < 2:
                    continue
 
                i1, i2    = selecionadas[0], selecionadas[1]
                resultado = comparar_cartas(cartas[i1], cartas[i2])
 
                if resultado == "par_perfeito":
                    pontos, multiplicador = ganhar_pontos(pontos, multiplicador)
                    cartas[i1]["estado"] = "fixada"
                    cartas[i2]["estado"] = "fixada"
                    selecionadas         = []
                    mensagem             = "PAR PERFEITO!"
                    cor_mensagem         = DOURADO
                    tempo_mensagem       = agora
 
                    if todas_fixadas(cartas):
                        nivel += 1
                        if nivel > MAX_NIVEL:
                            tela_vitoria_nivel(tela, fonte_titulo, fonte_btn, nivel, ultimo=True, relogio=relogio)
                            tela_menu(tela, fonte_titulo, fonte_btn, relogio)
                            nivel = 1
                            vidas = 3
                            pontos = 0
                            multiplicador = 1
                        else:
                            tela_vitoria_nivel(tela, fonte_titulo, fonte_btn, nivel, ultimo=False, relogio=relogio)
                        cartas, selecionadas, coringa_usado = _resetar_jogo(nivel, vidas)
                        mensagem = ""
 
                elif resultado in ("par_naipe", "par_valor"):
                    multiplicador = 1
                    mensagem          = "Tente de novo!"
                    cor_mensagem      = (180, 220, 255)
                    tempo_mensagem    = agora
                    aguardando_fechar = True
                    tempo_fechar      = agora + DELAY_FECHAR
 
                else:
                    multiplicador = 1
                    vidas          = tomar_dano(vidas, 1)
                    mensagem       = f"Errado! Vidas: {vidas}"
                    cor_mensagem   = VERMELHO
                    tempo_mensagem = agora
                    aguardando_fechar = True
                    tempo_fechar      = agora + DELAY_FECHAR
 
                    if jogador_perdeu(vidas):
                        salvar_ranking(CAMINHO_RANKING, nivel)
                        resultado = tela_game_over(tela, fonte_titulo, fonte_btn, nivel, relogio)
                        nivel = 1
                        vidas = 3
                        pontos = 0
                        multiplicador = 1
                        if resultado == "menu":
                            tela_menu(tela, fonte_titulo, fonte_btn, relogio)
                        cartas, selecionadas, coringa_usado = _resetar_jogo(nivel, vidas)
                        aguardando_fechar = False
                        mensagem = ""
 
        if aguardando_fechar and agora >= tempo_fechar:
            for i in selecionadas:
                if cartas[i]["estado"] == "aberta":
                    cartas[i]["estado"] = "fechada"
            for c in cartas:
                if c["coringa"] and c["estado"] == "aberta":
                    c["estado"] = "fechada"
            selecionadas      = []
            aguardando_fechar = False
 
        _desenhar_fundo(tela)
        for carta in cartas:
            desenhar_carta(tela, carta)
        desenhar_painel(tela, vidas, nivel, pontos, fonte_titulo, fonte_info)
 
        if mensagem and agora - tempo_mensagem < DURACAO_MSG:
            txt_msg = fonte_msg.render(mensagem, True, cor_mensagem)
            mx = PAINEL_X // 2 - txt_msg.get_width() // 2
            my = ALTURA_TELA  // 2 - txt_msg.get_height() // 2
            fundo = pygame.Surface((txt_msg.get_width() + 20, txt_msg.get_height() + 10), pygame.SRCALPHA)
            fundo.fill((0, 0, 0, 160))
            tela.blit(fundo, (mx - 10, my - 5))
            tela.blit(txt_msg, (mx, my))
 
        pygame.display.flip()
 
    pygame.quit()
