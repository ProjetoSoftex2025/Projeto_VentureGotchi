from django.db import transaction
from gotchi.models import Gotchi
from missions.models import Mission


XP_PER_LEVEL = 100


def calculate_level(xp: int) -> int:
    """
    Regra simples de nível:
    cada 100 XP = 1 nível
    """
    return max(1, xp // XP_PER_LEVEL)


@transaction.atomic
def complete_mission(user, mission_id: int) -> Gotchi:
    """
    Marca missão como concluída,
    adiciona XP ao Gotchi
    e recalcula o nível.
    """

    mission = Mission.objects.select_for_update().get(
        id=mission_id,
        user=user,
        completed=False
    )

    gotchi = Gotchi.objects.select_for_update().get(user=user)

    # 1. Concluir missão
    mission.completed = True
    mission.save()

    # 2. Ganhar XP
    gotchi.xp += mission.xp_reward

    # 3. Recalcular nível
    gotchi.level = calculate_level(gotchi.xp)

    gotchi.save()

    return gotchi
