from pathlib import Path
LARGURA_TELA = 900
ALTURA_TELA = 700
FPS = 60

TITULO_JOGO = "Royal Flush"

BRANCO       = (255, 255, 255)
PRETO        = (0, 0, 0)
CINZA        = (212, 212, 212)
VERDE_MESA   = (35, 100, 55)
VERDE_ESCURO = (20, 70, 35)
DOURADO      = (212, 175, 55)
VERMELHO     = (200, 40, 40)
AZUL_CARTA   = (30, 60, 130)
AMARELO      = (255, 215, 0)

NAIPES  = ["copas", "ouros", "espadas", "paus"]
VALORES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

SIMBOLOS_NAIPE = {
    "copas":   "♥",
    "ouros":   "♦",
    "espadas": "♠",
    "paus":    "♣",
}

CORES_NAIPE = {
    "copas":   VERMELHO,
    "ouros":   VERMELHO,
    "espadas": PRETO,
    "paus":    PRETO,
}

GRID_NIVEIS = {
    1: (3, 3),  
    2: (5, 3),   
    3: (5, 5),   
}

VIDAS_INICIAIS = 3
PONTOS_INICIAIS = 0
MULTIPLICADOR_INCIAL = 1

PAINEL_X    = 720
PAINEL_LARG = 180

CARTA_LARG   = 90
CARTA_ALT    = 120
MARGEM_CARTA = 12

ROOT_FOLDER = Path(__file__).resolve().parent
CAMINHO_RANKING = ROOT_FOLDER/ ".." / "data" / "ranking.txt"
