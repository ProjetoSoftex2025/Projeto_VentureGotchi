def usuario_no_grupo(user, nome_grupo):
    if not user.is_authenticated:
        return False
    return user.groups.filter(name=nome_grupo).exists()
