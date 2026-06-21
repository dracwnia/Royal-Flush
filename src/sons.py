import pygame

TAXA_AMOSTRAGEM = 44100

_inicializado = False
_som_cassino = None
_som_tiro = None


def iniciar_audio():
    global _inicializado, _som_cassino, _som_tiro

    if _inicializado:
        return

    try:
        pygame.mixer.pre_init(TAXA_AMOSTRAGEM, -16, 2, 512)
    except Exception:
        pass

    if not pygame.mixer.get_init():
        pygame.mixer.init(frequency=TAXA_AMOSTRAGEM, size=-16, channels=2)

    try:
        import os
        BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        
        caminho_cassino = os.path.join(BASE_DIR, "assets", "sons", "cassino.wav")
        caminho_tiro = os.path.join(BASE_DIR, "assets", "sons", "tiro.wav")

        _som_cassino = pygame.mixer.Sound(caminho_cassino)
        _som_tiro = pygame.mixer.Sound(caminho_tiro)
    except Exception as e:
        print(f"Erro ao carregar os sons: {e}")

    _inicializado = True


def tocar_som_cassino(volume=0.5):
    if not _inicializado or _som_cassino is None:
        return
    _som_cassino.set_volume(volume)
    _som_cassino.play()


def tocar_som_tiro(volume=0.6):
    if not _inicializado or _som_tiro is None:
        return
    _som_tiro.set_volume(volume)
    _som_tiro.play()