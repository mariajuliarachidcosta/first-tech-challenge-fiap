"""Funções, constantes e decisões de método compartilhadas pelos notebooks."""
import pandas as pd
from matplotlib.ticker import FuncFormatter

# Paleta
COR, COR_DESTAQUE, COR_CINZA = "#1f4e79", "#e07b00", "#9aa5b1"

# Decisões de método (justificativa no notebook 01, seção 10)
JANELA_INICIO, JANELA_FIM = pd.Period("2017-01"), pd.Period("2018-08")

# Semente para todos os processos aleatórios
SEED = 42


def br(n, casas=0):
    """Formata número no padrão brasileiro: 1.234,5"""
    s = f"{n:,.{casas}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def pct(x, casas=0):
    """Formata proporção como percentual brasileiro: 0,123 -> 12%"""
    return br(x * 100, casas) + "%"


def limpa(ax):
    """Visual limpo para gráficos executivos."""
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="y", alpha=0.25)
    ax.set_axisbelow(True)


def formatador_br(casas=0):
    """Formatter de eixo com números no padrão brasileiro."""
    return FuncFormatter(lambda v, _: br(v, casas))
