from django.urls import path
from . import views

app_name = "missions"

urlpatterns = [
    path("", views.mission_list_view, name="list"),
    path("<int:mission_id>/complete/", views.complete_mission_view, name="complete"),
    path("create/", views.create_mission_view, name="create"),
    path("detail/<int:mission_id>/", views.mission_detail_view, name="detail"),
]
