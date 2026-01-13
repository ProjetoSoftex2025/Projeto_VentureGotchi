from django.utils import timezone

from gotchi.services.xp_service import add_xp
from missions.models import MissionProgress


def complete_mission(user, mission) -> None:
    """
    Marca missão como concluída e entrega XP ao Gotchi.
    """

    progress, created = MissionProgress.objects.get_or_create(
        user=user,
        mission=mission
    )

    if not progress.completed:
        progress.completed = True
        progress.completed_at = timezone.now()
        progress.save()

        # Entrega XP ao Gotchi
        add_xp(user.gotchi, mission.xp_reward)