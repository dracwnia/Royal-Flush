from src.funcoes import tomar_dano, jogador_perdeu, comparar_cartas, todas_fixadas
from src.dados import salvar_ranking


def test_jogador_perdeu_com_zero_vidas():
    """Deve indicar derrota quando o total de vidas chega a zero."""
    assert jogador_perdeu(0) is True


def test_jogador_nao_perdeu_com_vidas():
    """Nao deve indicar derrota quando o jogador ainda tem vidas."""
    assert jogador_perdeu(3) is False

def test_tomar_dano_reduz_vida():
    """Deve subtrair o dano das vidas atuais."""
    assert tomar_dano(3, 1) == 2


def test_tomar_dano_pode_zerar():
    """Deve permitir chegar a zero vidas."""
    assert tomar_dano(1, 1) == 0


def test_comparar_par_perfeito():
    """Mesmo naipe e mesmo valor deve retornar par_perfeito."""
    c1 = {"valor": "A", "naipe": "copas"}
    c2 = {"valor": "A", "naipe": "copas"}
    assert comparar_cartas(c1, c2) == "par_perfeito"


def test_comparar_par_naipe():
    """Mesmo naipe mas valor diferente deve retornar par_naipe."""
    c1 = {"valor": "A", "naipe": "copas"}
    c2 = {"valor": "K", "naipe": "copas"}
    assert comparar_cartas(c1, c2) == "par_naipe"


def test_comparar_par_valor():
    """Mesmo valor mas naipe diferente deve retornar par_valor."""
    c1 = {"valor": "A", "naipe": "copas"}
    c2 = {"valor": "A", "naipe": "espadas"}
    assert comparar_cartas(c1, c2) == "par_valor"


def test_comparar_errado():
    """Naipe e valor diferentes deve retornar errado."""
    c1 = {"valor": "A", "naipe": "copas"}
    c2 = {"valor": "K", "naipe": "espadas"}
    assert comparar_cartas(c1, c2) == "errado"


def test_todas_fixadas_true():
    """Deve retornar True quando todas as cartas nao-coringa estao fixadas."""
    cartas = [
        {"coringa": False, "estado": "fixada"},
        {"coringa": False, "estado": "fixada"},
        {"coringa": True,  "estado": "aberta"},
    ]
    assert todas_fixadas(cartas) is True


def test_todas_fixadas_false():
    """Deve retornar False quando ainda ha carta nao-coringa fechada."""
    cartas = [
        {"coringa": False, "estado": "fixada"},
        {"coringa": False, "estado": "fechada"},
        {"coringa": True,  "estado": "aberta"},
    ]
    assert todas_fixadas(cartas) is False


def test_salvar_ranking_acumula_entradas(tmp_path):
    """Deve acumular multiplas entradas sem sobrescrever."""
    arquivo = tmp_path / "ranking.txt"
    salvar_ranking(str(arquivo), 1)
    salvar_ranking(str(arquivo), 3)
    linhas = arquivo.read_text(encoding="utf-8").splitlines()
    assert len(linhas) == 2