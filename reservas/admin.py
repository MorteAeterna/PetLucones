from django.contrib import admin
from .models import Reserva


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):

    list_display = (
        "mascota",
        "servicio",
        "fecha",
        "hora",
        "estado",
    )

    list_filter = (
        "estado",
        "fecha",
    )

    search_fields = (
        "mascota__nombre",
    )