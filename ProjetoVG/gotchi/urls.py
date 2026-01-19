from django.urls import path
from .views import gotchi_status_view

app_name = "gotchi"

urlpatterns = [
    path("status/", gotchi_status_view, name="status"),
]
