from django.urls import path
from . import views

app_name = 'missions'  # Certifique-se de que isso está aqui para o namespace

urlpatterns = [
    path('', views.mission_list_view, name='list'),
    path('complete/<int:mission_id>/', views.complete_mission_view, name='complete'),
    path('uncomplete/<int:mission_id>/', views.uncomplete_mission_view, name='uncomplete'),  # Corrigido: agora chama 'uncomplete_mission_view'
    path('create/', views.create_mission_view, name='create'),
    path('<int:mission_id>/', views.mission_detail_view, name='detail'),
]