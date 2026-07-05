from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from core.views import dashboard

urlpatterns = [
    path("admin/", admin.site.urls),

    path(
        "login/",
        auth_views.LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),

    path("", dashboard, name="dashboard"),
    path("clientes/", include("clientes.urls")),
    path("mascotas/", include("mascotas.urls")),
    path("servicios/", include("servicios.urls")),
    path("reservas/", include("reservas.urls")),
]