from django.shortcuts import render

# from django.http import HttpResponse


def home(request):
    # return HttpResponse("<h1> Bem Vindos à Venture Gotchi!</h1>")
    context = {
        "nome_usuario": "Gotcher",
        "atividades": ["Desafio_01", "Desafio_02", "Desafio_03"],
    }
    return render(request, "home.html", context)


def dashboard(request):
    # Função chamando a página dashboard.html
    return render(request, "dashboard.html")


def progresso(request):
    # Função chamando a página progresso.html
# Importa a função render do Django, que serve para juntar um template HTML com dados
from django.shortcuts import render

# Define a view chamada progresso
def progresso(request):
    # XP simulado (futuramente esse valor virá do banco de dados do usuário)
    xp = 120

    # Lógica de nível baseada no XP
    if xp < 100:
        # Se o XP for menor que 100, o nível é Iniciante
        nivel = "Iniciante"
        # O próximo nível que o usuário pode alcançar é Intermediário
        proximo = "Intermediário"
        # A porcentagem de progresso é igual ao próprio XP, já que o limite é 100
        porcentagem = xp

    elif xp < 300:
        # Se o XP estiver entre 100 e 299, o nível é Intermediário
        nivel = "Intermediário"
        # O próximo nível será Avançado
        proximo = "Avançado"
        # Calcula a porcentagem de progresso em relação ao limite de 300
        porcentagem = int((xp / 300) * 100)

    else:
        # Se o XP for 300 ou mais, o nível é Avançado
        nivel = "Avançado"
        # O próximo nível é Máximo
        proximo = "Máximo"
        # Como já atingiu ou passou o limite, a porcentagem fica fixa em 100
        porcentagem = 100

    # Cria um dicionário chamado context, que guarda todas as informações
    # Esse dicionário será enviado para o template HTML
    context = {
        "xp": xp,                # quantidade de experiência atual
        "nivel": nivel,          # nível atual do usuário
        "proximo": proximo,      # próximo nível que ele pode alcançar
        "porcentagem": porcentagem  # porcentagem de progresso até o próximo nível
    }

    # Renderiza o template progresso.html, passando o contexto com os dados
    return render(request, "progresso.html", context)
