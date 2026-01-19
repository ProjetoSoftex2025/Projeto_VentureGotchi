from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # Dashboard (home do sistema)
    path("", include("dashboard.urls")),

    # Apps
    #path("accounts/", include("accounts.urls")),
    path("accounts/", include(("accounts.urls", "accounts"), namespace="accounts")),
    path("missions/", include("missions.urls")),
    path("achievements/", include("achievements.urls")),
]
