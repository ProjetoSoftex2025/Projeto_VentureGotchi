from gotchi.services.xp_service import add_xp
from achievements.models import UserAchievement


def unlock_achievement(user, achievement) -> None:
    """
    Desbloqueia uma conquista para o usuário, se ainda não existir.
    """

    obj, created = UserAchievement.objects.get_or_create(
        user=user,
        achievement=achievement
    )

    if created and achievement.xp_bonus > 0:
        # Entrega bônus de XP ao Gotchi
        add_xp(user.gotchi, achievement.xp_bonus)
