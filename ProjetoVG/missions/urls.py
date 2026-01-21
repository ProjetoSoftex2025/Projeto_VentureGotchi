
# missions/urls.py
from django.urls import path
from . import views
from django.urls import path
from .views import mission_list_view, complete_mission_view

app_name = "missions"

urlpatterns = [
    path("", views.missions_list, name="list"),
    path("", mission_list_view, name="list"),
    path("complete/<int:mission_id>/", complete_mission_view, name="complete"),
]
