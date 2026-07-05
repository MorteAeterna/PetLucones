from django.urls import path
from . import views

app_name = "servicios"

urlpatterns = [
    path("", views.ServicioListView.as_view(), name="lista"),
    path("nuevo/", views.ServicioCreateView.as_view(), name="crear"),
    path("<int:pk>/editar/", views.ServicioUpdateView.as_view(), name="editar"),
    path("<int:pk>/eliminar/", views.ServicioDeleteView.as_view(), name="eliminar"),
]