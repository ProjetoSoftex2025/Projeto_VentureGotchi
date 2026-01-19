"""
Serviço responsável por TODA lógica de XP e evolução.

Centralizar esta lógica evita duplicações
e bugs de progressão espalhados pelo projeto.
"""

from django.db import transaction


def xp_to_next_level(level: int) -> int:
    """
    Fórmula simples e previsível de progressão.
    Pode ser refinada futuramente.
    """
    return level * 100


@transaction.atomic
def add_xp(gotchi, amount: int) -> None:
    """
    Adiciona XP ao Gotchi e processa level up automaticamente.
    Operação atômica.
    """

    if amount <= 0:
        return

    gotchi.xp += amount

    while gotchi.xp >= xp_to_next_level(gotchi.level):
        gotchi.xp -= xp_to_next_level(gotchi.level)
        gotchi.level += 1

    gotchi.save(update_fields=["xp", "level"])
