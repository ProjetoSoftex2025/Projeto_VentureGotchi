from django.urls import path
from .views import dashboard_view, index

app_name = "dashboard"

urlpatterns = [
    path("", dashboard_view, name="index"),
    #path("", index, name="index")
]