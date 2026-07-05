from django.urls import path
from . import views

app_name = "reservas"

urlpatterns = [
    path("", views.ReservaListView.as_view(), name="lista"),
    path("nueva/", views.ReservaCreateView.as_view(), name="crear"),
    path("nueva/<str:fecha>/<str:hora>/", views.ReservaCreateView.as_view(), name="crear_con_hora"),
    path("<int:pk>/editar/", views.ReservaUpdateView.as_view(), name="editar"),
    path("<int:pk>/eliminar/", views.ReservaDeleteView.as_view(), name="eliminar"),
    path("agenda/", views.agenda, name="agenda"),
]