from django.utils import timezone
from django.db import transaction

from gotchi.models import Gotchi
from gotchi.services.xp_service import add_xp
from missions.models import MissionProgress


@transaction.atomic
def complete_mission(user, mission) -> None:
    """
    Marca missão como concluída e entrega XP ao Gotchi.
    """

    progress, _ = MissionProgress.objects.get_or_create(
        user=user,
        mission=mission
    )

    if progress.completed:
        return

    progress.completed = True
    progress.completed_at = timezone.now()
    progress.save(update_fields=["completed", "completed_at"])

    # 🔥 GARANTIA DE EXISTÊNCIA DO GOTCHI
    gotchi, _ = Gotchi.objects.get_or_create(user=user)

    add_xp(gotchi, mission.xp_reward)
