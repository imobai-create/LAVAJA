"""Funcoes financeiras e tributarias compartilhadas. Sem dependencias externas."""

# ---------------------------------------------------------------- financeiras

def vpl(taxa_mensal, fluxos):
    return sum(f / (1 + taxa_mensal) ** i for i, f in enumerate(fluxos))


def tir_mensal(fluxos, lo=-0.95, hi=3.0, it=300):
    """TIR mensal por bisseccao. Retorna None se nao houver troca de sinal."""
    f = lambda r: vpl(r, fluxos)
    if f(lo) * f(hi) > 0:
        return None
    for _ in range(it):
        m = (lo + hi) / 2
        if f(lo) * f(m) <= 0:
            hi = m
        else:
            lo = m
    return (lo + hi) / 2


def tir_anual(fluxos):
    r = tir_mensal(fluxos)
    return None if r is None else (1 + r) ** 12 - 1


def payback(fluxos):
    """Primeiro mes em que o caixa acumulado fica >= 0. None se nunca."""
    acc = 0.0
    for i, f in enumerate(fluxos):
        acc += f
        if i > 0 and acc >= 0:
            return i
    return None


def mensal(taxa_anual):
    return (1 + taxa_anual) ** (1 / 12) - 1


# ---------------------------------------------------------------- tributarias

# Simples Nacional, Anexo III (LC 123/2006). Faixa: (teto RBT12, aliquota, deducao)
ANEXO_III = [
    (180_000, 0.060, 0),
    (360_000, 0.112, 9_360),
    (720_000, 0.135, 17_640),
    (1_800_000, 0.160, 35_640),
    (3_600_000, 0.210, 125_640),
    (4_800_000, 0.330, 648_000),
]

# Anexo V, para o caso de o Fator R jogar a atividade para la.
ANEXO_V = [
    (180_000, 0.155, 0),
    (360_000, 0.180, 4_500),
    (720_000, 0.195, 9_900),
    (1_800_000, 0.205, 17_100),
    (3_600_000, 0.230, 62_100),
    (4_800_000, 0.305, 540_000),
]


def aliquota_simples(rbt12, tabela=ANEXO_III):
    """Aliquota efetiva do Simples sobre a receita, dado o RBT12."""
    if rbt12 <= 0:
        return tabela[0][1]
    for teto, aliq, ded in tabela:
        if rbt12 <= teto:
            return max(0.0, (rbt12 * aliq - ded) / rbt12)
    # acima do teto do Simples: estimativa de Lucro Presumido sobre servicos
    return 0.165


def brl(v, casas=0):
    s = f"{v:,.{casas}f}".replace(",", "@").replace(".", ",").replace("@", ".")
    return s
